print("Program starting.")

print("Insert two integers.")

num1 = int(input("Insert first integer: "))
num2 = int(input("Insert second integer: "))
# pyydetään numerot

print("Comparing inserted integers.")

if(num1>num2):
    print("First integer is greater.")
elif(num1<num2):
    print("Second integer is greater.")
else:
    print("Integers are the same")
# verrataan numeroita, kumpi on isompi vai ovatko yhta suuret

print("\nAdding integers together")

sum = int(num1 + num2)

print(f"{num1} + {num2} = {sum}")
# laketaan yhteen ja tulostetaan laskutoimitus

print("\nChecking the parity of the sum...")

if sum % 2 == 1:
    print("Sum is odd.")
else:
    print("Sum is even.")
# tarkistetaan summan parillisuus jakojäännöksellä ja kerrotaan käyttäjälle

print("Program ending.")