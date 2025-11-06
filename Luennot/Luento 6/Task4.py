def askDimension(PPrompt: str) -> float:
   Feed = float(input(f"Insert {PPrompt}: ")) # käytetään promptia jotta input viestissä voidaan käyttää haluttua sanaa ja muutetaaan input floatiksi
   return Feed

print("Program starting.") # lisätty program starting teksti

Width = askDimension("width") # käytetään molemmissa oikeaa funktiota koska askNumber funktiota ei ollut olemassa
Height = askDimension("height")

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
   Area = PWidth * PHeight # korjattu laskutoimitus
   return Area # korjattu return

Area = calcRectangleArea(Width, Height) # käytetään funktiossa käyttäjältä pyydettyjä arvoja

print("")
print(f"Area is {Area}²") # käytetään f-stringiä
print("Program endeing.") # korjattu lopetus viesti