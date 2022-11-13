logo = ('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ 
''')

cgr = ('''
╔═══╗─────────────╔╗───╔╗───╔╗
║╔═╗║────────────╔╝╚╗──║║──╔╝╚╗
║║─╚╬══╦═╗╔══╦═╦═╩╗╔╬╗╔╣║╔═╩╗╔╬╦══╦═╗╔══╗
║║─╔╣╔╗║╔╗╣╔╗║╔╣╔╗║║║║║║║║╔╗║║╠╣╔╗║╔╗╣══╣
║╚═╝║╚╝║║║║╚╝║║║╔╗║╚╣╚╝║╚╣╔╗║╚╣║╚╝║║║╠══║
╚═══╩══╩╝╚╩═╗╠╝╚╝╚╩═╩══╩═╩╝╚╩═╩╩══╩╝╚╩══╝
──────────╔═╝║
──────────╚══╝
''')

stages = [
  '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

word_list = [
  'gradually', 'fetch', 'compatible', 'compatibility', 'blueprint', 'ensure',
  'neat', 'subtle', 'alias', 'constitute', 'constitution'
]

import random

import os


def screen_clear():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')


chosen_word = random.choice(word_list)
#print(f"The chosen word is: {chosen_word}\n")
length_of_chosen_word = len(chosen_word)

display = []
for letter in chosen_word:
  display.append("_")

#print(" *** - HANGMAN GAME - *** ")
print(logo)
minus = 1
lives = 6
print(f"\nYou have {lives} lives!\n")
print("\nThis is the Hidden Word:")
print(display)
print("\nTry to guess the hidden word, before the man gets hanged!")

guessed_letters = []
while True:
  guess = input("\nMake a guess, type a letter\n:").lower()
  screen_clear()
  guessed_letters += guess
  for position in range(length_of_chosen_word):  #for3 = 0,1,2
    if chosen_word[position] == guess:
      display[position] = guess

  if guess not in chosen_word:
    lives -= 1
    minus += 1
    print(stages[len(stages) - minus])
    if lives != 0:
      print("NOPE!!! TRY ANOTHER ONE!\n")
    if lives == 0:
      print("!!! YOU HAVE HANGED THE MAN !!!")
      print("\n! You lost !")
      print(
        f"\nHidden Word Was:\n\n-- _______  ''  {chosen_word.upper()}  ''  _______ --\n"
      )
      break

  display_str = ""
  for x in display:
    display_str += x
  if display_str == chosen_word:
    print(display)
    print("\n\n___!! YOU WON !!___")
    print(cgr)
    break
  print(display)
  print(f"Previous Guesses: {guessed_letters}")
  print(f"You have {lives} lives left!\n")
