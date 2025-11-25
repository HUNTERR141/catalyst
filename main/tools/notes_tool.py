from google.adk.tools import BaseTool

class NotesTool(BaseTool):
    def __init__(self):
        super().__init__(
    name = "notes_tool",
    description = "Store and retrieve user notes.",
    )
        
    def __call__(self, note: str):
        with open("notes.txt", "a") as f:
            f.write(note + "\n")
        return f"Saved note: {note}"
