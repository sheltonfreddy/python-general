''' The user guesses a number between 0 and 100 and returns in '''

import random


def guess_number(guessed_no, name):

    guesses = 0
    while True:
        number = int(input("Hi {}, I've a no: b/w 0 and 100 in my mind. Can you guess that number?\n".format(name)))
        if type(guessed_no) is not int:
            print("Enter an Integer!!")
        if number < guessed_no:
            print ("Guess is low")
            guesses += 1
        elif number > guessed_no:
            print("Guess is higher")
            guesses += 1
        else:
            guesses += 1
            print('Good Job!! You have guessed in {} tries'.format(guesses))
            play_again()
            break

def play_again():
    ans = input("Do you want to play again? (y/n)\n")
    if ans.lower() == 'y':
        main()
    else:
        print ('Bye!')


def main():
    name = input("Please enter your name\n")
    computer_guess = random.randint(1,100)
    guess_number(computer_guess,name)


if __name__ == '__main__':
    main()