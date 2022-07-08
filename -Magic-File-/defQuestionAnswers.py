QuestionAnswerList = ['a', 'b']

def QuestionAnswers(Question, Choices):
    AnswerQuestion = False
    while not AnswerQuestion:
        Answer = input(Question)
        if Answer in Choices:
            AnswerQuestion = True
        else:
            print("~ Please select one of the options ~")
    return Answer