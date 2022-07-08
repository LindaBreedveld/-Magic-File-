from defQuestionAnswers import QuestionAnswers
from defQuestionAnswers import QuestionAnswerList

# 09.39 AM - Lotte: Okay guys, let's keep it fun in here, shall we? - Story about pastor

input()
print("09.39 AM - Lex: Okay, all these stories are fun, but wasn't there also an elderly man?? Why is nobody talking"
      "about that guy")
input()
print("09.40 AM - Cas: Yeah, you're right, the elderly man was the former pastor of this town")
input()
print("09.40 AM - Bella: I've heard he sexually assaulted people, this only came out after he was dead, so it's "
      "never been confirmed")
input()
print("09.41 AM - Cyrena: He deserved to die, I don't even blame the killer for killing that man")
input()
print("09.41 AM - Lex: WOOOWW Cyrena, isn't that a bit too harsh")
input()
print("09.41 AM - Lex: For ones I actually don't wanna argue, he is a really bad person, but nobody should get "
      "harshly murdered by a serial killer")
input()
print("09.42 AM - Lotte: I do say I have to agree with Cyrena here, sucha disgusting pig shouldn't be walking around"
      "on this earth")
input()
print("09.42 AM - Bella: Guys, guys, let's calm down a bit first")
input()
print("09.42 AM - Cyrena: I have lived with that man under the same roof for 12 years of my life, I have the right"
      "to call him out for how horrible he was")
input()
print("09.43 AM - Lex: YOU ARE THE DAUGHTER OF THE PASTOR???")
input()
print("09.43 AM - Lex: I have heard SO much stuff about you")
input()
print("09.43 AM - Cyrena: Oh god, you're one of THEM")
input()
print("09.44 AM - Lex: One of who???")
input()
print("09.44 AM - Cyrena: One of those bitches that only think I'm 'the daughter of the pastor' instead of an "
      " actual human being of myself")
input()
print("09.45 AM - Bella: Okaayyy, let's not fight everybody")
input()
print("09.45 AM - Cyrena: Omg, please stop trying to be goody-tho-shoes")
input()
print("09.46 AM - Cas: Maybe we should investigate the crime scene itself to find some more answers")
input()

print("~ Select: a) 'I could go, since I live close' ~")
print("~ Select: b) 'Who lives close to there and wants to investigate??' ~")

Answer = QuestionAnswers("~ Type 'a' or 'b' please ~", QuestionAnswerList)
if Answer == 'a':
    input()
    print("09.47 AM - You: I could go, since I live close")
    import Choice6a

else:  # b
    input()
    print("09.36 AM - You: Who lives close to there and wants to investigate??")
    import Choice6b