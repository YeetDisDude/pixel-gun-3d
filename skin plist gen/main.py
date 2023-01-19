import random
dictionary = {}
skinname_dictionary = {}

count = 1001 # to avoid overwriting other skins
skin_names = ["YeetDisDude", "yeetdisdude", "ig: y_etd.sdude", "YeetDisDude#0001", "Subscribe", "cXwbBTz8"]
file = "path/dict.txt" # path to where the file will be saved

while True:
    b64 = input("Enter Base64: ")
    key = str(count)
    dictionary[key] = b64

    key2 = str(count)
    skinname_dictionary[key2] = random.choice(skin_names)

    count += 1
    with open(file, "w") as f:
        f.write("Plist for skins Base64 'User Skins':\n" + "<string>" + str(dictionary) + "</string>\n\nPlist for Skin Names 'User Name Skins'\n<string>" + str(skinname_dictionary) + "</string>")
