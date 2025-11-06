DELIMITER = ","

def collectWords(): # pyydetään käyttäjältä sanoja kunnes syöte on tyhjä
    words = []
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        words.append(word)
    return DELIMITER.join(words)

def analyseWords(words_str): # lasketaan sanojen määrä, merkkien määrä ja sanojen keskipituus
    if not words_str:
        print("- 0 Words\n" \
        "- 0 Characters\n" \
        "- 0.00 Average word length")
        return
    
    words = words_str.split(DELIMITER)
    wordCount = len(words)
    charCount = sum(len(word) for word in words)
    avgLength = charCount / wordCount if wordCount >  0 else 0

    print(f"- {wordCount} Words")
    print(f"- {charCount} Characters")
    print("- {:.2f} Average word length".format(avgLength))


def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")

main()