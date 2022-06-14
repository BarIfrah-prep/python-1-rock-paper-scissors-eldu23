# Rock Paper Scissors
# A code file structure:
# A line that starts with "#"  is a comment line (it will not be interpreted)
"""
If you want to comment multiple lines, start and finish with three (3) double quotes (")
As you can see, this line is also a comment.

"""
"""
I am a comment


"""
# ----------------------------------------------------------------------------------------------------------------------
# Here you include all of your package imports (like random and time packages we've discussed about)
# ----------------------------------------------------------------------------------------------------------------------
import random

# ----------------------------------------------------------------------------------------------------------------------
# Here you will write all of the functions (for later stages of the course
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Here you write code :)
# ----------------------------------------------------------------------------------------------------------------------
"""
I'll give you the text inputs for this program, to make your lives a little easier.
In addition, and to make it simple to you, the input from the user will be an integer:
1 for ROCK
2 for PAPER
3 for SCISSORS
A text input describing the operation is unacceptable and will cost you with points.

A quick reminder of the rules:

ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins
SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win
PAPER(2) vs ROCK(1)      --> PAPER(2) wins

DO NOT ADD EXTRA OPTIONS (No lizard, no Spock.)
"""

# print the instructions for the user to see:
print("GAME RULES: \n"
      "ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins\n"
      "SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win\n"
      "PAPER(2) vs ROCK(1)      --> PAPER(2) wins)\n")

# The game will run in a WHILE loop.
# The loop is infinite, and only the user has the power to stop it (when they say they don't want to play anymore)
while True:
    """
      This is the game's heart. You'll need to think and use everything we've learned so far to make this game work.
      Remember Python's rules ( the ':' after a statement, the indentation with loops and statements..)
      
      """
    pass

import Random

#Here you write the code

gameIson = True

#printing message to the player

userName = input("who are you ?")
print(f"Hello welcome{userName}")

while gameIson:
    userChoice = input("choose your Choice Rock(1),Paper(2),scissors(3)")

    #validating User
    while userChoice != "1" and userChoice !="2" and userChoice != "3":
        print("Invalid Choice")
        userChoice = input("Choose your choice Rock(1),Paper(2),Scissors(3)")

    else:
        computerChoice = random.randint(1,3)
        userChoice =int(userChoice)

        # Case User Choose Rock
        if userChoice == 1 and computerChoice == 3:
            print("congra you won")
        elif userChoice ==1 and computerChoice == 2:
            print("oops you lose")
        elif userChoice == 1 and computerChoice == 1:
            print("its amazing!")

        #case user choose paper
        if userChoice == 2 and computerChoice == 1:
            print("congra you won")
        elif userChoice == 2 and computerChoice == 3:
            print("oops you lose")
        elif userChoice == 2 and computerChoice == 2:
            print("its amazing!")

            #case user choose scissors

        if userChoice == 3 and computerChoice == 2:
            print("congra you won")
        elif userChoice == 3and computerChoice == 1:
            print("oops you lose")
        elif userChoice== 3and computerChoice == 3:
            print("its amazing!")

     #asking the user if he wants to continue

    answerRequest = input("you want to continue? y/n")

    while answerRequest !="y" and answerRequest != "n":
        print("Invalid Answer!")
        answerRequest = input("wanna continue ? y/n")

    if answerRequest.lower() == "y":
        continue
    elif answerRequest.lower() == "n":
        print("Thanks  for playing the game!")
        gameIson = False
