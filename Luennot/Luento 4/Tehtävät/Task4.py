print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")

name = input("Before the menu, please insert your name: ")

print("\nOptions: " \
"\n1 - Print welcome message" \
"\n2 - Print the name backwards" \
"\n3 - Print the first character" \
"\n4 - Show the amount of characters in the name" \
"\n0 - Exit")
# annetaan vaihtoehdot

choice = int(input("Your choice: "))

if choice == 1:
    print(f"Welcome {name}!")
elif choice == 2:
    print(f"your name backwards is \"{name[::-1]}\"")
elif choice == 3:
    print(f"the first character in name \"{name}\" is \"{name[0]}\"")
elif choice == 4:
    print(f"There are {len(name)} characters in the name \"{name}\"")
elif choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")
#  verrataan valintaa ja annetaan oikea tuloste

print("\nProgram ending.")