# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression

def getMenuSelection():
    print("\nMain Menu")
    print("1: Spell Check a Wrod(Linear Search)")
    print("2: Spell Chack a Word(Binary Search)")
    print("3: Spell Check Alice In Wonderland(Linear Search)")
    print("5: Exit")
    return input("\nEnter memu selection (1-5):")

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    while True:
        # Get Menu Selection & Do Stuff
        selection = getMenuSelection()

        if selection == "1":
            linearSearchWord(dictionary)
        elif selection == "2":
            binarySearch(dictionary)
        elif selection == "5":
            break


# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


def linearSearchWord(dictionary):
    # Search the dictionary for a user provided word
    input_Word = input("Enter a single word: ")
    index = linearSearch(dictionary, input_Word.lower())
    if index == -1:
        print(f"{input_Word} not found.")
    else:
        print(f"{input_Word} found at position: {index}")


def linearSearch(anArray, item):
    for i in range(len(anArray)):
        if item == anArray[i]:
            return i
    return -1

def binarySearch(anArray, item):
    # LI = Lower Index
    LI = 0
    UI = len(anArray) - 1
    input_Word = input("Enter a single word: ")
    index = binarySearch(dictionary, input_Word.lower())
    while LI <= UI:
        # MI = Middle Index
        MI = (LI + UI)//2
        if item == anArray[MI]:
            return MI
        else:
            if anArray[MI] < item:
                LI = MI +1
            else:
                UI = MI -1
    return -1



# Call main() to begin program
main()
