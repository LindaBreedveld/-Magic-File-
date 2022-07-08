from defQuestionAnswers import QuestionAnswers
from defQuestionAnswers import QuestionAnswerList

Answer = QuestionAnswers("~ Type 'a' or 'b' please ~", QuestionAnswerList)
if Answer == 'a':
    input()
    print("~ You go and grab a cookie ~")
    Nickname = 'Chocolate Chip'
    import Choice2a

else:  # b
    input()
    print("~ You decide to listen to some music ~")
    Nickname = 'Songbird'
    import Choice2b
