import random

def game():
    # generate random number between 1 and 10
    secret_num = random.randint(1,10)
    guesses = []
    
    while len(guesses) < 5:
        try:
            # get a number from player
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            print("{} isn't a number you dummy!".format(guess))
            
        else:
            # compare to secret number
            if guess == secret_num:
            # print hit or miss
                print("You win! My number was {}".format(secret_num))
                break
            elif guess < secret_num:
                print("My number is higher than {}".format(guess))
            else:
                print("My number is lower than {}".format(guess))
            guesses.append(guess)
    else:   
        print("You didn't get it! My number was {}".format(secret_num))
    play_again = input("Do you want to play again? Y/n ")
    if play_again.lower() != 'n':
        game()
    else:
        print("Bye!")
            
game()
