import random

def get_random_number():
    print("Do you want to generate a random number?(yes/no)")
    
    user_response = input().lower()

    if user_response == "yes":
        return random.choice(list(range(1, 10000001)))
    else:
        print("Okay, no problem then.")
        return None

result = get_random_number()
if result:
    print(result)
