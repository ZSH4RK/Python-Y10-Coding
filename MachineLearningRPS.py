import random as rn
computer_choices = ["rock", "paper", "scissors"]
def LearningRPS(computer_choices):
  computer = rn.choice(computer_choices)
  human = input()
  if human == "rock":
    computer_choices.append("paper")
    if computer == "rock":
      print("draw")
    elif computer == "paper":
      print("computer")
    else:
      print("human")
  elif human == "paper":
    computer_choices.append("scissors")
    if computer == "rock":
      print("human")
    elif computer == "paper":
      print("draw")
    else:
      print("computer")
  else:
    computer_choices.append("rock")
    if computer == "rock":
      print("computer")
    elif computer == "paper":
      print("human")
    else:
      print("draw")

while True:
  LearningRPS(computer_choices)
  
