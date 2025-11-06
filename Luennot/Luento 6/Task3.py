def main():
    print("Program starting.")

    name = askName() # askName fuktiosta saatu tieto sijoitetaan name muuttujaan
    greetUser(name) # greetUser funktiossa käytetään name muuttujaa joka saadaan askName funktiosta

    print("program ending.")
    return None

def askName():
    name = input("Insert name: ")
    return name

def greetUser(PName):
    print(f"Hello {PName}!")
    return None

main()