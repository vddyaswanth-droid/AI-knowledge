"""
AutoSage Rule Engine
Analyzes vehicle details, symptoms, and operating conditions to compute
diagnostics, urgency levels, subsystem impacts, and visual Car Health Fingerprints.
"""

from typing import Dict, List, Any
import hashlib
import time
from knowledge_base import SUBSYSTEMS, SYMPTOMS, DIAGNOSTIC_RULES, GENERAL_DIY_CHECKLIST

class CarHealthRuleEngine:
    def __init__(self):
        self.subsystems = SUBSYSTEMS
        self.symptoms_catalog = SYMPTOMS
        self.rules = DIAGNOSTIC_RULES

    def analyze(self, vehicle: Dict[str, Any], symptoms: List[str], conditions: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Main diagnostic pipeline:
        1. Validates selected symptoms against catalog
        2. Evaluates multi-symptom combination rules
        3. Falls back to individual symptom impacts if no compound rule matches
        4. Calculates subsystem health degradation
        5. Computes overall vehicle health score and urgency rating
        6. Generates Car Health Fingerprint radar vector and unique hash
        7. Compiles DIY inspection checklist and mechanic discussion points
        """
        conditions = conditions or {}
        selected_set = set(symptoms)

        matched_rules = []
        covered_symptoms = set()

        # Step 1: Match compound diagnostic rules
        for rule in self.rules:
            req = set(rule.get("required_symptoms", []))
            opt = set(rule.get("optional_symptoms", []))
            match_type = rule.get("match_type", "all")

            is_match = False
            matched_req = req.intersection(selected_set)
            matched_opt = opt.intersection(selected_set)

            if match_type == "all":
                if req and req.issubset(selected_set):
                    is_match = True
            elif match_type == "any":
                if len(matched_req) > 0:
                    is_match = True

            if is_match:
                # Calculate confidence percentage based on base score and optional matches
                confidence = rule.get("min_score", 70)
                if opt and len(opt) > 0:
                    bonus = int((len(matched_opt) / len(opt)) * 15)
                    confidence = min(98, confidence + bonus)

                # Contextual condition bonus
                driving_condition = conditions.get("occurs_when", "")
                if driving_condition:
                    if "braking" in driving_condition and "brake" in rule["id"].lower():
                        confidence = min(99, confidence + 5)
                    elif "highway" in driving_condition and "highway" in rule["id"].lower():
                        confidence = min(99, confidence + 5)

                rule_copy = dict(rule)
                rule_copy["confidence"] = confidence
                rule_copy["matched_symptoms"] = list(matched_req.union(matched_opt))
                matched_rules.append(rule_copy)
                covered_symptoms.update(matched_req.union(matched_opt))

        # Sort matched rules by urgency and confidence
        urgency_weight = {"critical": 4, "high": 3, "moderate": 2, "low": 1}
        matched_rules.sort(
            key=lambda r: (urgency_weight.get(r.get("urgency", "low"), 0), r.get("confidence", 0)),
            reverse=True
        )

        # Step 2: Handle any leftover symptoms with single-symptom fallback evaluation
        uncovered_symptoms = selected_set - covered_symptoms
        fallback_causes = []
        for sym_id in uncovered_symptoms:
            sym_meta = self.symptoms_catalog.get(sym_id)
            if not sym_meta:
                continue

            subsystem_key = sym_meta.get("subsystem", "powertrain")
            severity = sym_meta.get("base_severity", "moderate")
            
            deduction = {"critical": 60, "high": 40, "moderate": 25, "low": 15}.get(severity, 20)
            fallback_causes.append({
                "id": f"GENERIC_{sym_id.upper()}",
                "confidence": 60,
                "urgency": severity,
                "urgency_label": f"{severity.upper()}: Inspection Recommended",
                "title": f"Issue Detected: {sym_meta['title']}",
                "subsystem_impacts": {subsystem_key: deduction},
                "explanation": f"Reported symptom '{sym_meta['title']}' indicates potential wear or operational anomaly within the vehicle's {self.subsystems.get(subsystem_key, {}).get('name', 'subsystem')}.",
                "risk_explanation": f"Leaving '{sym_meta['title']}' unaddressed can lead to secondary component wear or sudden breakdown.",
                "diy_checks": [
                    f"Perform a thorough visual check of the {self.subsystems.get(subsystem_key, {}).get('name', 'vehicle')} components.",
                    "Verify all relevant fluid levels, belt tensions, and warning indicators.",
                    "Note down exact driving conditions when the symptom recurs for your technician."
                ],
                "mechanic_questions": [
                    f"Can you inspect components related to {sym_meta['title']}?",
                    "Are there any associated fault codes stored in history?"
                ],
                "estimated_cost_tier": "Diagnostic Check ($80 - $180)",
                "matched_symptoms": [sym_id]
            })

        all_probable_causes = matched_rules + fallback_causes

        # Step 3: Compute Subsystem Health Scores (0 to 100)
        # 100 = Pristine / No symptoms reported
        subsystem_scores = {key: 100 for key in self.subsystems.keys()}
        subsystem_issues = {key: [] for key in self.subsystems.keys()}

        # Factor in vehicle mileage aging factor (subtle baseline wear)
        mileage = vehicle.get("mileage")
        try:
            mileage = float(mileage) if mileage is not None else 0
        except (ValueError, TypeError):
            mileage = 0

        mileage_wear = min(8, int(mileage / 35000))  # Max 8 points baseline wear for high mileage

        for key in subsystem_scores:
            subsystem_scores[key] -= mileage_wear

        # Apply impacts from matched rules & causes
        for cause in all_probable_causes:
            impacts = cause.get("subsystem_impacts", {})
            for sub_key, penalty in impacts.items():
                if sub_key in subsystem_scores:
                    subsystem_scores[sub_key] -= penalty
                    subsystem_issues[sub_key].append(cause["title"])

        # Clamp subsystem scores between 10 and 100
        for sub_key in subsystem_scores:
            subsystem_scores[sub_key] = max(10, min(100, subsystem_scores[sub_key]))

        # Step 4: Overall Health Score
        # Weighted between minimum compromised system and global average
        score_values = list(subsystem_scores.values())
        min_subsystem = min(score_values)
        avg_subsystem = sum(score_values) / len(score_values)
        overall_health_score = int(round(0.45 * min_subsystem + 0.55 * avg_subsystem))
        overall_health_score = max(5, min(100, overall_health_score))

        # Overall Health Rating & Urgency Classification
        if any(cause.get("urgency") == "critical" for cause in all_probable_causes) or min_subsystem < 30:
            overall_urgency = "critical"
            urgency_badge = "CRITICAL / DO NOT DRIVE"
            health_status = "Severe Danger - Immediate Attention Required"
            health_color = "#ef4444" # red
        elif any(cause.get("urgency") == "high" for cause in all_probable_causes) or min_subsystem < 50:
            overall_urgency = "high"
            urgency_badge = "HIGH PRIORITY / SCHEDULE SOON"
            health_status = "Compromised - Schedule Service Promptly"
            health_color = "#f97316" # orange
        elif any(cause.get("urgency") == "moderate" for cause in all_probable_causes) or min_subsystem < 75:
            overall_urgency = "moderate"
            urgency_badge = "MODERATE / ROUTINE SERVICE"
            health_status = "Fair - Maintenance Needed"
            health_color = "#eab308" # yellow
        elif len(symptoms) > 0:
            overall_urgency = "low"
            urgency_badge = "LOW / MONITOR VEHICLE"
            health_status = "Good Condition - Minor Watch Items"
            health_color = "#22c55e" # green
        else:
            overall_urgency = "clean"
            urgency_badge = "OPTIMAL / HEALTHY"
            health_status = "Optimal Vehicle Condition"
            health_color = "#10b981" # emerald

        # Step 5: Generate Car Health Fingerprint Vector & Hash
        # Fingerprint vector format: [powertrain, transmission, brakes, suspension, electrical, emissions_fuel]
        fingerprint_vector = {
            "powertrain": subsystem_scores["powertrain"],
            "transmission": subsystem_scores["transmission"],
            "brakes": subsystem_scores["brakes"],
            "suspension": subsystem_scores["suspension"],
            "electrical": subsystem_scores["electrical"],
            "emissions_fuel": subsystem_scores["emissions_fuel"]
        }

        # Deterministic Fingerprint Identifier Code
        year_str = str(vehicle.get("year", "2026"))[-2:]
        urgency_code_map = {"critical": "CRT", "high": "HGH", "moderate": "MOD", "low": "LOW", "clean": "OPT"}
        urg_code = urgency_code_map.get(overall_urgency, "MOD")
        
        fingerprint_hash_str = f"AS{year_str}-P{fingerprint_vector['powertrain']}-B{fingerprint_vector['brakes']}-T{fingerprint_vector['transmission']}-E{fingerprint_vector['electrical']}-S{fingerprint_vector['suspension']}-F{fingerprint_vector['emissions_fuel']}-{urg_code}"

        # Step 6: Curate Pre-Mechanic Checklist and Action Plan
        action_checklist = []
        seen_checks = set()
        for cause in all_probable_causes:
            for chk in cause.get("diy_checks", []):
                if chk not in seen_checks:
                    seen_checks.add(chk)
                    action_checklist.append({
                        "source": cause["title"],
                        "urgency": cause["urgency"],
                        "task": chk
                    })

        # Step 7: Subsystem details enriched for frontend
        subsystem_report = []
        for key, meta in self.subsystems.items():
            sub_score = subsystem_scores[key]
            if sub_score >= 85:
                sub_status = "Good"
                sub_class = "status-good"
            elif sub_score >= 65:
                sub_status = "Fair / Wear Detected"
                sub_class = "status-warning"
            elif sub_score >= 40:
                sub_status = "Degraded / Needs Service"
                sub_class = "status-high"
            else:
                sub_status = "Critical Risk"
                sub_class = "status-critical"

            subsystem_report.append({
                "key": key,
                "name": meta["name"],
                "icon": meta["icon"],
                "score": sub_score,
                "status": sub_status,
                "status_class": sub_class,
                "issues": subsystem_issues[key]
            })

        return {
            "vehicle": vehicle,
            "symptoms_reported": [self.symptoms_catalog.get(sid, {"id": sid, "title": sid}) for sid in symptoms],
            "overall_health_score": overall_health_score,
            "overall_urgency": overall_urgency,
            "urgency_badge": urgency_badge,
            "health_status": health_status,
            "health_color": health_color,
            "subsystem_scores": subsystem_scores,
            "subsystems_report": subsystem_report,
            "fingerprint_vector": fingerprint_vector,
            "fingerprint_code": fingerprint_hash_str,
            "probable_causes": all_probable_causes,
            "diy_checklist": action_checklist,
            "general_inspection_guide": GENERAL_DIY_CHECKLIST,
            "generated_at": int(time.time())
        }
