"""
AutoSage Database Module
SQLite-backed storage for diagnostic runs, vehicle profiles, historical reports,
and temporal Car Health Fingerprint comparison.
"""

import sqlite3
import json
import os
import time
from typing import List, Dict, Any, Optional

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "autosage.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes the SQLite database tables."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            vehicle_make TEXT NOT NULL,
            vehicle_model TEXT NOT NULL,
            vehicle_year INTEGER NOT NULL,
            vehicle_mileage INTEGER DEFAULT 0,
            vehicle_fuel TEXT DEFAULT 'Gasoline',
            vehicle_transmission TEXT DEFAULT 'Automatic',
            vehicle_nickname TEXT,
            symptoms_json TEXT NOT NULL,
            conditions_json TEXT,
            overall_score INTEGER NOT NULL,
            urgency TEXT NOT NULL,
            fingerprint_code TEXT NOT NULL,
            fingerprint_vector_json TEXT NOT NULL,
            full_result_json TEXT NOT NULL,
            user_notes TEXT,
            resolved INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def save_report(analysis_result: Dict[str, Any], user_notes: str = "") -> int:
    """Saves a new vehicle diagnostic analysis report."""
    vehicle = analysis_result.get("vehicle", {})
    conn = get_db_connection()
    cursor = conn.cursor()

    symptoms_list = [s.get("id") if isinstance(s, dict) else s for s in analysis_result.get("symptoms_reported", [])]

    cursor.execute("""
        INSERT INTO reports (
            vehicle_make, vehicle_model, vehicle_year, vehicle_mileage,
            vehicle_fuel, vehicle_transmission, vehicle_nickname,
            symptoms_json, conditions_json, overall_score, urgency,
            fingerprint_code, fingerprint_vector_json, full_result_json,
            user_notes, resolved
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        vehicle.get("make", "Unknown"),
        vehicle.get("model", "Vehicle"),
        int(vehicle.get("year", 2020)),
        int(vehicle.get("mileage", 0)),
        vehicle.get("fuel_type", "Gasoline"),
        vehicle.get("transmission", "Automatic"),
        vehicle.get("nickname", f"{vehicle.get('year', '')} {vehicle.get('make', '')} {vehicle.get('model', '')}".strip()),
        json.dumps(symptoms_list),
        json.dumps(analysis_result.get("conditions", {})),
        int(analysis_result.get("overall_health_score", 100)),
        analysis_result.get("overall_urgency", "moderate"),
        analysis_result.get("fingerprint_code", ""),
        json.dumps(analysis_result.get("fingerprint_vector", {})),
        json.dumps(analysis_result),
        user_notes,
        0
    ))
    report_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return report_id

def get_reports(limit: int = 50) -> List[Dict[str, Any]]:
    """Retrieves previous diagnostic reports list."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, created_at, vehicle_make, vehicle_model, vehicle_year,
               vehicle_mileage, vehicle_nickname, overall_score, urgency,
               fingerprint_code, fingerprint_vector_json, symptoms_json, user_notes, resolved
        FROM reports
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))
    rows = cursor.fetchall()
    conn.close()

    reports = []
    for row in rows:
        r = dict(row)
        try:
            r["fingerprint_vector"] = json.loads(r["fingerprint_vector_json"])
            r["symptoms"] = json.loads(r["symptoms_json"])
        except Exception:
            r["fingerprint_vector"] = {}
            r["symptoms"] = []
        reports.append(r)
    return reports

def get_report_by_id(report_id: int) -> Optional[Dict[str, Any]]:
    """Retrieves a single full diagnostic report by ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reports WHERE id = ?", (report_id,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        return None

    r = dict(row)
    try:
        r["full_result"] = json.loads(r["full_result_json"])
        r["fingerprint_vector"] = json.loads(r["fingerprint_vector_json"])
        r["symptoms"] = json.loads(r["symptoms_json"])
        if r.get("conditions_json"):
            r["conditions"] = json.loads(r["conditions_json"])
    except Exception:
        pass
    return r

def delete_report(report_id: int) -> bool:
    """Deletes a diagnostic report."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reports WHERE id = ?", (report_id,))
    deleted = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return deleted

def update_report_status(report_id: int, resolved: int, notes: str) -> bool:
    """Updates resolution status and user notes for a report."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE reports
        SET resolved = ?, user_notes = ?
        WHERE id = ?
    """, (resolved, notes, report_id))
    updated = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return updated

