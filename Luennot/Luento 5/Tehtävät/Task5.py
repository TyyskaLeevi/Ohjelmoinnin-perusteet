print("Program starting.\n")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspect = int(input("Insert inspection point: "))
# pyydetään aloitus, lopetus sekä tarkistuspisteet

run = True

print("")
if start >= stop:
    print("Starting point value must be less than the stopping point value.")
    run = False
if inspect > stop or inspect < start:
    print("Inspection value must be within the range of start and stop.\n")
    run = False
# jos annetaan virheelliset inputit annetaan oikea virheilmoitus

if(run):
    print("First loop - inspection with break:")
    for i in range(start, stop):
        if i == inspect:
            break
        if(i == start):
            print(i, end="")
        else:
            print(f" {i}", end="")
# ensimmainen loop joka loppuu kun päästään tarkistuspisteeseen

    
    print("\nSecond loop - inspection with continue:")
    for i in range(start, stop):
        if i == inspect:
            continue
        if(i == start):
            print(i, end="")
        else:
            print(f" {i}", end="")
# toinen loop joka jatkaa laskemista tarkistuspisteen jälkeen


print("\n\nProgram ending.")