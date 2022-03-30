import random

options = ['rock', 'paper', 'scissors']
while True:
    machine = random.choice(options)

    player = input("\nChoose one between rock, paper and scissors. ")
    if player == 'q':
        break
    if player in options:
        print(f"\nYou choose {player}.")
        print(f"The machine choose {machine}.")
        print("...")

        if player == 'rock' and machine == 'paper':
            print("You lost!")
        elif player == 'rock' and machine == 'scissors':
            print("You won!")
        elif player == 'paper' and machine == 'scissors':
            print("You lost!")
        elif player == 'paper' and machine == 'rock':
            print("You won!")
        elif player == 'scissors' and machine == 'rock':
            print("You lost!")
        elif player == 'scissors' and machine == 'paper':
            print("You won!")
        elif player == machine:
            print("That was a tie!")
    else:
        print("Plese enter a valid awnser.")