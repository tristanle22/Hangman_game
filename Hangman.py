# Hangman game

#generate a list of alphabet
import string
import random
from time import sleep
import sys

#define Word class and its attribute, methods
class Word(object):
    def __init__(self, name, theme):
        self.name = name
        self.theme = theme

        if self.theme == 'animals':
            animals.append(self)
        elif self.theme == 'geography':
            geography.append(self)
        elif self.theme == 'food':
            food.append(self)
        else:
            print('What theme?')

    def word_count(self):
        return len(self.name)

    def separate_word(self):
        return list(self.name)


    def print_dash(self):
        dash_list = list("_"*len(self.name))
        return dash_list

animals = []
geography = []
food = []

theme_collection = [animals, geography, food]
#adding words to lists
word1 = Word('crocodile', 'animals')
word2 = Word('elephant', 'animals')
word3 = Word('spaghetti', 'food')
word4 = Word('dimsum', 'food')
word5 = Word('himalaya', 'geography')
word6 = Word('pangea', 'geography')
word7 = Word('AnhTyHam', 'animals')
#call up the random word
#create a list of word and use random method to "pop" word

game_intro = """
Hangman - designed by Tristan Le
Welcome to the game of Hangman.
There will be 3 themes:

Animals - Food - Geography

You will have 5 guesses

Good luck!"""

def typewritter(line, new_line):
    if new_line == '1':
        for x in line:
            print(x, end='')
            sys.stdout.flush()
            sleep(0.1)
        print("\n")
    else:
        for x in line:
            print(x, end='')
            sys.stdout.flush()
            sleep(0.1)

typewritter(game_intro, '1')

def engine():
    #generate alphabet list
    alphabet = list(string.ascii_lowercase)
    #call up the random word
    #create a list of word and use random method to "pop" word
    word = random.choice(random.choice(theme_collection))
    hidden_word = word.print_dash() #create a list of underscore
    disposed = [] #create a list of used letters
    i = 5 #trials
    list_word = word.separate_word() #turn "word" string into a list
    print(alphabet)
    typewritter("The hidden word is: ", None)
    print('.'.join(hidden_word)) #display the hidden word list as string

    while i > 0:
        typewritter('Used letters are: ', None)
        print(disposed)
        typewritter('Theme: ', None)
        typewritter(word.theme, '1')

        letter = input("> ")

        if letter in list_word:
            if letter not in disposed:
                append_remove(alphabet, disposed, letter)
                for pos, val in list(enumerate(list_word)):
                    if val == letter:
                        hidden_word[pos] = letter

                print("\n")
                print(alphabet)
                print("\n")
                print('.'.join(hidden_word))

                if '_' not in hidden_word:
                    print(hidden_word)
                    end_game(i)
            else:
                line()
                print("Try another letter")
                line()
        else:
            if letter not in disposed:
                line()
                typewritter("OOPSIE!", '1')
                append_remove(alphabet, disposed, letter)
                i = i - 1
                typewritter("you have {} guess[es] left".format(i), '1')
                line()
            else:
                line()
                print("Try another letter")
                line()
    end_game(i)

def append_remove(list1, list2, letter):
    list1.remove(letter)
    list2.append(letter)

def line():
    print("___________")

def end_game(i):
    if i == 0:
        typewritter("You lost...Good luck next time!", '1')
    else:
        typewritter("Congratulations, YOU WON!", '1')

    while True:
        redo = input("Do you want to replay the game? \n>")
        if redo == 'yes':
            engine()
        elif redo == 'no':
            typewritter("Thank you for playing!", None)
            sys.exit()
        else:
            typewritter("I don't get it", None)

engine()
