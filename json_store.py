import json
from pathlib import Path
from config import REFLECTION_ENTRIES_FILE


class JSONStore:
    """
    Class to store entries to one JSON file.
    """
    def __init__(self, path=REFLECTION_ENTRIES_FILE):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

        if not self.path.exists():
            self._write([])

    def _read(self):
        with self.path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def _write(self, data):
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def insert_entry(self, entry):
        data = self._read()
        data.append(entry.to_dict())
        self._write(data)

        return entry

    def get_all(self):
        return self._read()