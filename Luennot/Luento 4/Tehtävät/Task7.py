print("Program starting.")
print("Testing decision structures.")

num = int(input("Insert an integer: "))

print("Options: " \
"\n1 - In one multi-branched decision" \
"\n2 - In multiple independent if-statements" \
"\n0 - Exit")
# annetaan vaihtoehdot

choice = int(input("Your choice: "))

if choice == 1:
    print("Using one multi-branched decision structure.")

    if num >= 400:
        result = num + 44
    elif 200 <= num < 400:
        result = num + 22
    elif num >= 100:
        result = num + 11
    else:
        result = num
    print(f"Result is {result}")
    # lukuun lisätään eri luku vain silloin kun se osuu oikeaan väliin


elif choice == 2:
    print("Using multiple independent if-statements structure.")

    if num >= 400:
        num += 44
    if num >= 200:
        num += 22
    if num >= 100:
        num += 11
    else:
        result = num
    print(f"Result is {num}")
    # lukuun lisätään eri luku aina silloin kun se on suurempi kuin mitä ehto vaatii


elif choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")
#  verrataan valintaa ja annetaan oikea tuloste

print("\nProgram ending.")