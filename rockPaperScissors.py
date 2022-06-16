

import random
print("GAME RULES: \n"
      "ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins\n"
      "SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win\n"
      "PAPER(2) vs ROCK(1)      --> PAPER(2) wins)\n")


while True:
 userName = input("who are you ?")
 print(f"Hello welcome{userName} ")
computerChoice = random.randint(1,3)
   while True:

        userChoice = input("choose your Choice Rock(1),Paper(2),scissors(3)")

    #validating User
    while userChoice != "1" and userChoice !="2" and userChoice != "3":
        print("Invalid Choice")
        userChoice = input("Choose your choice Rock(1),Paper(2),Scissors(3)")

    else:

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
        elif userChoice== 3and ComputerChoice == 3:
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
