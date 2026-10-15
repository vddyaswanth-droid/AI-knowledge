"""
AutoSage - Beginner-Friendly Web-Based Car Health Analysis System
Flask Web Server and REST API
"""

from flask import Flask, render_template, request, jsonify
import os
import json
from rule_engine import CarHealthRuleEngine
from knowledge_base import SYMPTOMS, SUBSYSTEMS, GENERAL_DIY_CHECKLIST, MECHANIC_CONVERSATION_TIPS
import database as db

app = Flask(__name__,
            static_folder="static",
            template_folder="templates")

# Initialize Engine and Database
rule_engine = CarHealthRuleEngine()
db.init_db()
db.seed_sample_history(rule_engine)

# Presets for rapid demo/testing
PRESET_SCENARIOS = [
    {
        "id": "preset_overheating",
        "title": "Severe Overheating & White Smoke",
        "description": "Temperature gauge in red, thick white smoke from tailpipe, sweet maple odor.",
        "vehicle": {
            "make": "Ford",
            "model": "F-150 XLT",
            "year": 2015,
            "mileage": 118000,
            "fuel_type": "Gasoline",
            "transmission": "Automatic",
            "nickname": "Work Truck"
        },
        "symptoms": ["engine_overheating", "white_exhaust_smoke", "sweet_syrup_smell"],
        "conditions": {
            "occurs_when": "heavy stop-and-go traffic and hill climbing",
            "frequency": "constant"
        }
    },
    {
        "id": "preset_vibration",
        "title": "Highway Speed Shudder & Braking Wobble",
        "description": "Steering wheel shakes at 65 mph, and brake pedal pulses during highway deceleration.",
        "vehicle": {
            "make": "Honda",
            "model": "Civic EX",
            "year": 2018,
            "mileage": 64000,
            "fuel_type": "Gasoline",
            "transmission": "CVT",
            "nickname": "Daily Commuter"
        },
        "symptoms": ["highway_vibration", "brake_pulsation_vibration"],
        "conditions": {
            "occurs_when": "highway cruising (60-70 mph) and when braking",
            "frequency": "every trip"
        }
    },
    {
        "id": "preset_starting",
        "title": "Sluggish Cold Morning Crank & Dim Lights",
        "description": "Labored slow crank on chilly mornings, rapid clicking sound, dim headlights at idle.",
        "vehicle": {
            "make": "Toyota",
            "model": "RAV4 AWD",
            "year": 2020,
            "mileage": 48000,
            "fuel_type": "Gasoline",
            "transmission": "Automatic",
            "nickname": "Family SUV"
        },
        "symptoms": ["slow_engine_crank", "clicking_when_starting", "dim_flickering_lights"],
        "conditions": {
            "occurs_when": "cold start in the morning",
            "frequency": "intermittent"
        }
    },
    {
        "id": "preset_mpg_drop",
        "title": "Sudden Drop in Fuel Efficiency & Rough Idle",
        "description": "Car feels sluggish when accelerating, shakes at red lights, fuel economy dropped 25%.",
        "vehicle": {
            "make": "Volkswagen",
            "model": "Golf TSI",
            "year": 2017,
            "mileage": 82000,
            "fuel_type": "Gasoline",
            "transmission": "Automatic",
            "nickname": "VW Golf"
        },
        "symptoms": ["reduced_fuel_economy", "sluggish_acceleration", "engine_rough_idle", "check_engine_light_steady"],
        "conditions": {
            "occurs_when": "accelerating and stopped in Drive",
            "frequency": "constant"
        }
    }
]

@app.route("/")
def index():
    """Renders the main single-page application dashboard."""
    return render_template("index.html")

@app.route("/api/symptoms", methods=["GET"])
def get_symptoms():
    """Returns the symptom catalog organized by category."""
    categories = {}
    for sym_id, sym_data in SYMPTOMS.items():
        cat = sym_data["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(sym_data)
    
    return jsonify({
        "categories": categories,
        "all_symptoms": SYMPTOMS,
        "subsystems": SUBSYSTEMS
    })

@app.route("/api/presets", methods=["GET"])
def get_presets():
    """Returns pre-configured realistic test cases."""
    return jsonify(PRESET_SCENARIOS)

@app.route("/api/analyze", methods=["POST"])
def analyze_vehicle():
    """
    Analyzes submitted vehicle details and symptoms using the rule engine,
    saves the report to SQLite history, and returns full diagnostics.
    """
    data = request.get_json() or {}
    vehicle = data.get("vehicle", {})
    symptoms = data.get("symptoms", [])
    conditions = data.get("conditions", {})
    save_history = data.get("save_history", True)
    user_notes = data.get("user_notes", "")

    # Run Rule Engine Analysis
    result = rule_engine.analyze(vehicle=vehicle, symptoms=symptoms, conditions=conditions)
    result["conditions"] = conditions

    # Save to SQLite Database
    report_id = None
    if save_history:
        report_id = db.save_report(result, user_notes=user_notes)
        result["report_id"] = report_id

    return jsonify(result)

@app.route("/api/reports", methods=["GET"])
def list_reports():
    """Lists recent diagnostic reports with summary data."""
    limit = request.args.get("limit", default=50, type=int)
    reports = db.get_reports(limit=limit)
    return jsonify(reports)

@app.route("/api/reports/<int:report_id>", methods=["GET"])
def get_report(report_id):
    """Retrieves full details of a specific report."""
    report = db.get_report_by_id(report_id)
    if not report:
        return jsonify({"error": "Report not found"}), 404
    return jsonify(report)

@app.route("/api/reports/<int:report_id>/status", methods=["POST"])
def update_report_status(report_id):
    """Updates the resolved state or notes of a report."""
    data = request.get_json() or {}
    resolved = 1 if data.get("resolved") else 0
    notes = data.get("user_notes", "")
    success = db.update_report_status(report_id, resolved, notes)
    if not success:
        return jsonify({"error": "Report not found or update failed"}), 404
    return jsonify({"success": True})

@app.route("/api/reports/<int:report_id>", methods=["DELETE"])
def delete_report(report_id):
    """Deletes a report by ID."""
    success = db.delete_report(report_id)
    if not success:
        return jsonify({"error": "Report not found"}), 404
    return jsonify({"success": True})

@app.route("/api/compare/<int:id1>/<int:id2>", methods=["GET"])
def compare_reports(id1, id2):
    """Compares two historical reports side-by-side."""
    comparison = db.compare_reports(id1, id2)
    if "error" in comparison:
        return jsonify(comparison), 400
    return jsonify(comparison)

@app.route("/api/education", methods=["GET"])
def get_educational_resources():
    """Returns general DIY checklists, tips, and fluid guides."""
    return jsonify({
        "diy_checklist": GENERAL_DIY_CHECKLIST,
        "mechanic_tips": MECHANIC_CONVERSATION_TIPS
    })

if __name__ == "__main__":
    # Run locally on port 5000
    print("Starting AutoSage Server on http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=True)
