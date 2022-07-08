from defQuestionAnswers import QuestionAnswers
from defQuestionAnswers import QuestionAnswerList
from NicknameChoosingFile import Nickname

# after chaos in the group chat, the explanation

input()
print("02.49 PM - Lotte: Hey guys, I made this group chat because I felt like we were all pretty interested in the"
      " deaths at the haunted library ")
print("and thought it'd be nice to be able to discuss some things in here")
input()
print("02.50 PM - Lex: OMG HI LOTTE")
input()
print("02.50 PM - Lex: Finally somebody I know")
input()
print("02.50 PM - Cas: Uhm okay, yeah I am actually pretty interested in the case")
input()
print("02.50 PM - Lex: Wait, where you here the whole time?? 0-0")
input()
print("02.51 PM - Bella: Lex, maybe you should calm down a bit")
input()
print("02.51 PM - Cas: I'm Cas, and you're Lex I suppose")
input()
print("02.51 PM - Lex: Yep, I am indeed, and this is my new bestie", Nickname)
input()
print("~ Select: a) 'Okay, all chaos aside, Lotte, what do you specifically want to discuss?' ~")
print("~ Select: b) 'Omg Lex, WHY?? -_-' ~")

Answer = QuestionAnswers("~ Type 'a' or 'b' please ~", QuestionAnswerList)
if Answer == 'a':
    input()
    print("02.51 PM - You: Okay, all chaos aside, Lotte, what do you specifically want to discuss?")
    import Choice3a

else:  # b
    input()
    print("02.51 PM - You: Omg Lex, WHY?? -_-")
    import Choice3b
