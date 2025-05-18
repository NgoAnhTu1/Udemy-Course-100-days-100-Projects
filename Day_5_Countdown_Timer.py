import time 

start = int(input("Enter the number to start the countdown: "))

print("\n--- Countdown Begins ---")

while start > 0:
    print(start)
    time.sleep(1)
    start -= 1

print("\n--- Countdown Complete ---")