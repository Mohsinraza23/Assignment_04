import random
print("\n ✨Welcome to the Number Guessing Game.✨ \n")
print("\n 💻 Computer Guess the Number. \n")

low = 1
high = 10

print("🤔 Think of a number between 1 and 10, and 💻 will try to guess it!")
if low <= high:
    guess = random.randint(low,high)
    print(f"🤖 Is your number {guess}?")

    feedback=input(" 👉 Enter 'h' to indicate the guess is too high, 'l' to indicate the guess is too low, or 'c' to indicate I guessed correctly: ").lower()
    if feedback=='h':
        high = guess - 1
    elif feedback == 'l':
        low = guess + 1
    elif feedback == 'c':
        print(f"🎉 🎉🎉🎉🎉 Yay! 💻 guess the {guess} correctly. 🎉 🎉🎉🎉🎉")
    else:
        print("⚠️ Invalid input. Please enter only 'h', 'l', or 'c'. 🚫")

    if low > high:
        print("😅 Hmm... It seems there was a misunderstanding. Let's try again! 🔄")