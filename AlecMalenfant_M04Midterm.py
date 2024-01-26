"""This program will take all of the inputed words from the user, string them into a sentence
and then count the number of words in the sentence
Alec Malenfant"""
print("Alec Malenfant\n")


def main():
    # Define the variables
    sentence = []
    word = ""
    completeSentence = ""

    #Get the words from the user
    print("Enter every word in the sentence one by one. When finished, enter a period: ")
    while word != ".":
        word = str(input("Enter a word: "))
        #Add the word to a list of words
        sentence.append(word)

    #Make the first word uppercase
    firstWord = sentence[0]
    sentence[0] = firstWord[0].upper() + firstWord[1:len(firstWord)]

    #Turn the list into a string
    for words in sentence:
        completeSentence += (words + " ")

    #Print It
    print(completeSentence)
    print("There are " + str(len(sentence) - 1) + " words in this sentence.")


main()