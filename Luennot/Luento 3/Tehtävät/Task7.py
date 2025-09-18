print("Program starting.")

fahrenheit = float(input("Insert fahrenheits: "))
celcius = float((fahrenheit-32)/1.8)
# pyydetään fahrenheit ja lasketaan mitä se on celciuksissa

print(f"{fahrenheit}°F is {round(celcius, 2)}°C")
# tulostetaan molemmissa mittayksiköissä, celcius pyöristettynä kahteen desimaaliin

print("Program ending.")