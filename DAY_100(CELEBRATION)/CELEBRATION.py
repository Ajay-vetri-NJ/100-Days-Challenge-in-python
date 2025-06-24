import time
import os

def display_banner(message):
    print("\n" + "*" * 50)
    print(f"{message:^50}")
    print("*" * 50 + "\n")

def new_year_countdown(seconds):
    print("🎆 Get ready for the New Year 2025! 🎇")
    while seconds:
        print(f"New Year in... {seconds} seconds", end="\r")
        time.sleep(1)
        seconds -= 1
    print("✨ Happy New Year 2025! 🎉🎈")

def celebrate_day_100():
    display_banner("Day 100 of #100DaysOfCode")
    print("🎉 Congratulations on this incredible milestone! 🎊")
    print("Here's to your dedication, learning, and growth in Python. 🚀\n")

def fireworks():
    print("🎆 Launching fireworks to celebrate! 🎆\n")
    firework_frames = [
        "         .     .  .      +     .      .          .",
        "     .       .      .     #       .           .",
        "        .      .         *      .       .          .",
        "      .    .     .      o      .     .           +",
        "      +     .     .     *    +       .            .",
        "         .         .  . +        +       +",
    ]
    for frame in firework_frames * 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(frame)
        time.sleep(0.3)

def main():
    display_banner("Celebrating New Year 2025 and Day 100!")
    new_year_countdown(5)
    fireworks()
    celebrate_day_100()
    print("🎇 Keep coding, keep learning, and let's make 2025 amazing! 🎇")

if __name__ == "__main__":
    main()