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
    print("4: Spell Check Alice In Wonderland (Binary Search)")
    print("5: Exit")
    return input("\nEnter memu selection (1-5):")

# Call main() to begin program
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
            binarySearchWord(dictionary)
        elif selection == "3":
            linearSearchWord(aliceWords,dictionary)
        elif selection == "4":
            binarySearchWord(aliceWords,dictionary)
        elif selection == "5":
            break




 

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

def linearSearchWord(aliceWords,dictionary):
    count = 0
    for word in aliceWords:
        index = linearSearch(dictionary,word.lower())
        if index == -1:
            count += 1
    print(count)

def binarySearch(anArray, item):
    # LI = Lower Index
    LI = 0
    UI = len(anArray) - 1
   
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

def binarySearchWord(aliceWords,dictionary):
    count = 0
    for word in aliceWords:
        index = binarySearch(dictionary,word.lower())
        if index == -1:
            count += 1
    print(count)

def binarySearchWord (dictionary):
        input_Word = input("Enter a single word: ")
        index = binarySearch(dictionary, input_Word.lower())
        if index == -1:
            print(f"-{input_Word}- is not found.")
        else:
            print(f"-{input_Word}- is found at position {index}")


# end main()
main()