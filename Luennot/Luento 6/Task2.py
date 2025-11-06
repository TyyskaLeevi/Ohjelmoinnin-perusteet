def main (): # Main funktiossa pyydetään sanaa jolle tehdään reunus
    print("Program starting.")
    PWord = input("Insert word: ")
    print()
    frameWord(PWord)
    print("\nProgram ending.")
    return None

def frameWord (PWord): # frameword funktio jossa tehdään reunus sanalle
    border = "*" * (len(PWord) + 4) # len +4 jotta reunus ympäröi koko sanan
    print(border)
    print(f"* {PWord} *")
    print(border)
    return None

main()