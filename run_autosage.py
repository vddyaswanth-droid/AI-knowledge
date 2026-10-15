"""
AutoSage Launcher Script
Run this script to start the AutoSage Car Health Analysis System.
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUTOSAGE_DIR = os.path.join(BASE_DIR, "autosage")

if AUTOSAGE_DIR not in sys.path:
    sys.path.insert(0, AUTOSAGE_DIR)

from app import app

if __name__ == "__main__":
    print("=" * 60)
    print("  AutoSage - Beginner-Friendly Car Health Analysis System")
    print("  Open your browser and navigate to: http://127.0.0.1:5000")
    print("=" * 60)
    app.run(host="127.0.0.1", port=5000, debug=True)
