from google.adk.runners import Runner
from main.agents.orchestrator_agent import orchestrator
from google.adk.sessions import InMemorySessionService
from google.adk.memory import InMemoryMemoryService
from main.agents.planner_agent import planner_tool
from main.agents.tutor_agent import tutor_tool      
from main.agents.quiz_agent import quiz_tool
from main.agents.evaluator_agent import evaluator_tool
from main.tools.notes_tool import save_note, list_notes     
from google.adk.tools import load_memory_tool

# Instantiate the orchestrator agent with session memory
root_agent = orchestrator()
runner = Runner(
        agent=root_agent,
        name="orchestrator_runner",
        model="gemini-2.5-flash",
        memory_service=InMemoryMemoryService(),
        session_service=InMemorySessionService(),
        tools=[
            planner_tool,
            tutor_tool,
            quiz_tool,
            evaluator_tool,
            save_note,
            list_notes,
            load_memory_tool, 
        ]
    )

if __name__ == "__main__":
    runner.run()