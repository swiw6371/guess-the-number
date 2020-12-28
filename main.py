import random
number = random.randint(2,99)
level_selected=False
attempt_initial=0

def playGame(attempt_initial):
 attempt=attempt_initial
 game_finished=False
 while not game_finished:
  if attempt==0:
     game_finished=True
     print(f"You lost! Number is:{number}")
  else:
    guess=int(input("Guess a number: "))
    if guess < number:
     print("Low")
     attempt-=1
     print(f"Attempts left:{attempt}\n")
    elif guess > number:
     print("High")
     attempt-=1
     print(f"Attempts left:{attempt}\n")
    else:
     print("You guessed the number!")
     attempt=0
     game_finished=True

#Choose game level - Easy or Hard
while not level_selected:
 select_level=input("Easy or Hard?: ")
 if select_level=="Easy":
  attempt_initial=10
  level_selected=True
 elif select_level=="Hard":
  attempt_initial=5
  level_selected=True
#game start here
playGame(attempt_initial)




