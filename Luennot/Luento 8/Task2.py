def main():
    print("Program starting.")

    user_input = input("Insert comma separated integers: ")
    items = user_input.split(",")
    
    valid_integers: list[int] = []
    for item in items:
        item = item.strip()
        try:
            number = int(item)
            valid_integers.append(number)
        except ValueError:
            print(f"Invalid value '{item}' detected. ")

    if valid_integers:
        total_count = len(valid_integers)
        total_sum = sum(valid_integers)
        parity = "even" if total_sum % 2 == 0 else "odd"
        print(f"There are {total_count} integers in the list.")
        print(f"Sum of the integers is {total_sum} and it's {parity}")
    else:
        print("No values to analyse.")

    print("Program ending.")


if __name__ == "__main__":
    main()