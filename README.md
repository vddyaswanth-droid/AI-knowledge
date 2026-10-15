# AutoSage 🚗
### Beginner-Friendly Web-Based Car Health Analysis System

AutoSage empowers everyday drivers to diagnose automotive symptoms without OBD-II scanners or specialized technical knowledge. By analyzing combinations of symptoms using a Python-based rule engine, AutoSage provides plain-English cause explanations, urgency ratings, safe DIY inspection checklists, and a visual **Car Health Fingerprint**.

---

## 🌟 Key Features

1. **Intelligent Multi-Symptom Rule Engine**:
   - Detects compound multi-symptom patterns (e.g., *Engine Overheating* + *White Exhaust Smoke* + *Sweet Syrup Smell* = **Blown Head Gasket**; *Highway Vibration* + *Steering Shake under Braking* = **Warped Rotors**).
   - Accurately classifies urgency into **Critical** (Do Not Drive), **High** (Prompt Service), **Moderate** (Schedule Within Weeks), and **Low/Routine**.
   - Calculates impact scores across 6 vehicle subsystems: Engine/Powertrain, Transmission, Brakes, Suspension & Steering, Electrical, and Fuel & Emissions.

2. **Visual Car Health Fingerprint**:
   - Generates an interactive 6-axis Radar (Spider) Chart representing the complete health profile of the vehicle.
   - Generates a deterministic **Fingerprint ID Code** (e.g., `AS18-P75-B40-T95-E90-S80-F85-CRT`) for tracking condition over time.
   - 100% self-contained HTML5 Canvas implementation with zero external CDN dependencies.

3. **Temporal Comparison Hub**:
   - Compares previous diagnostic reports side-by-side.
   - Overlays dual fingerprint radars (Baseline vs Current) to visually inspect health recovery after maintenance or detect compounding wear.
   - Computes subsystem health deltas (+/- score shifts) and odometer progression.

4. **Beginner-Friendly Pre-Mechanic Guides**:
   - **Safe DIY Checklists**: Instructions for checking motor oil, coolant reservoir, brake fluid, battery terminals, and under-car parking drips.
   - **Under-Car Fluid Color Visualizer**: Identifies oil, coolant, transmission fluid, brake fluid, and normal A/C condensation by color and texture.
   - **Mechanic Discussion Cheat Sheet**: 1-click copyable/printable questions to ask your technician to prevent overcharging.

5. **1-Click Preset Scenarios**:
   - Built-in realistic scenarios for testing: *Severe Overheating*, *Highway Speed Shudder*, *Sluggish Cold Morning Crank*, and *Sudden MPG Drop*.

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.8+
- Flask (`pip install flask`)

### Running the Application

From the project root:
```bash
python autosage/app.py
```
Or navigate into `autosage` and run:
```bash
cd autosage
python app.py
```

Then open your browser to:
```
http://127.0.0.1:5000
```

---

## 🧪 Running Automated Tests

Run the complete test suite (unit and API integration tests):
```bash
python -m unittest discover -s autosage/tests -v
```

---

## 📁 System Architecture

```
autosage/
├── app.py                     # Flask server and REST API endpoints
├── database.py                # SQLite3 database helper & history persistence
├── rule_engine.py             # Diagnostic rule engine & fingerprint calculator
├── knowledge_base.py          # Automotive symptoms catalog, combination rules & advice
├── templates/
│   └── index.html             # Single-page web application dashboard
├── static/
│   ├── css/
│   │   └── style.css          # Modern dark automotive cockpit styling
│   └── js/
│       ├── app.js             # UI state, symptom search, presets & wizard
│       └── charts.js          # Canvas radar fingerprint visualizer & gauges
└── tests/
    ├── test_engine.py         # Unit tests for rule engine & diagnostics
    └── test_api.py            # API integration tests for all REST routes
```
