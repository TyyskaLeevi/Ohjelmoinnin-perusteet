print("Program starting.")

num = int(input("Insert a positive integer: "))

if num > 0:
    steps = 0 # muuttuja laskun kierroksille
    print(num, end="")

    while num != 1:
        if num % 2 == 0:
            num = num // 2 # jos annettu numero on parillinen jaetaan se kahdella
        else:
            num = 3 * num + 1 # jos se ei ole parillinen kerrotaan kolmella ja lisätään yksi
        print(f" -> {num}", end="")
        steps += 1 # lisätään kierroksiin yksi
    
    print(f"\nSequence had {steps} total steps.")

print("\nProgram ending.")