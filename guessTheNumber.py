"""
The two problems I've encountered are:
1. numbers higher than around 300 do not show up as correctly guessed when
they are
2. using try and except to check input is an int. Does not work inside while
loop, but does outside... maybe something to do with nesting the while loops?
"""


import random
import time

def generate(max_number): #generates a random number based off user specified
                          #input.
        the_number = random.randint(0,max_number)
        return the_number


def main():
        guess_total = 1
        print("Welcome Guess The Number! To win, you have to guess the number the computer generates. The number will be an integer between 0 and the value you specify as the maximum. Good luck!")
        while True: 
                try:
                        upper_limit = int(input("Enter the number you wish to be the maximum possible value: "))
                        break
                except:
                        print("Oops! That's not a real number. Try again")
        correct = generate(upper_limit)
        print (correct, "\n")
        print("Good! Now, try to guess the number\n")
        guessing = True
        while guessing:
#                while True:
#                        try:
                guess = int(input("Enter your guess: "))
#                                break
#                        except:
#                                ("Please enter a valid number")
                if guess is correct:
                        print("You got it! Nice job. It took you ", guess_total, " guesses")
                        guessing = False
                elif guess < correct:
                        print("Too low, try again\n")
                        guess_total += 1
                        continue
                elif guess > correct:
                        print("Too high, try again\n")
                        guess_total += 1
                        continue
main()
