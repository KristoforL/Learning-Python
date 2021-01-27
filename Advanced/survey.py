class AnnonymousSurvey:
    """Collect annonymous answeres to a survey questions."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_questions(self):
        """Show the survey questions"""
        print(self.question)

    def store_responses(self, new_response):
        """Stores the responses in the list"""
        self.responses.append(new_response)

    def show_results(self):
        """Show the responses from the people who took the survey"""
        for response in self.responses:
            print(f"- {response}")