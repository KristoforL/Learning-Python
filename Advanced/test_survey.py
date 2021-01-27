import unittest

from survey import AnnonymousSurvey

class TestAnnonymousSurvey(unittest.TestCase):
    """Test for the class AnnonymousSurvey"""

    def setUp(self):
        """Create a survey and a set of responses for uuse in all test methods"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']



    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        self.my_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test to see that multiple reponses can be stored"""
        for response in self.responses:
            self.my_survey.store_responses(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()
