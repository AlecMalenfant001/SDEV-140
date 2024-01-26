"""this program will return a sentence that the user ented with the first letter of each word capitolized
Alec Malenfant"""
print("Alec Malenfant\n ")


def capitolize(string):
    #Put each word into a item in a list
    wordList = string.split()
    #Define variables needed
    sentence = ""
    count = 0
    #replace each word in the list with itself but with the first letter capital
    for word in wordList:
        word = (word.upper()[0] + word.lower()[1:-1])
        wordList[count] = word
        count +=1
    #put each word back into a sentence
    for word in wordList:
        sentence += (word + " ")
    print(sentence)

#Main
string = str(input("Please enter a sentence: "))
capitolize(string)