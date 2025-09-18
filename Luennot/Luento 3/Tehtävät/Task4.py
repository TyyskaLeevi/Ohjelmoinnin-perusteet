print("Program starting.")

print("Estimate how many minutes you spent on programming... \n")

num1 = int(input("A1_T1: "))
num2 = int(input("A2_T2: "))
num3 = int(input("A3_T3: "))
num4 = int(input("A4_T4: "))
num5 = int(input("A5_T5: "))
num6 = int(input("A6_T6: "))
num7 = int(input("A7_T7: "))
# kysytään ajat tehtäville

total = num1+num2+num3+num4+num5+num6+num7
average = float(total / 7)
# lasketaan ajat yhteen ja lasketaan niiden keskiarvo

print(f"\nIn total you spent {round(total)} minutes on programming.")
# annetaan kokonais aika tehtäville

print(f"Average per task was {round(average, 2)} min and same rounded to the nearest integer {round(average)} min.\n")
# annetaan keskiarvo pyöristettynä kahden desimaalin tarkkuudella sekä lähimpään kokonaislukuun

print("program ending.")