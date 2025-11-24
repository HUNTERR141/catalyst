from typing import List
import json
from pathlib import Path

NOTES_FILE = Path("notes.json")

class NotesTool:
    """
    Tool to save and retrieve notes. Notes persist to notes.json
    across sessions.
    """

    def __init__(self, persist_to_file: bool = True):
        self.__name__ = "save_note"
        self.name = "save_note"
        self.description = "Save and retrieve user notes."
        self._notes: List[str] = []
        self._persist = persist_to_file

        # load persisted notes from disk
        if self._persist:
            self._load_from_disk()

    def _load_from_disk(self):
        """Load notes from JSON file."""
        if NOTES_FILE.exists():
            try:
                data = json.loads(NOTES_FILE.read_text(encoding="utf-8"))
                self._notes = data.get("notes", [])
            except Exception:
                pass

    def _save_to_disk(self):
        """Save notes to JSON file."""
        try:
            data = {"notes": self._notes}
            NOTES_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception:
            pass

    def save(self, note: str) -> str:
        note = (note or "").strip()
        if not note:
            return "No note provided."
        self._notes.append(note)
        if self._persist:
            self._save_to_disk()
        return f"Saved note: {note}"

    def list_notes(self) -> str:
        notes = list(self._notes)
        if not notes:
            return "No notes saved."
        return "\n".join(f"{i+1}. {n}" for i, n in enumerate(notes))

    def __call__(self, command_or_note: str) -> str:
        """
        Interface:
         - 'list' / 'get' / 'show' -> returns saved notes
         - 'save: <text>' -> saves note
         - plain text -> saves note
        """
        if not isinstance(command_or_note, str):
            return "Invalid input."

        cmd = command_or_note.strip()
        lower = cmd.lower()
        if lower in ("list", "get", "show", "show notes", "list notes"):
            return self.list_notes()
        if lower.startswith("save:"):
            return self.save(cmd.split(":", 1)[1].strip())
        # default: treat as note text to save
        return self.save(cmd)
