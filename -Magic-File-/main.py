# def for making decisions
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

# game introductions
#   introduction game


print("Welcome by Down to Downhill")
print()
print("This is an interactive text story game.")
print("Your choices will have impact on the storyline and the ending")
print("Choose wisely")
print()
#   introduction how to play
print("If the game stops running click enter to continue")
input()
print("If the game asks a question, please answer the question on the same line as the question.")
print("The code will see your enter as the answer if you first click enter and then fill in your answer.")
print()
print("For example:")
Example = input("What is your favorite color?")
print("Your favorite color is", Example)
input()


print("Now that you know how to play, lets start this game!")
input()

import cv2

img_0 = cv2.imread("Startscreen.jpg")
cv2.imshow('Image', img_0)
cv2.waitKey(0)

# begin story
print("~ On Snappic you come across an app for chatting with people about crimes. You decide to download it. ~ ")

# introduction

print()
print("11.00 AM - Unknown: Hey, you're new here I saw!")
input()
print("11,00 AM - Unknown: I would love to be your friend. What is your name?")
print("~ please fill in your name ~")
# choosing player name
NamePlayer = str(input())
str(input())
print(f"Are you sure you want to continue with {NamePlayer}, as player name?")
Question1 = str(input("Type 'yes' if you want to continue, type 'no', if you want to pick a new name."))
str(input())
# if wrong player name, selecting a new one
while Question1 != 'yes':
    while Question1 != 'no' and Question1 != 'yes':
        print("Please type 'yes' or 'no'")
        Question1 = str(input("Type 'yes' if you want to continue, type 'no', if you want to pick a new name."))
        str(input())
    while Question1 == 'no':
        print('Okay, please select a new name:')
        NamePlayer = str(input())
        str(input())
        print(f'Do you want to continue with {NamePlayer} as your name?')
        Question1 = str(input("Type 'yes' if you want to continue, type 'no', if you want to pick a new name."))
        str(input())
else:
    print('')
    print(f"11.05 AM - You: Hi, my name is {NamePlayer} :)")
    input()
    print(f"11.06 AM - Unknown: Its so nice to meet you, {NamePlayer}")
    input()
    print("11.06 AM - Unknown: Im sure we'll be best friends in no time! :)")
    input()
    print("11.06 AM - Lotte: Im Charlotte, but just call me Lotte for short.")
    input()
    print("...")
    input()
    print("~ Later that day.. ~")
    # start story, the talks in town
    input()
    print("02.30 PM - Lotte: Have you heard about the rumor that goes around in town?")
    input()
    print("02.30 PM - You: No?")
    input()
    print("02.30 PM - Lotte: Some kids went to the haunted library last weekend...")
    input()
    print("02.31 PM - Lotte: They were found dead this morning, crushed under bookcases")

    # first choice starts here
    input()
    print("~ It's time to make your first choice.")
    input()
    print("~ How will you respond to this text? ~")
    input()
    print("Select: a)'What?? Dead?! How old were they?? D:'")
    print("Select: b)'Oh no, that's horrible, how did a whole bookcase fall on them?'")

    
    Answer = QuestionAnswers("~ Type 'a' or 'b' please ~", QuestionAnswerList)
    if Answer == 'a':
        input()
        print("02.31 PM - You: What?? Dead?! How old were they?? D:")
        import Choice1a

    else:  # b
        input()
        print("2.31 PM - You: Oh no, that's horrible, how did a whole bookcase fall on them?")
        import Choice1b