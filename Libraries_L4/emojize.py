# This script takes user input and converts emoji aliases to actual emojis using the 'emoji' library.

import emoji

emo = input("Input: ")
print(f"{emoji.emojize(emo, language = 'alias')}")