def compare_reports(report_id_1: int, report_id_2: int) -> Dict[str, Any]:
    """
    Compares two diagnostic reports side-by-side.
    Computes health delta, subsystem improvements/declines, and fingerprint progression.
    """
    rep1 = get_report_by_id(report_id_1)
    rep2 = get_report_by_id(report_id_2)

    if not rep1 or not rep2:
        return {"error": "One or both reports not found."}

    # Ensure chronological order: rep1 is older (baseline), rep2 is newer
    if rep1["id"] > rep2["id"]:
        rep1, rep2 = rep2, rep1

    vec1 = rep1.get("fingerprint_vector", {})
    vec2 = rep2.get("fingerprint_vector", {})

    subsystems = ["powertrain", "transmission", "brakes", "suspension", "electrical", "emissions_fuel"]
    subsystem_deltas = {}
    for sub in subsystems:
        s1 = vec1.get(sub, 100)
        s2 = vec2.get(sub, 100)
        subsystem_deltas[sub] = {
            "initial": s1,
            "current": s2,
            "delta": s2 - s1
        }

    score_delta = rep2["overall_score"] - rep1["overall_score"]
    mileage_delta = rep2["vehicle_mileage"] - rep1["vehicle_mileage"]

    # Qualitative comparison summary
    if score_delta > 10:
        summary_verdict = f"Significant Health Improvement (+{score_delta} points). Resolved wear items restored subsystem health."
        verdict_class = "improvement"
    elif score_delta < -10:
        summary_verdict = f"Vehicle Health Deterioration ({score_delta} points). New symptoms or unresolved wear have compounded."
        verdict_class = "decline"
    else:
        summary_verdict = "Vehicle Health Stable (minimal change in overall score)."
        verdict_class = "stable"

    return {
        "report_baseline": rep1,
        "report_current": rep2,
        "score_delta": score_delta,
        "mileage_delta": mileage_delta,
        "subsystem_deltas": subsystem_deltas,
        "summary_verdict": summary_verdict,
        "verdict_class": verdict_class
    }

def seed_sample_history(rule_engine):
    """Seeds realistic sample reports if the database is newly initialized."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM reports")
    count = cursor.fetchone()[0]
    conn.close()

    if count > 0:
        return

    # Seed 1: 2018 Honda Civic - Vibrations when braking (Warped rotors)
    civic_run_1 = rule_engine.analyze(
        vehicle={"make": "Honda", "model": "Civic EX", "year": 2018, "mileage": 62400, "transmission": "CVT", "fuel_type": "Gasoline", "nickname": "Daily Civic"},
        symptoms=["brake_pulsation_vibration", "highway_vibration"],
        conditions={"occurs_when": "braking from highway speed"}
    )
    save_report(civic_run_1, user_notes="Noticed steering wheel shudder when braking on highway off-ramp.")

    # Seed 2: 2018 Honda Civic - 2 months later after front rotor replacement (Follow-up check)
    civic_run_2 = rule_engine.analyze(
        vehicle={"make": "Honda", "model": "Civic EX", "year": 2018, "mileage": 64100, "transmission": "CVT", "fuel_type": "Gasoline", "nickname": "Daily Civic"},
        symptoms=["highway_vibration"],
        conditions={"occurs_when": "slight steering vibration over 65mph"}
    )
    r2_id = save_report(civic_run_2, user_notes="Front rotors replaced. Still slight highway vibration from tire balance.")
    update_report_status(r2_id, 1, "Front brake rotors replaced with ceramic pads. Braking pulsation completely eliminated!")

    # Seed 3: 2015 Ford F-150 - Overheating & sweet syrup smell
    f150_run = rule_engine.analyze(
        vehicle={"make": "Ford", "model": "F-150 XLT", "year": 2015, "mileage": 118000, "transmission": "Automatic", "fuel_type": "Gasoline", "nickname": "Work Truck"},
        symptoms=["engine_overheating", "sweet_syrup_smell", "white_exhaust_smoke"],
        conditions={"occurs_when": "heavy traffic and uphill climbing"}
    )
    save_report(f150_run, user_notes="Temp gauge climbed to red line. Noticed sweet pancake odor and white smoke.")
