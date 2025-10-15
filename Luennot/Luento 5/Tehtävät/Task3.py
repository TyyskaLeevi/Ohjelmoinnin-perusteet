print("Program starting.\n")

start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))
num = int(start)
# pyydetään käyttäjältä aloitus- ja lopetusarvot

print("\nstarting while-loop:")

while num <= stop:
    print(num, end=' ')
    num += 1
# kierretään loopissa niin kauan että numero on sama kuin valittu lopetusarvo ja tulostetaan numero samalle riville jokaisessa vaiheessa
 
print("\nProgram ending.")