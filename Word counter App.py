#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     12/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def word_counter(text):
    char_count=len(text)
    word_count=len(text.split())
    sentense_count=text.count('.') + text.count('!') + text.count('?')
    return char_count, word_count,sentense_count

def main():
    print("Welcome to Words Counter App")
    print("Press Enter twice to end")
    print("Enter Your Text")

    user_input=""
    while True:
        line=input()
        if line == "":
            break
        user_input += line +""



    char_count, word_count,sentense_count = word_counter(user_input)

    print("\n----Analysis Result------")
    print(f"Total Charachters: {char_count}")
    print(f"Total Words: {word_count}")
    print(f"Total Sentense: {sentense_count}")

if __name__ == '__main__':
    main()





