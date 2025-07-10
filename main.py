import random

Count = 0
word = None
dashes = None

words = [
    "apple", "banana", "orange", "grape", "lemon", "peach", "cherry", "melon", "pear", "plum",
    "mango", "kiwi", "apricot", "avocado", "blueberry", "coconut", "fig", "guava", "lime", "papaya",
    "pineapple", "raspberry", "strawberry", "watermelon", "blackberry", "cranberry", "date", "elderberry", "gooseberry", "jackfruit",
    "lychee", "mandarin", "nectarine", "olive", "passionfruit", "persimmon", "pomegranate", "quince", "tangerine", "currant",
    "dragonfruit", "durian", "grapefruit", "kumquat", "longan", "mulberry", "rambutan", "starfruit", "soursop", "ugli",
    "carrot", "broccoli", "cabbage", "cauliflower", "celery", "cucumber", "eggplant", "garlic", "lettuce", "onion",
    "pea", "pepper", "potato", "pumpkin", "radish", "spinach", "squash", "tomato", "turnip", "zucchini",
    "beet", "chard", "leek", "okra", "parsnip", "rutabaga", "shallot", "yam", "artichoke", "asparagus",
    "basil", "cilantro", "dill", "fennel", "ginger", "mint", "oregano", "parsley", "rosemary", "sage",
    "thyme", "vanilla", "wasabi", "anise", "bay", "chive", "clove", "coriander", "cress", "marjoram"
]

def start_game():
    global word, dashes
    word = random.choice(words)
    dashes = ["_"] * len(word)
    print(" ".join(dashes))

def guess():
    global word, dashes, Count
    user_choice = input("Guess the letter: ").lower()
    found = False
    for idx, char in enumerate(word):
        if char == user_choice:
            dashes[idx] = char
            found = True
    if found:
        print("You have guessed the letter correctly!")
    else:
        print("This letter is not present in this word")
        Count += 1
    print(" ".join(dashes))

def main():
    global Count
    user_input = input("Do you want to start the game? (y/n): ").lower()
    if user_input in ("y", "yes"):
        start_game()
        while Count < 6 and "_" in dashes:
            guess()
        if "_" not in dashes:
            print("Congratulations! You guessed the word:", word)
        else:
            print("Game over! The word was:", word)
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()