import random

# Hangman stages
stages = [
    '''
     +---+
     |   |
         |
         |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
         |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========''', '''
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
    /|\\  |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========='''
]

# 500 common English words 
common_words = [
    "apple", "banana", "grape", "orange", "mango", "peach", "watermelon", "melon", "berry", "cherry",
    "lemon", "lime", "kiwi", "pineapple", "plum", "apricot", "papaya", "fig", "date", "pomegranate",
    "table", "chair", "window", "keyboard", "screen", "laptop", "mouse", "bottle", "notebook", "pen",
    "pencil", "paper", "eraser", "book", "lamp", "phone", "cable", "charger", "bag", "clock",
    "love", "hope", "dream", "peace", "fight", "strong", "light", "dark", "truth", "happy",
    "sad", "angry", "laugh", "cry", "smile", "friend", "enemy", "fear", "brave", "kind",
    "school", "college", "teacher", "student", "classroom", "lesson", "exam", "test", "grade", "homework",
    "subject", "math", "science", "history", "geography", "art", "music", "computer", "physics", "chemistry",
    "earth", "moon", "planet", "galaxy", "space", "universe", "star", "sun", "comet", "asteroid",
    "orbit", "rocket", "satellite", "gravity", "eclipse", "meteor", "sky", "night", "telescope", "blackhole",
    "dog", "cat", "elephant", "lion", "tiger", "bear", "giraffe", "monkey", "horse", "sheep",
    "goat", "cow", "pig", "rabbit", "deer", "zebra", "snake", "fish", "shark", "whale",
    "bird", "eagle", "sparrow", "duck", "hen", "pigeon", "parrot", "owl", "bat", "insect",
    "river", "mountain", "valley", "ocean", "desert", "island", "beach", "lake", "forest", "cave",
    "hill", "cliff", "volcano", "iceberg", "plain", "jungle", "reef", "waterfall", "glacier", "swamp",
    "car", "bus", "bike", "train", "plane", "truck", "van", "boat", "ship", "submarine",
    "engine", "wheel", "brake", "mirror", "seat", "door", "window", "light", "horn", "radio",
    "red", "blue", "green", "yellow", "black", "white", "brown", "pink", "orange", "purple",
    "gold", "silver", "gray", "cyan", "magenta", "navy", "beige", "lime", "maroon", "teal",
    "run", "walk", "jump", "swim", "read", "write", "draw", "cook", "clean", "laugh",
    "dance", "sing", "talk", "listen", "look", "see", "eat", "drink", "play", "sleep",
    "wake", "work", "rest", "think", "plan", "study", "teach", "learn", "build", "create",
    "yes", "no", "maybe", "never", "always", "often", "sometimes", "rarely", "soon", "now",
    "before", "after", "early", "late", "today", "tomorrow", "yesterday", "morning", "evening", "night",
    "hot", "cold", "warm", "cool", "wet", "dry", "clean", "dirty", "soft", "hard",
    "fast", "slow", "high", "low", "long", "short", "big", "small", "old", "young",
    "man", "woman", "boy", "girl", "child", "baby", "father", "mother", "brother", "sister",
    "uncle", "aunt", "cousin", "friend", "neighbor", "stranger", "king", "queen", "prince", "princess",
    "city", "town", "village", "country", "capital", "road", "street", "bridge", "park", "market",
    "shop", "store", "mall", "bank", "school", "hospital", "office", "station", "hotel", "airport",
    "money", "coin", "note", "card", "wallet", "purse", "price", "sale", "cost", "value",
    "food", "drink", "bread", "rice", "meat", "fish", "fruit", "vegetable", "cheese", "egg",
    "milk", "butter", "sugar", "salt", "pepper", "spice", "soup", "cake", "cookie", "icecream",
    "job", "work", "boss", "salary", "task", "team", "meeting", "goal", "project", "deadline",
    "idea", "thought", "dream", "vision", "plan", "hope", "wish", "chance", "luck", "faith",
    "door", "wall", "floor", "ceiling", "roof", "window", "stair", "lift", "room", "hall",
    "kitchen", "bathroom", "bedroom", "livingroom", "garden", "garage", "balcony", "basement", "attic", "yard"
]


# Ensure we have enough
if len(common_words) < 500:
    common_words *= (500 // len(common_words)) + 1
    common_words = common_words[:500]

def play_hangman():
    word = random.choice(common_words)
    guessed = ['_'] * len(word)
    tries = 6
    guessed_letters = set()

    print("🎮 Welcome to Hangman!\n")
    while tries >= 0 and '_' in guessed:
        print(stages[6 - tries])
        print("Word: ", " ".join(guessed))
        print("Tries left:", tries)
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single alphabetical letter.\n")
            continue

        if guess in guessed_letters:
            print("ℹ️ You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            tries -= 1

    if '_' not in guessed:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print(stages[6])
        print("\n💀 Game over. The word was:", word)

# Run game
if __name__ == "__main__":
    play_hangman()