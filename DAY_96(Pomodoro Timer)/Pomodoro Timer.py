import time

def pomodoro_timer(work_minutes, short_break_minutes, cycles):
    print("Welcome to the Pomodoro Timer!")
    print(f"Focus for {work_minutes} minutes, then take a short {short_break_minutes}-minute break.")
    print(f"Complete {cycles} cycles to stay productive.\n")
    
    for cycle in range(1, cycles + 1):
        print(f"Cycle {cycle} - Work Time!")
        countdown(work_minutes * 60)
        print("\nTime for a short break!")
        countdown(short_break_minutes * 60)
        print("\n--- Cycle Completed ---")
    
    print("\nCongratulations! You've completed all your Pomodoro cycles!")

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")  
        time.sleep(1)
        seconds -= 1

try:
    work_minutes = int(input("Enter work duration (in minutes): "))
    short_break_minutes = int(input("Enter break duration (in minutes): "))
    cycles = int(input("Enter the number of cycles: "))
    
    pomodoro_timer(work_minutes, short_break_minutes, cycles)
except ValueError:
    print("Invalid input. Please enter valid numbers.")