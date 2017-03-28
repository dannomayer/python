import random
import sys
import string
import time


#Hangman Drawing


hangman_drawing =  """  
 _________     
|         |    
|         0   
|        /|\\ 
|        / \\  
|  
| """

drawing = hangman_drawing.split('\n')

hangman_text = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    """




def main():
        print(hangman_text)

        start = input("\n press h for instructions or any key to continue\n")
        if start is "h":
                print("Guess the word by typing a letter you think could be in it. But too many wrong guesses and you get the hangman!. It's unlikely you will know the word, this program uses the entire dictionary. A good way to expand your vocab!")
        
#getting the word        
        dictionary_file = "/usr/share/dict/words"
        wordNum = random.randint(1,235886) #number of words in built in dictionary
        wordList = open(dictionary_file).read().splitlines()
        word = wordList[wordNum]
        word_secure = False
        while word_secure is not True:
                if len(word) > 7:
                        wordNum += 1
                        word = wordList[wordNum]
                else:
                        word_secure = True
        letters = len(word)

#setting up the hangman ascii art
        guessing = True
        #create an array to track guesses already made
        incorrect_guesses = list()
        correct_guesses = list()
        hang_count = 0 #number of incorrect guesses

#guessing process
                    #if the guess is occurs at least once, don't waste time trying to store
                    #exactly where else it could be. instead, note that it's there once and parse upon
                    #printing the updated hangman word sequence for other occurences of letter
        while guessing:
                guesses_left = False
                print("\n\n")
                for i in range(0,letters):
                        if word[i] in correct_guesses:
                                sys.stdout.write(" ")
                                sys.stdout.write(word[i])
                                sys.stdout.write(" ")
                        else:
                                sys.stdout.write(" _ ") #using print creates a newline each loop
                                guesses_left = True
                if guesses_left is False:
                        print("\n\nYou've won! Congratulations!\n\n")
                        time.sleep(1)
                        guessing = False
                        break
                print("\n\n")
                guess = input("Guess a letter\n")
                if guess in correct_guesses or guess in incorrect_guesses:
                        print("\nYou already guessed that. Try again\n")
                        time.sleep(.7)
                        continue
                if guess in word: #look how easy it is to search a string in python!!!! 
                        #need to add the guess to an array of correctly guessed letters for printing purposes
                        correct_guesses.append(guess)
                        print("\nThat's a good guess!")
                        time.sleep(.7)
                else:
                        incorrect_guesses.append(guess)
                        print("Bad guess! \n")
                        hang_count += 1
                        for i in range(0,hang_count):
                                if hang_count > len(drawing):
                                        print("You hung him! Game over")
                                        time.sleep(.7)
                                        print("The word you were looking for is", word)
                                        time.sleep(1)
                                        guessing = False
                                        break
                                else:
                                        print(drawing[i])
                        time.sleep(1)
                                
                                
main()        
