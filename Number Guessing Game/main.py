import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def do_easy(num_final):
    turns_left = EASY_LEVEL_TURNS
    take = 0
    print(f"You have {turns_left} attempts remaining to guess the number")
    while(turns_left>0):
        take = int(input("Make A Guess: "))
        if take==num_final :
            return 1
        elif take<num_final:
            print("Too Low")
            turns_left-=1
        else:
            print("Too High")
            turns_left-=1
        if(turns_left>0):
            print("Guess again")
        print(f"You have {turns_left} left")
    return 0
    
    
def do_hard(num_final):
    turns_left = HARD_LEVEL_TURNS
    take = 0
    print(f"You have {turns_left} attempts remaining to guess the number")
    while(turns_left>0):
        take = int(input("Make A Guess: "))
        if take==num_final :
            return 1
        elif take<num_final:
            print("Too Low")
            turns_left-=1
        else:
            print("Too High")
            turns_left-=1
        if(turns_left>0):
            print("Guess again")
        print(f"You have {turns_left} left")
    return 0
    
    
def perform(level, num_final):
    if level=="easy" :
        condition = do_easy(num_final)
    else:
        condition = do_hard(num_final)    
    return condition

print(logo)
print("Welcome tothe Number Guessing Game!")
print("I 'm thinking of a number between 1 and 100")
num_final = random.randint(1,100)
print(num_final)
level = input("Choosen a difficulty level. Type 'easy' or 'hard': ").lower()
condition = perform(level,num_final)

if condition==1:
    print("You Won🙂🙂")
else:
    print("You Lost😏😏")
    