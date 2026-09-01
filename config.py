from pathlib import Path

# Main Window attributes
MW_TITLE = "Reflect Log-In"
MW_HEIGHT = 500
MW_WIDTH = 400

# Questions
FOCUSED_QUESTION = "Are you being productive right now?"
DOING_QUESTION = "What are you about to do?"
DOING_PLACEHOLDER = "Apply to jobs / Write an email"
KNOW_NEXT_STEP_QUESTION = "Do you know what your next step is?"

# File paths
# Project root (directory containing config.py)
PROJECT_ROOT = Path(__file__).resolve().parent

DATA_DIR = PROJECT_ROOT / "data"

REFLECTION_ENTRIES_FILE = DATA_DIR / "reflection_entries.json"