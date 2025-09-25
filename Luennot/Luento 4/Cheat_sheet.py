# print("Welcome to the temp app!")
# temp = int(input("What is the temperature of CPU? "))

# if(temp > 80):
#     print("Warning, temperature too high!")
# else:
#     print("All cool, keep on going!")


# num = int(input("anna numero: "))

# if num % 2 == 1:
#     print("pariton")
# else:
#     print("parillinen")

# if(temp > 80):
#     if(temp > 90):
#         print("you are toast")
#     else:
#         print("Warning")
# else:
#     print("you are ok")

# if(temp > 90):
#     print("you are toast")
# elif(temp > 80):
#     print("warning")
# else:
#     print("you are ok")


# nimi1 = input("anna nimi: ")
# nimi2 = input("anna toinen nimi: ")


# if len(nimi1) > len(nimi2):
#     print("eka on pidempi")
# elif(len(nimi1) < len(nimi2)):
#     print("toka on pidempi")
# else:
#     print("saman pituiset")

# town = "lahti"
# street = "mukkulankatu"
# building = 19

# if(town == "lahti" and street == "mukkulankatu" and building == 19):
#     print("you are at LAB")
# elif(town == "lahti" and (street != "mukkulankatu" or building != 19)):
#     print("you are in the correct town but check the street address again")
# elif not(town == "lahti" and street == "mukkulankatu" and building == 19):
#     print("you are completely lost...")

import random

# print(random.random()) antaa luvun 0-1
# print(random.randint(1, 10))

ksp = int(input("kivi1 sakset2 paperi3: "))
kps = random.randint(1, 3)
print(kps)

if ksp == kps:
    print("tasapeli")
elif (ksp == 1 and kps == 2) or (ksp == 2 and kps == 3) or (ksp == 3 and kps == 1):
    print("pelaaja voitti")
else:
    print("kone voitti")