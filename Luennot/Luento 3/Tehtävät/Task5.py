print("Program starting.")

word = input("\nInsert a closed compound word: ")
# pyydetään sana

print(f"The word you inserted is '{word}' and in reverse it is '{word[::-1]}'.")
print(f"The inserted word length is {len(word)}")
print(f"Last character is '{(word[-1])}'\n")
# annetaan sana normaalisti ja takaperin sekä sanan pituus ja viimeinen merkki

print(f"Take substring from the inserted word by inserting...")
start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))
# pyydetään komentoja jotta saadaan luotua substring

substring = (word[start:end:step])
# luodaan substring käyttämällä annettuja komentoja

print(f"\nThe word '{word}' sliced to the defined substring is '{substring}'.")
# annetaan substring käyttäjälle


print("Program ending.")