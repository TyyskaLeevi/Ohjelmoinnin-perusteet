def readFile(fileName):
    fileHandler = open(fileName, 'r')
    content = ''
    row = fileHandler.readline()
    while row != '':
        content += row
        row = fileHandler.readline()
    fileHandler.close()
    return content # palaa kutsukohtaan

def main():
    print("Program starting.\n"
    "This program can read a file.")
    fileName = input("Insert filename: ")
    fileContent = readFile(fileName) # hyppää readFile funktioon
    print(f"#### START {fileName} ####")
    print(f"{fileContent}")
    print(f"#### END {fileName} ####")
    print("Program ending.")


if __name__ == "__main__":
    main()