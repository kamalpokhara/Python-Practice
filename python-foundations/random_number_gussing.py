import random

random_number = random.randint(0,100)

while True:
    user_input =  int(input("Please entre a guess [number only]"))


    if random_number == user_input:
        print("Correct number")
        break
        

    elif user_input > random_number:
        print("User guess is High")
        
    elif user_input < random_number:
        print("User guess is Low")

    else:
        print(" Incorrect guess")    
    
print(f"Random number was {random_number}")
