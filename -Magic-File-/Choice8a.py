from defQuestionAnswers import QuestionAnswers
from defQuestionAnswers import QuestionAnswerList

# ~ You decide to also go to the library ~

input()
print("~ At 8.30 PM you decide to join Lex in the library")
input()
print("~ You walk down the street until you're in front of the large building where your parents would always take you"
      "as a child ~")
input()
print("~ You open the doors and go inside ~")
input()
print("~ Before you go in further you remember to grab your phone and sent a quick message to the group chat")
input()
print("8.37 PM - You: I'm gonna join Lex in the investigation")
input()
print("~ At first you don't notice anything off, it's a lot older then before, and the bookcases do look very old")
input()
print("~ Then all off a sudden you hear the sound of something falling in the back of the library")
input()
print("~ Could it be Lex? ~")
input()

print("~ Select: a) Yell Lex towards the noise ~")
print("~ Select: b) Go quietly to the place you heard the noise ~")

Answer = QuestionAnswers("~ Type 'a' or 'b' please ~", QuestionAnswerList)
if Answer == 'a':
    input()
    print("~ You yell Lex towards the noise ~")
    import Choice10ENDING5

else:  # b
    input()
    print("~ You go quietly to the place you heard the noise ~")
    import Choice7a