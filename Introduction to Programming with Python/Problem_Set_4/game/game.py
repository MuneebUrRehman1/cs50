import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            number = random.randint(0, level)
            while True:
                try: 
                    guess = int(input("Guess: "))
                    if guess == number:
                        print("Just right!")
                        break
                    elif guess < number:
                        print("Too small!")
                    else:
                        print("Too large!")
                except ValueError:
                    pass
            break
    except ValueError:
        pass
    
