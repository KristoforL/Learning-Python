from survey import AnnonymousSurvey

#Define a question, and make a survey
question = "What language did you learn first?"
my_survey = AnnonymousSurvey(question)

#Show the question and store response to the question
my_survey.show_questions()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    else:
        my_survey.store_responses(response)

#Show rhe survey results
print("\nThank you to everyone who participated in the survey")
my_survey.show_results()







