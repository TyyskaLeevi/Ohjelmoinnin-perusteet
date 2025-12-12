def readFile(sourcefile):
    fileHandler = open(sourcefile, 'r')
    content = ''
    row = fileHandler.readline()
    while row != '':
        content += row
        row = fileHandler.readline()
    fileHandler.close()
    return content

def writeFile(PfileContent, Pdestfile):
    filehandle = open(Pdestfile, 'w')
    filehandle.write(PfileContent)
    filehandle.close()
    return None

def main():
    print("Program starting.\n" \
    "This program can copy a file.")
    sourcefile = input("Insert source filename: ")
    destfile = input("Insert destination filename: ")
    fileContent = readFile(sourcefile)
    print(f"Reading file '{sourcefile}' content.")
    print("File content ready in memory.")
    writeFile(fileContent, destfile)
    print(f"Writing content into '{destfile}'.")
    print("Copying operation complete.\n" \
    "Program ending.")
    return None
    
if __name__ == "__main__":
    main()