from random import *

answers = ['Definitely', 'I think yes', 'Unclear yet, try again', "Don't even think about it",
           "It's a foregone conclusion", 'Most likely', 'Ask later', 'My answer is no', 'No doubt',
           'Good prospects', 'Better not tell', 'According to my knowledge - no', 'Definitely yes',
           'Signs say yes', 'Now it is impossible to predict', 'Prospects are not very good',
           'You can be sure of it', 'Yes', 'Concentrate and ask again', 'Very doubtful']

print("Hello world! I'm magic ball and i know answer on any question.")
name = input("Please, enter your name: ")
print(f"Hello {name}!")
while True:
    question = input(f"{name} ask your question or enter q to exit: ")
    if question == "q":
        print(f"Bye {name}. Comeback if u have a question!")
        break
    print(f"Answer is: {choice(answers)}")
