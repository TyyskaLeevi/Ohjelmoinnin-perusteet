print("Program starting.")

name = input ("What is your name: ")
# pyydetään nimi

num1 = input ("Enter a floating point number: ")
num1 = float(num1)
# pyydetään ensimmäinen numero ja sijoitetaan se num1 muuttujaan

num2 = input ("Enter second floating point number: ")
num2 = float(num2)
# pyydetään toinen numero ja sijoitetaan se num2 muuttujaan


print(name, "you gave numbers", num1, "and", num2)
# kerrotaan käyttäjälle hänen valitsemansa numerot

num3 = num1 * num2
# kerrotaan numerot yheen ja sijoitetaan tulo num3 muuttujaan
product = round(num3, 2)
# ja pyöristetään tulos kahden desimaalin tarkkuudella ja sijoitetaan tulos product muuttujaan

print("Multiplying first and second number will result in product", product)
# annetaan vastaus käyttäjälle

print("program ending.")