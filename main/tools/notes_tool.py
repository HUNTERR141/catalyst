import json
from pathlib import Path

NOTES_FILE = Path("notes.json")

def save_note(note_content: str) -> str:
    """
    Saves a text note to a local file called notes.json.
    
    Args:
        note_content: The text content that needs to be saved.
    """
    try:
        # 1. Load existing notes
        notes = []
        if NOTES_FILE.exists():
            content = NOTES_FILE.read_text(encoding="utf-8").strip()
            if content:
                data = json.loads(content)
                notes = data.get("notes", [])

        # 2. Add the new note
        if not note_content:
            return "Error: Note content was empty."
            
        notes.append(note_content)

        # 3. Save back to file
        NOTES_FILE.write_text(
            json.dumps({"notes": notes}, indent=2, ensure_ascii=False), 
            encoding="utf-8"
        )
        
        return f"Context saved to notes: {note_content}"

    except Exception as e:
        return f"System Error saving note: {str(e)}"

def list_notes() -> str:
    """Retrieves all currently saved notes."""
    if not NOTES_FILE.exists():
        return "No notes file found."
    
    try:
        content = NOTES_FILE.read_text(encoding="utf-8").strip()
        if not content:
            return "No notes found."
        data = json.loads(content)
        notes = data.get("notes", [])
        return "\n".join(f"{i+1}. {n}" for i, n in enumerate(notes))
    except Exception:
        return "Error reading notes."