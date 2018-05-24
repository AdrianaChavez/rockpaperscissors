list = ["rock","paper","scissors"]
import random
computer_choice = (random.choice(list))
user_input = input("Let's play Rock Paper Scissors. Which do you choose? (Type 'Rock', 'Paper', or 'Scissors'")

print("Rock, paper, scissors, shoot!")

if user_input=="Rock" and computer_choice=="rock":
    print("I chose rock too. We tied.")
elif user_input=="Rock" and computer_choice=="paper":
    print("I chose paper. I win.")
elif user_input=="Rock" and computer_choice=="scissors":
    print("I chose scissors. You win.")
elif user_input=="Paper" and computer_choice=="rock":
    print("I chose rock. You win.")
elif user_input=="Paper" and computer_choice=="paper":
    print("I chose paper too. We tied.")
elif user_input=="Paper" and computer_choice=="scissors":
    print("I chose scissors. I win.")
elif user_input=="Scissors" and computer_choice=="rock":
    print("I chose rock. I win.")
elif user_input=="Scissors" and computer_choice=="paper":
    print("I chose paper. You win.")
elif user_input=="Scissors" and computer_choice=="scissors":
    print("I chose scissors too. We tied.")
else:
    print("There's been an error. Please make sure your response is valid.")
