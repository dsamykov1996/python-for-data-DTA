import random # random.randrange(5) 
# import random as r # r.randrange(5)
# from random import * # randrange(5)
# from random import randrange, randint # randrange(5)
# from random import randrange as rr # rr(5)
# # from numpy import *

comp_choice = random.randint(0,100)
n_count = 0

while n_count < 3:
    try:
        user_choice = int(input("enter number:"))
    except ValueError:
        print("Incorrect") 
        continue 
    else:
        print("Excelent! I remeber your number")
    finally:
        n_count += 1
        # print(f"Your choice" {user_choice})      
        print(f"Your attempt {n_count}") 

    if user_choice < comp_choice:
        print("number is bigger")
    elif user_choice > comp_choice:
        print("number is smaller")
    

    if user_choice == comp_choice:
        print("Congratulations")
        break    
    print("Try agaiin!")


