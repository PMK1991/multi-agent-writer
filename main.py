from crewai import Crew
from agents import ContentTeam
from tasks import ContentTaskFactory

# Step 1: Instantiate ContentTeam once
content_team = ContentTeam()

# Step 2: Pass the ContentTeam instance to ContentTaskFactory
task_factory = ContentTaskFactory(content_team)

# Define inputs for the tasks
#inputs = {"topic": "Comparative study of LangGraph, Autogen and Crewai for building multi-agent system."}
inputs = {"topic": "What is the difference between Shakuntala from Kalidasa and Shakuntala from Mahabharata?"}
# Step 3: Use the same ContentTeam instance to create agents
planner = content_team.create_planner()
writer = content_team.create_writer()
editor = content_team.create_editor()

# Step 4: Create tasks by calling methods on the Conten  tTaskFactory instance
plan = task_factory.create_planning_task(inputs)
write = task_factory.create_writing_task(inputs)
edit = task_factory.create_editing_task(inputs)

# Instantiate Crew with agents and tasks
crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=2
)

# Kickoff the crew with inputs
result = crew.kickoff(inputs=inputs)
