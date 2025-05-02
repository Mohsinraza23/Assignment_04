import time
print("\n ⏲️⏰⏱️ Welcome to the Countdown Timer. ⏲️⏰⏱️ \n")

def countdown_timer(seconds):
  while seconds:
    mins,secs = divmod(seconds,60)
    time_display = f"{mins:02d}:{secs:02d}"
    print(f"\r⏳ {time_display} ⏳", end="")
    time.sleep(1)
    seconds -= 1
  print("\n🚨 Time's up ⏰")
try:
    total_time = int(input("Enter the time in seconds:"))
    countdown_timer(total_time)
except ValueError:
    print("❌ Invalid input! Please enter a valid input!")