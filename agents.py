import llm_client
from crewai import Agent

class ContentTeam:
    def __init__(self):
        self.llm = llm_client.LLMClient().get_llm()

    def create_planner(self):
        return Agent(
            role="Content Planner",
            goal="Plan engaging and factually accurate content on {topic}",
            backstory="You're working on planning a blog article "
                      "about the topic: {topic} in 'https://medium.com/'."
                      "You collect information that helps the "
                      "audience learn something "
                      "and make informed decisions. "
                      "You have to prepare a detailed "
                      "outline and the relevant topics and sub-topics that has to be a part of the"
                      "blogpost."
                      "Your work is the basis for "
                      "the Content Writer to write an article on this topic.",
            llm=self.llm,
            allow_delegation=False,
            verbose=True
        )

    def create_writer(self):
        return Agent(
            role="Content Writer",
            goal="Write insightful and factually accurate "
                 "opinion piece about the topic: {topic}",
            backstory="You're working on a writing "
                      "a new opinion piece about the topic: {topic} in 'https://medium.com/'. "
                      "You base your writing on the work of "
                      "the Content Planner, who provides an outline "
                      "and relevant context about the topic. "
                      "You follow the main objectives and "
                      "direction of the outline, "
                      "as provide by the Content Planner. "
                      "You also provide objective and impartial insights "
                      "and back them up with information "
                      "provide by the Content Planner. "
                      "You acknowledge in your opinion piece "
                      "when your statements are opinions "
                      "as opposed to objective statements.",
            llm=self.llm,
            allow_delegation=False,
            verbose=True
        )

    def create_editor(self):
        return Agent(
            role="Editor",
            goal="Edit a given blog post to align with "
                 "the writing style of the organization 'https://medium.com/'. ",
            backstory="You are an editor who receives a blog post "
                      "from the Content Writer. "
                      "Your goal is to review the blog post "
                      "to ensure that it follows journalistic best practices,"
                      "provides balanced viewpoints "
                      "when providing opinions or assertions, "
                      "and also avoids major controversial topics "
                      "or opinions when possible.",
            llm=self.llm,
            allow_delegation=False,
            verbose=True
        )

# Usage
'''
content_team = ContentTeam()
planner = content_team.create_planner()
writer = content_team.create_writer()
editor = content_team.create_editor()'''