# Write your code here
import random
import string

def prompt(tries, clue, key):
    guessed = set()
    while tries != 0 and key != clue:
        print("\n" + clue)
        letter = input("Input a letter: ")

        if len(letter) != 1:
                print("You should input a single letter")
        else:
            if letter in guessed:
                print("You've already guessed this letter")
            elif letter in key:
                clue = swap(letter, clue, key)
            else:
                if letter not in string.ascii_lowercase:
                    print("Please enter a lowercase English letter")
                else:
                    print("That letter doesn't appear in the word")
                    tries -= 1
            guessed.add(letter)
    if key == clue:
        print(f"""{clue}
You guessed the word!
You survived!""")
    else:
        print("You lost!")
    guessed.clear()

def swap(letter, clue, key):
    for i in range(len(key)):
        if key[i] == letter:
            clue = clue[:i] + letter + clue[i+1:]
    return clue

def main():
    words = ['python', 'java', 'kotlin', 'javascript']
    print("H A N G M A N")
    while True:
        command = input('Type "play" to play the game, "exit" to quit: ')
        if command == "play":
            key = random.choice(words)
            clue = ""
            for c in key:
                clue += "-"
            tries = 8
            prompt(tries, clue, key)
        elif command == "exit":
            exit()

if __name__ == "__main__":
    main()
