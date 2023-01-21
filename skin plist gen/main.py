import os
os.system("pip install colorama")
import random, base64, datetime
from colorama import Fore

os.system("cls")
dictionary = {}
skinname_dictionary = {}

success = 0
failed = 0
count = 1001 # to avoid overwriting other skins
skin_names = ["YeetDisDude", "yeetdisdude", "ig: y_etd.sdude", "YeetDisDude#0001", "Subscribe", "cXwbBTz8"]
file = "D:\Folders\coding\py\pg3d\skin pack\dict.txt"
logfile = "D:\Folders\coding\py\pg3d\skin pack\logfile.txt"

while True:
    current_date = datetime.datetime.now().date()
    current_time = datetime.datetime.now().time()
    b64 = input(f"{Fore.LIGHTCYAN_EX}Enter Base64:{Fore.RESET} ")
    if not b64:
        failed += 1
        print(f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} - {Fore.LIGHTRED_EX}The input is blank. Please enter a valid base64 string.\n{Fore.RESET}")
        continue
    if "data:image/png;base64," in b64:
        print(f"{Fore.LIGHTRED_EX}[{Fore.RESET}!{Fore.LIGHTRED_EX}]{Fore.RESET} - prefix found in string, removing...")
        comma_index = b64.index(",")
        b64 = b64[comma_index+1:]
    else:
        1
    try:
        decoded_data = base64.b64decode(b64)
        key = str(count)
        dictionary[key] = b64

        key2 = str(count)
        skinname_dictionary[key2] = random.choice(skin_names)
        count += 1

        success += 1
        print(f"{Fore.LIGHTGREEN_EX}[{Fore.RESET}!{Fore.LIGHTGREEN_EX}]{Fore.RESET} - Saved to dict.txt | Success: {Fore.LIGHTGREEN_EX}{success}{Fore.RESET} | Failed: {Fore.LIGHTRED_EX}{failed}{Fore.RESET}\n")
        with open(logfile, "a") as f:
            f.write(f"\n{current_date} | {current_time} | {b64}")
        with open(file, "w") as f:
            f.write("Plist for skins Base64 'User Skins':\n\n" + "<key>User Skins</key>\n<string>" + str(dictionary) + "</string>\n\n\nPlist for Skin Names 'User Name Skins'\n\n<key>User Name Skins</key>\n<string>" + str(skinname_dictionary) + "</string>")
            f.close()
    except:
        failed += 1
        print(f"{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} - {Fore.LIGHTRED_EX}That string is not a valid base64 encoding.\n{Fore.RESET}")
