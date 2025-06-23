from random import choice,random

def random_word():
    words = ["apple","banana","mango"]
    first_word = random.choice(words)
    return first_word

def main():
    word = random_word()
    print("-----Spelling Bee-----")
    print(f"your first word is {word}")
    letter = word[-1]
    print(f"now start with letter {letter}")

    while(True):
        user_words = input("> ")
        user_letter = user_words[0]
        if user_letter == letter:
            next_word = user_words
            next_letter = next_word[-1]
            letter = next_letter
            print(f"right! next letter {letter}")
            #bypassing game highly prohibitted ;) -a programmer
        else:
            print(f"{user_words} not start with letter {letter}")
            exit(0)


if __name__ == "__main__":
    main()