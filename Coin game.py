import random
games=0
wins=0
losses=0

while True:
    
 print("welcome to the coin guessing game! ")
 print("choose one of these methods: ")
 print("1.using random.random()")
 print("2.using random.randint()")
 user_choice=input("choose 1 or 2: ")
 if user_choice=="1":
    computer_choice=random.random()
    if computer_choice>=0.5:
        computer_result="heads"
    else:
        computer_result="tails"
    



 elif user_choice=="2":
    computer_choice=random.randint(0,1)
    if computer_choice==1:
        computer_result="heads"
    else:
        computer_result="tails"
    
    
 else:
    print("please choose 1 or 2: ")
    
 user_choice=input("choose (Heads or tails): ").lower()
 if user_choice in ["heads","tails"]:
   if user_choice==computer_result:
     print("congratulations, you won")
     wins+=1
   else:
    
     print(f"You lost! The coin was {computer_result}")
     losses+=1
   games+=1
 else:
     print("please choose heads or tails")
 
 print(f"games:{games}")
 print(f"wins:{wins}")
 print(f"losses:{losses}")
 playing_again=input("Do you want to play again or exit? (Yes,No): ").lower()
 if playing_again in ["yes","y"]:
    print("okay")
 else:
    break

    
