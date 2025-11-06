def showOptions() -> None:  # näytetään valikko
    print("Options:\n" \
    "1 - Show count\n" \
    "2 - Increase count\n" \
    "3 - Reset count\n" \
    "0 - Exit")

def askChoice() -> int: # pyydetään valinta ja palautetaan se arvo
    choice = input("Your choice: ")

    if choice.isnumeric():
        return int(choice)
    else:
        print("Unknown option!")
        return -1  # jos input ei ole numero palautetaan tuntematon valinta
    
def main():
    print("Program starting.")
    count = 0

    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            print(f"Current count - {count}")
        elif choice == 2:
            print("Count increased!")
            count += 1
        elif choice == 3:
            print("Cleared count!")
            count = 0
        elif choice == 0:
            print("Exiting program.")
            break
        elif choice == -1:
            pass
        else:
            print("Unknown option!")

        print()

    print("\nProgram ending.")

main()