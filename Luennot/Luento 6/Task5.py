def showMenu() -> str:  # näytetään menu ja palautetaan käyttäjän valinta
    print("Options:\n" \
    "1 - Insert word\n" \
    "2 - Show current word\n" \
    "3 - Show current word in reverse\n" \
    "0 - Exit")
    choice = input("Your choice: ")
    return choice 

def insWord() -> str:  # pyydetään käyttäjältyä uusi sana ja palautetaan se
    word = input("Insert word: ")
    return word

def showWord(word: str) -> None:  # näyetään sana 
    print(f'Current word - "{word}"')

def revWord(word: str) -> None:  # näytetään sana takaperin
    print(f'Word reversed - "{word[::-1]}"')

def main():
    print("Program starting.")
    word = ""
    
    while True:
        choice = showMenu()

        if choice == "1":
            word = insWord()
        elif choice == "2":
            showWord(word)
        elif choice == "3":
            revWord(word)
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Unknown option! Try again.")

        print()

    print("\nProgram ending.")

main()