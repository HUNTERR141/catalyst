from google.adk.runners import Runner
from main.agents.orchestrator_agent import orchestrator
from google.adk.sessions import InMemorySessionService
from google.adk.memory import InMemoryMemoryService
from google.adk.tools import load_memory_tool

# Instantiate the orchestrator agent with session memory
root_agent = orchestrator()
runner = Runner(
        agent=root_agent,   
        app_name="Catalyst AI Study Tutor", 
        memory_service=InMemoryMemoryService(),
        session_service=InMemorySessionService(),
    )

if __name__ == "__main__":
    runner.run()