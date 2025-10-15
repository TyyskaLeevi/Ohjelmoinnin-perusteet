print("Program starting.\n")

start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))
# pyydetään käyttäjältä aloitus- ja lopetusarvot

print("\nstarting for-loop:")

for num in range(start, stop +1):
    print(num, end=' ')
# kierretään loopissa niin kauan että numero on sama kuin valittu lopetusarvo ja tulostetaan numero samalle riville jokaisessa vaiheessa

print("\nProgram ending.")