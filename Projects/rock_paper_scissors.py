import random
valid_choice = ['rock','paper','scissors']
def get_user_input(valid_choice):


    user_choice = input("Enter your choice(rock , paper ,scissors) ").lower()
   
    if user_choice not in valid_choice:
      
      print("Wrong choice")
    return user_choice 
def computer_choice(valid_choice):
   
   comp = random.choice(valid_choice)
   return comp
def determine_winner(user_choice,computer_choice):
  

  if user_choice == computer_choice:
   result="Draw!"
  elif user_choice == "rock" and computer_choice == "scissors" :
    result="You win!"
  elif user_choice== 'scissors' and computer_choice == 'paper':
   result="You win!"
  elif user_choice == 'paper' and computer_choice == 'rock':
    result = 'You win!'
  else:
    result= 'You lose!'
  return(result)


while True:
  
    print("Welcome to Rock, Paper, Scissors!")  

    user_choice = get_user_input(valid_choice)

    print(f"You chose: {(user_choice)}")

    computer_choice3=computer_choice(valid_choice)
    print(f"Computer chose: {(computer_choice3)}")
    result = determine_winner(user_choice,computer_choice3)
    print(result)
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
      break
print("GOODBYE")





