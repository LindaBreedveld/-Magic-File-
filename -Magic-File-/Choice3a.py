from defQuestionAnswers import QuestionAnswers
from defQuestionAnswers import QuestionAnswerList

# 02.51 PM - You: Okay, all chaos aside, Lotte, what do you specifically want to discuss?

input()
print("02.52 PM - Lotte: There really isn't anything I 'specifically' wanted to discuss")
input()
print("02.52 PM - Lotte: I just thought that it would be nice to be able to talk about these strange killings with"
      " some other interested people")
input()
print("02.52 PM - Cas: Kills? As in the DK case??")
input()
print("02.53 PM - Bella: It is indeed pretty similar if you say it like that")
input()
print("02.53 PM - Lex: Guys, sorry for my language but WHAT THE FREAK are we talking about")
input()
print("02.53 PM - You: Yeah, I also have no idea what we're talking about")
input()
print("02.54 PM - Lotte: The Downhill Killer, aka DK, killed people 5 years ago here in Downhill")
input()
print("02.54 PM - Cas: Yes, the people got buried under bookcases in the old library")
input()
print("02.54 PM - Lex: JUST LIKE WHAT HAPPENED TO THOSE CHILDREN THIS MORNING")
input()
print("02.55 PM - You: Why would somebody pretend to be DK though?")
input()
print("02.55 PM - Bella: I actually don't think they ever arrested DK")
input()
print("02.55 PM - Cas: Nope, you're right, it could just be DK who found a reason to start killing again")
input()
print("02.56 PM - Bella: I get the shivers when thinking about how that serial killer is just roaming around free")
input()
print("02.56 PM - You: It's a serial killer? That means 3 or more deaths right?")
input()
print("02.56 PM - Lotte: Five people were killed in total")
input()
print("02.57 PM - Bella: Yeah, I remember two of them were kids right?")
input()
print("02.57 PM - Lex: WHAT?? They killed even more children?? That's monstrous")
input()
print("02.57 PM - Cas: We don't know if the new kills were from the DK")
input()
print("02.58 PM - Lotte: No, but I agree that it's pretty suspicious that these kills are so similar")
input()
print("02.58 PM - You: But who were the other victims apart from the DK")
input()
print("02.58 PM - Lotte: Two women and an elderly men")
input()

print("~ Select: a) 'Why were those women murdered??' ~")
print("~ Select: b) 'Those children are still the ones that blow my mind the most. Why would you murder a child?!?' ~")

Answer = QuestionAnswers("~ Type 'a' or 'b' please ~", QuestionAnswerList)
if Answer == 'a':
    input()
    print("02.59 PM - You: Why were those women murdered??")
    import Choice4a

else:  # b
    input()
    print("02.59 PM - You: Those children are still the ones that blow my mind the most. Why would you murder a "
          "child?!?")
    import Choice4b
