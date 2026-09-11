from pathlib import Path

# Main Window attributes
MW_TITLE = "Reflect Log-In"
MW_HEIGHT = 500
MW_WIDTH = 400

# Reflection timer buttons
REFLECTION_TIMERS = [
    ("1m", 1),
    ("5m", 5),
    ("10m", 10),
    ("15m", 15),
]

# Questions
FOCUSED_QUESTION = "Are you being productive right now?"
DOING_QUESTION = "What are you about to do?"
DOING_PLACEHOLDER = "Apply to jobs / Write an email"
KNOW_NEXT_STEP_QUESTION = "Do you know what your next step is?"

# File paths
PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
REFLECTION_ENTRIES_FILE = DATA_DIR / "reflection_entries.json"

# IMPORTANT:
#    APP_DIR: absolute path to reflect-log-in
#             example: APP_DIR = "/home/you/projects/reflect-log-in"
#
#    VENV_PYTHON: absolute path to python inside the .venv/bin
#                 example: VENV_PYTHON = "/home/you/projects/reflect-log-in/.venv/bin/python"

APP_DIR = "/home/your-user/reflect-log-in"
VENV_PYTHON = "/home/your-user/reflect-log-in/.venv/bin/python"