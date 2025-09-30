print("Program starting.\n")

print("\nOptions: " \
"\n1 - Celsius to Fahrenheit" \
"\n2 - Fahrenheit to Celsius" \
"\n0 - Exit")
# annetaan käyttäjälle vaihtoehdot

choice = int(input("Your choice: "))

if choice == 1:
    temp = float(input("Insert the amount of Celsius: "))
    fahrenheit = round((temp * 1.8 + 32), 1)
    print(f"{temp} °C equals to {fahrenheit} °F")
elif choice == 2:
    temp = float(input("Insert the amount of Fahrenheit: "))
    celsius = round((temp - 32) / 1.8, 1)
    print(f"{temp} °F equals to {celsius} °C")
elif choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")
#  verrataan valintaa ja annetaan oikea tuloste

print("\nProgram ending.")