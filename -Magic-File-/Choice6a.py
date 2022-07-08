from defQuestionAnswers import QuestionAnswers
from defQuestionAnswers import QuestionAnswerList
from NicknameChoosingFile import Nickname

# 09.47 AM - You: I could go, since I live close

input()
print("09.47 AM - Lex:", Nickname, "are you gonna go to a haunted library by yourself??" )
input()
print("09.48 AM - You: Yeah, I don't have anything to do tonight and I basically live next to the library, so it "
      " works out perfectly, I mean, what's the worst that could happen")
input()
print("09.48 AM - Bella: Are you sure with going to that creepy place by yourself, YESTERDAY there were two bodies")
input()
print("09.48 AM - You: Guys, relax, if the police hasn't closed the building with fences, I'm sure it'll be okay")
input()
print("~ You close your phone, because you don't want to get too scared to go and be laughed at ~")
input()
print("~ The whole day you are unnerved and jump from every little sound in the house ~")
input()
print("~ Okay, maybe this is a bit scarier then you thought first, but you stick with your first argument: it can't be"
      " thát bad if the police hasn't closed of the library ~")
input()
print("~ At 8.30 PM you decide it's time to finally go to the library, you pick up your phone and walk out the front "
      " door ~")
input()
print("~ You walk down the street until you're in front of the large building where your parents would always take you"
      "as a child ~")
input()
print("~ You open the doors and go inside ~")
input()
print("~ Before you go in further you remember to grab your phone and sent a quick message to the group chat")
input()
print("8.37 PM - You: Going in now, wish me luck")
input()
print("~ At first you don't notice anything off, it's a lot older then before, and the bookcases do look very old")
input()
print("~ Then all off a sudden you hear the sound of something falling in the back of the library")
input()
print("~ A mouse maybe? ~")
input()

print("~ Select: a) Go towards the noise ~")
print("~ Select: b) Leave the library ~")

Answer = QuestionAnswers("~ Type 'a' or 'b' please ~", QuestionAnswerList)
if Answer == 'a':
    input()
    print("~ You go towards the noise ~")
    import Choice7a

else:  # b
    input()
    print("~ You leave the library ~")
    import Choice7bENDING1
