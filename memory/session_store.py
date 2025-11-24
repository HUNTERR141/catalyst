import json
from pathlib import Path
from typing import List

NOTES_FILE = Path("notes.json")

def load_notes_from_disk(path: Path = NOTES_FILE) -> List[str]:
    """
    Load notes from disk into memory.
    """
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data.get("notes", [])
    except Exception:
        return []

def save_notes_to_disk(notes: List[str] = None, path: Path = NOTES_FILE) -> None:
    """
    Persist notes to disk.
    """
    if notes is None:
        # load from global notes tool state
        notes = []
    data = {"notes": notes}
    try:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception:
        pass