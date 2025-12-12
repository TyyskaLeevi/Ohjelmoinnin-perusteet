def main():
    print("Program starting.")
    print("Collect positive integers.")

    numbers: list[int] = []

    while True:
        try:
            user_input = int(input("Insert positive integer(negative stops): "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if user_input < 0:
            break
        elif user_input > 0:
            numbers.append(user_input)
        else:
            print("Zero is not considered a positive integer. Please enter a positive integer.")

    print("Stopped collecting positive integers.")

    if numbers:
        print(f"Displaying {len(numbers)} integers:")
        for index, number in enumerate(numbers):
            ordinal = index + 1
            print(f"- Index {index} => Ordinal {ordinal} => Integer {number}")
    else:
        print("No positive integers were entered.")

    print("Program ending.")

if __name__ == "__main__":
    main()