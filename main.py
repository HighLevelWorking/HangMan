import random

Count = 0
word = None

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

def dashes():
    global words
    global word
    word = random.choice(words)
    num_dashes = len(word)
    dashes = "__  " * num_dashes
    print(dashes)

def guess():
    global word
    user_Choice = input("Guess the letter: ")
    word = list(word)
    if user_Choice in word:
        print("You have guessed the letter correctly! ")
    else:
        print("This letter is not present in this word")


def main():
    global Count
    user_input = input("Do you want to start the game? (y/n): ").lower()
    if user_input == "y" or user_input == "yes":
        dashes()
        while Count <= 6:
            guess()
    else:
        return False
    
if __name__ == "__main__":
    main()