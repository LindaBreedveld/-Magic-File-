from defQuestionAnswers import QuestionAnswers
from defQuestionAnswers import QuestionAnswerList
from NicknameChoosingFile import Nickname

# 09.36 AM - You: Who lives close to there and wants to investigate??

print("09.36 AM - Lex: I live kinda close... I could do it if you want me to")
input()
print("09.37 AM - Bella: What happened to you never wanting to go to a library ever again? xD")
input()
print("09.37 AM - Lex: I'm sorry Bella but", Nickname, "needs me, so of course I'll go ;)")
input()
print("09.38 AM - You: You're amazing Lex!!")
input()
print("09.38 AM - Lex: I'll be going tonight then, wish me luck >:D")
input()
print("~ You decide to put off your phone for the time being ~")
input()
print("8.29 PM - Lex: You guys I'm going now!!")
input()
print("~ You begin to get a bad feeling about letting Lex go to the library alone ~")

print("~ Select: a) Go join them at the library ~")
print("~ Select: b) Stay at home ~")

Answer = QuestionAnswers("~ Type 'a' or 'b' please ~", QuestionAnswerList)
if Answer == 'a':
    input()
    print("~ You decide to also go to the library ~")
    import Choice8a

else:  # b
    input()
    print("~ You decide to stay at home ~")
    import Choice8bENDING2