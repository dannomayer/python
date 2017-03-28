import random


def roll():
        rolled = random.randint(1,6)
        return rolled

def main():
        while True:
                user_roll = input("Press Enter to roll the die. Press q to quit\n")
                if user_roll != "q":
                        num_rolled = roll()
                        print("You rolled a", num_rolled, "\n")
                else:
                        break
        print("\nThanks for rolling\n")

main()

