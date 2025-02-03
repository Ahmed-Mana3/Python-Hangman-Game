# Hangman Game
import random
from words_list import words

Hangman = {0: ("   ",
               "   ",
               "   "),
           1: (" O ",
               "   ",
               "   "),
           2: (" O ",
               " | ",
               "   "),
           3: (" O ",
               "/| ",
               "   "),
           4: (" O ",
               "/|\\",
               "   "),
           5: (" O ",
               "/|\\",
               "/  "),
           6: (" O ",
               "/|\\",
               "/ \\")}


def get_word():
    word = random.choice(words)
    return word


def display_hangman(wrong_guesses):
    print("*********************")
    for line in Hangman[wrong_guesses]:
        print(line)
    print("*********************")


def main():

    your_guesses = []
    word = get_word()
    dashes = ["-"] * len(word)
    is_running = True
    wrong_guesses = 0

    print("Welcome to Hangman!")

    while is_running:

        # print the hangman and the word dashes
        display_hangman(wrong_guesses)
        print(" ".join(dashes))

        # check if the player Enters Valid Input
        answer = input("Enter The Letter: ")

        if len(answer) > 1:
            print("Please enter only one letter")
            continue

        if not answer.isalpha():
            print("Please enter only letters")
            continue

        if answer in your_guesses:
            print("You already guessed that letter")
            continue

        your_guesses.append(answer)

        # check if the player Guesses a correct letter
        if answer in word:
            for index in range(len(word)):
                if word[index] == answer:
                    dashes[index] = answer
        else:
            wrong_guesses += 1

        # check if the player has won or lost
        if "-" not in dashes:
            print("Congratulations! You won!")
            print(f"The word was {word}")
            is_running = False

        if wrong_guesses == 6:
            display_hangman(wrong_guesses)
            print("Sorry, You lost!")
            print(f"The word was {word}")
            is_running = False


if __name__ == '__main__':
    main()
