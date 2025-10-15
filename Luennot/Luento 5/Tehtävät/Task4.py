print("Program starting.\n")

word = input("Insert word (empty stops): ")
chars = int(len(word))
words = int(0)
# pyydetään ensimmäinen sana ja sijoitetaan sen pituus omaan muuttujaan sekä määritetään words-muuttuja jotta sanojen määrä saadaan laskettua

while word != "":
    # pysytään loopissa niin kauan että käyttäjä antaa tyhjän vastauksen
    word = input("Insert word (empty stops): ") # sijoitetaan aina uusi sana samaan muuttujaan vanhan tilalle
    chars += len(word) # lisätään kirjainten muuttujaan uuden sanan merkkien määrä
    words += 1 # lisätään sanalaskuriin yksi


print(f"\nyou inserted:" \
f"\n- {words} words" \
f"\n- {chars} characters")
# tulostetaan sanojen ja merkkien määrä

print("\nProgram ending.")