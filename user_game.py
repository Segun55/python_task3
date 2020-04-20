import random
def Game():
    #user decides level
    print("There are three stages, EASY, MEDIUM and HARD")
    decide = str(input("type in the desired stage "))
    
    #Stage 1 EASY
    if decide.lower() == "easy": 
        print("guess a number between 1 to 10")
    
        secret_number = random.randint(1,10)
        guess_count = 1
        guess_limit = 6
        while guess_count <= 6:

            print(f"you have {7 - guess_count} guesses left")
            guess = int(input("guess a number "))
            guess_count += 1

            if guess == secret_number:
                print("You got it right!")
                break   
            else:
                print("That was wrong")
                
        print("GAME OVER!")
        
    #Stage 2 MEDIUM    
    elif decide.lower() == "medium":
        print("guess a number between 1 to 20")

        secret_number = random.randint(1,20)
        guess_count = 1
        guess_limit = 4
        while guess_count <= 4:

            print(f"you have {5 - guess_count} guesses left")
            guess = int(input("guess a number "))
            guess_count += 1

            if guess == secret_number:
                print("You got it right!")
                break
            else:
                print("That was wrong")


        print("GAME OVER!")
        
    #stage 3 HARD    
    elif decide.lower() == "hard":
        print("guess a number between 1 to 50")

        secret_number = random.randint(1,50)
        guess_count = 1
        guess_limit = 3
        while guess_count <= 3:

            print(f"you have {4 - guess_count} guesses left")
            guess = int(input("guess a number "))
            guess_count += 1

            if guess == secret_number:
                print("You got it right!")
                break
            else:
                print("That was wrong")


        print("GAME OVER!")
        
    else:
        return Game()