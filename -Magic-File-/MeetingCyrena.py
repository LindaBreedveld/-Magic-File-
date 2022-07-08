from defQuestionAnswers import QuestionAnswers
from defQuestionAnswers import QuestionAnswerList
from NicknameChoosingFile import Nickname


# The next morning - Cyrena has been added to the group

input()
print("~ The next morning you awake to the buzzing of your phone ~")
input()
print("~ You reach your hand out to your phone and try to stop you alarm ~")
input()
print("~ After awhile of struggling and the alarm not stopping you decide to grab your phone and see what's wrong with"
      "it ~")
input()
print("09.30 AM - Notification: Lotte added Cyrena to 'The mystery of DH'")
input()
print("09.30 AM - Lotte: Hey everybody, I found another person who's interested in these new murders, so I asked"
      " her to join")
print("09.30 AM - Lotte: This is Cyrena")
print("09.31 AM - Cyrena: Hey everybody")
print("09.31 AM - Lex: OH WOW MORE PEOPLE, Hello Cyrena, Im Lex")
print("09.31 AM - Cyreana: Oh hello Lex")
print("09.32 AM - Bella: I would look out with talking to them Cyrena, or you'll get a weird nickname in no-time")
print("09.32 AM - Cyrena: If I wouldn't wanna talk to him, I wouldn't, so you really don't have to look out for me")
input()
print("09.33 AM - You: Oh come on guys, I was trying to sleep, did I really have to wake up at 09.30 on my free day")
input()
print("09.33 AM - Lex: Oh good morning to you too", Nickname, "you really are always a lot of fun when you just come"
                                                             "online, aren't you?")
input()
print("09.34 AM - Cas: Good morning everyone :)")
input()
print("09.34 AM - Cas: I've been looking into the DK case again after our conversation from yesterday again")
input()
print("09.35 AM - Lex: Oeehh, more storytime with Cas, tell me everything")
input()
print("09.35 AM - Cas: I found some stories about one of children that died and one of the women")
input()
print("09.35 AM - Cas: They died together")

print("~ Select: a) 'Why was the woman murdered??' ~")
print("~ Select: b) 'Why was the child murdered?!' ~")

Answer = QuestionAnswers("~ Type 'a' or 'b' please ~", QuestionAnswerList)
if Answer == 'a':
    input()
    print("09.36 AM - You: Why was the woman murdered??")
    import Choice5a

else:  # b
    input()
    print("09.36 AM - You: Why was the child murdered?!")
    import Choice5b
