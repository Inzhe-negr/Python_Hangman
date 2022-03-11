import random

words = ['python', 'java', 'kotlin', 'javascript']
word = ""
chars = []


def hint():
    return "".join((char if char in chars else "-" for char in word))


def read_letter():
    is_input_error = True
    while is_input_error:
        print()
        print(hint())
        text = input("Input a letter: ").strip()
        if len(text) != 1:
            print("You should input a single letter")
        elif text.isascii() and text.islower() and text.isalpha():
            if text in chars:
                print("You've already guessed this letter")
            else:
                is_input_error = False
        else:
            print("Please enter a lowercase English letter")
    return text


def menu_input():
    decision = ""
    while decision not in ["play", "exit"]:
        decision = input('Type "play" to play the game, "exit" to quit: ').strip()
    return decision


print("H A N G M A N")
while menu_input() == "play":
    chars = []
    word = random.choice(words)
    lives = 8
    while lives > 0:
        letter = read_letter()
        if letter not in word:
            lives -= 1
            print("That letter doesn't appear in the word")
        chars.append(letter)
        if not ("-" in hint()):
            print("\n" + word)
            print("You guessed the word!\nYou survived!\n")
            break
    else:
        print("You lost!\n")
