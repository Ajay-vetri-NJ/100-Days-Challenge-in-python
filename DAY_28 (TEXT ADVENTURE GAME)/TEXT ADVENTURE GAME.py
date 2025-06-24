def intro():
    print("Welcome, brave adventurer!")
    print("You find yourself standing in front of a dark, mysterious cave.")
    print("Your goal is to explore and find the hidden treasure.")
    print("What would you like to do?")
    print("1. Enter the cave.")
    print("2. Walk away.")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        enter_cave()
    elif choice == "2":
        walk_away()
    else:
        print("Invalid choice. Please choose again.")
        intro()

def enter_cave():
    print("\nYou step inside the cave. It's dark and cold.")
    print("You see two paths ahead:")
    print("1. Take the left path.")
    print("2. Take the right path.")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        left_path()
    elif choice == "2":
        right_path()
    else:
        print("Invalid choice. Please choose again.")
        enter_cave()

def walk_away():
    print("\nYou decide it's best not to risk it and walk away.")
    print("However, you will never know what treasures or dangers were hidden in that cave...")
    print("Game Over.")

def left_path():
    print("\nYou take the left path.")
    print("The tunnel leads you deeper into the cave, and you hear strange noises.")
    print("Suddenly, a giant spider drops down in front of you!")
    print("What will you do?")
    print("1. Fight the spider.")
    print("2. Run back to the cave entrance.")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        print("\nYou bravely fight the spider and defeat it!")
        print("You move forward and find a chest filled with treasure!")
        print("Congratulations, you found the treasure!")
    elif choice == "2":
        print("\nYou run back to the cave entrance. Maybe this cave is too dangerous for you.")
        print("Game Over.")
    else:
        print("Invalid choice. Please choose again.")
        left_path()

def right_path():
    print("\nYou take the right path.")
    print("The tunnel is long and winding, but eventually, you reach a room filled with glowing crystals.")
    print("In the center of the room, you see a pedestal with a golden key on it.")
    print("What will you do?")
    print("1. Take the key.")
    print("2. Leave the key and explore elsewhere.")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        print("\nYou take the key, and the ground starts to shake!")
        print("The cave begins to collapse, and you barely manage to escape with the key!")
        print("You rush out of the cave with the key in hand, but the treasure remains hidden inside.")
        print("Game Over.")
    elif choice == "2":
        print("\nYou leave the key and decide it's not worth the risk.")
        print("As you explore further, you find a hidden passage leading to the treasure room!")
        print("Congratulations, you found the treasure!")
    else:
        print("Invalid choice. Please choose again.")
        right_path()

if __name__ == "__main__":
    intro()
