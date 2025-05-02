import random
print("\n ✨Welcome to the Number Guessing Game.✨ \n")
print("\n 👨‍💻 User Guess the Number 👩‍💻 \n")

Secret_Number = random.randint(1,10)
print("🎯 I have a Secret Number between 1 to 10. Can you guess it? 🤔")

while True:
  try:
    guess = int(input("🔢Guess the Number."))

    if guess > Secret_Number:
      print("📈 Too High! Try again. 🔄")
    elif guess < Secret_Number:
      print("📉 Too Low! Try again. 🔄")
    else:
      print("🎉 🎉🎉🎉🎉 Congratulation you guess the right number. 🎉 🎉🎉🎉🎉" )
      break
  except ValueError:
    print("⚠️ Please enter a valid number! 🚫")