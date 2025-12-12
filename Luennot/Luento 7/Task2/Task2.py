def writeFile(Pfilename, Pcontent):
    filehandle = open(Pfilename, 'w')
    filehandle.write(Pcontent)
    filehandle.close()
    return None

def main():
    print("Program starting.")
    firstname = input("insert first name: ")
    lastname = input("insert first name: ")
    filename = input("insert filename: ")
    content = "{}\n{}\n".format(firstname,lastname)
    writeFile(filename, content)
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()