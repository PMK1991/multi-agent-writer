class ContentTaskFactory:
    def __init__(self, content_team):
        self.content_team = content_team

    def create_planning_task(self, inputs):
        topic = inputs["topic"]
        return {
            "description": (
                f"1. Prioritize the latest trends, key players, "
                f"and noteworthy news on {topic}.\n"
                "2. Identify the target audience, considering "
                "their interests and pain points.\n"
                "3. Develop a detailed content outline including "
                "an introduction, key points, and a call to action.\n"
                "4. Include SEO keywords and relevant data or sources."
            ),
            "expected_output": "A comprehensive content plan document "
                               "with an outline, audience analysis, "
                               "SEO keywords, and resources.",
            "agent": self.content_team.create_planner(),
        }

    def create_writing_task(self, inputs):
        topic = inputs["topic"]
        return {
            "description": (
                f"1. Use the content plan to craft a compelling "
                f"blog post on {topic}.\n"
                "2. Incorporate SEO keywords naturally.\n"
                "3. Sections/Subtitles are properly named "
                "in an engaging manner.\n"
                "4. Ensure the post is structured with an "
                "engaging introduction, insightful body, "
                "and a summarizing conclusion.\n"
                "5. Proofread for grammatical errors and "
                "alignment with the brand's voice.\n"
            ),
            "expected_output": "A well-written blog post "
                               "in markdown format, ready for publication, "
                               "each section should have 2 or 3 paragraphs.",
            "agent": self.content_team.create_writer(),
        }

    def create_editing_task(self, inputs):
        return {
            "description": "Proofread the given blog post for "
                           "grammatical errors and "
                           "alignment with the brand's voice.",
            "expected_output": "A well-written blog post in markdown format, "
                               "ready for publication, "
                               "each section should have 2 or 3 paragraphs.",
            "agent": self.content_team.create_editor()
        }