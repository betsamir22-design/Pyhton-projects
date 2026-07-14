import random

def welcome():
    print("""==========Welcome to the guess number game==========""")
    
    
def random_computer_number():
    
     return random.randint(0,100)
     
     
def exit_continue():
      while True:
        choice=input("Do you want to exit (yes,no) :").strip().lower()
        if choice in ["yes","y"]:
            return True
            
        elif choice in["no","n"]:
            return False
           
        else:
            print("please choose yes or no")
    
    
def random_user_number():
    while True:
       try:
          return int(input("Write the number :"))
       except ValueError:
    	     print("please choose a random number")
  
def game():
 attempts=0
 random_number=random_computer_number()
 while True:
     number=random_user_number()
     if random_number==number:
        attempts+=1
        print("congratulations!you won")
        print(f"you guessed it in {attempts} attempts")
        if exit_continue():
        	return
      
     elif random_number<number:
        print("this is high")
        print("your guess is wrong,try again")
        attempts+=1
     elif random_number>number:
     	print("this is low")
     	print("you guess is wrong")
     	attempts+=1
            
            
    
        
 
        