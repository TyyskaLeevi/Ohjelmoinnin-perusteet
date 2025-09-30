print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.\n")

print("Options:" \
"\n1 - Length" \
"\n2 - Weight" \
"\n0 - Exit")
# annetaan vaihtoehdot

main_choice = int(input("Your choice: ").strip())

if main_choice == 1:
    print("\nLength options:" \
    "\n1 - Meters to kilometers" \
    "\n2 - Kilometers to meters" \
    "\n0 - Exit")

    length_choice = int(input("Your choice: ").strip())

    if length_choice == 1:
        meters = float(input("Insert meters: ").strip())
        km = round(meters / 1000, 1)
        print(f"{meters} m is {km} km")

    elif length_choice == 2:
        km = float(input("Insert kilometers: ").strip())
        meters = round(km * 1000, 1)
        print(f"{km} km is {meters} m")

    elif length_choice == 0:
        print("Exiting...")
    
    else:
        print("Unknown option.")
# Jos valitaan 1 mennään pituusvalikkoon ja siellä kysytään uusi valinta ja tehdään tarpeelliset muutokset ja annetaan tulos käyttäjälle

        

elif main_choice == 2:
    print("\nWeight options:" \
    "\n1 - Grams to pounds" \
    "\n2 - Pounds to grams" \
    "\n0 - Exit")

    weight_choice = int(input("Your choice: ").strip())

    if weight_choice == 1:
        grams = float(input("Insert grams: ").strip())
        lbs = round(grams * 0.00220462262185, 1)
        print(f"{grams} g is {lbs} lb") 

    elif weight_choice == 2:
        lbs = float(input("Insert pounds: ").strip())
        grams = round(lbs * 453.59237, 1)
        print(f"{lbs} lb is {grams} g")

    elif weight_choice == 0:
        print("Exiting...")
    
    else:
        print("Unknown option.")
# Jos valitaan 2 mennään painovalikkoon ja siellä kysytään uusi valinta ja tehdään tarpeelliset muutokset ja annetaan tulos käyttäjälle


elif main_choice == 0:
    print("\nExiting...")


else:
    print("Unknown option.")



print("\nProgram ending.")