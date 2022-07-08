from defQuestionAnswers import QuestionAnswers
from defQuestionAnswers import QuestionAnswerList

# ~ You go towards the noise ~

input()
print("~ You walk between the large bookshelves to the far back of the library ~")
input()
print("~ In the back of the library is almost no light, very careful you put one foot in front of the other ~")
input()
print("~ You finally arrive at the shelve where the noise seems to be coming from, a soft shuffling noise, as if "
      "somebody is pacing back and forth behind this bookcase")
input()

print("~ Select: a) Walk behind the bookcase ~")
print("~ Select: b) Carefully look around the corner ~")

Answer = QuestionAnswers("~ Type 'a' or 'b' please ~", QuestionAnswerList)
if Answer == 'a':
    input()
    print("~ You walk behind the bookcase ~")
    import Choice9aENDING3

else:  # b
    input()
    print("~ You carefully look behind the bookcase ~")
    import Choice9bENDING4

