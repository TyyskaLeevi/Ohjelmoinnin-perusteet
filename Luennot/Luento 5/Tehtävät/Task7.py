print("Program starting.\n")
print("Check multiplicative persistence.")

num = int(input("Insert an integer: "))
steps = 0 # muuttuja laskun kierroksille

while num != 0:

    if num < 10:
        break

    while num >= 10: # loopataan niin pitkään että luku on yhden numeron mittainen
        product = 1
        digits = [int(d) for d in str(num)] # muutetaan luku listaksi jossa on sen numerot

        for d in digits:
            product *= d # kerrotaan yksittäiset numerot yhteen

        step_str = " * ".join(str(d) for d in digits) # muutetaan luvun numerot kertolaskuksi stringissä
        print(f"{step_str} = {product}") # tulostetaan tämänhetkinen kierros

        num = product # sijoitetaan tulos muuttujaan seuraavaa kierrosta varten

        steps += 1 # lisätään kierroslaskuriin yksi

    print("No more steps.")
        
    print(f"\nThis program took {steps} step(s)")

print("\nProgram ending.")