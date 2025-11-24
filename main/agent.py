from agents.orchestrator_agent import orchestrator
from memory.session_store import load_notes_from_disk, save_notes_to_disk
import atexit


# build the root/orchestrator agent
root_agent = orchestrator()

# ensure notes are saved on exit
atexit.register(save_notes_to_disk)
