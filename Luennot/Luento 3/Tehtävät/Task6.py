print("Program starting.\n")

hex = input("Insert a hex color: ")
# pyydetään väri

red = hex[1:3]
green = hex[3:5]
blue = hex[5:7]
# pilkotaan värin hexamuoto punaiseen, vihreään ja siniseen


print(f"\nColors\n- Red {red}\n- Green {green}\n- Blue {blue}")
# tulostetaan värit omille riveille


print("\nProgram ending.")