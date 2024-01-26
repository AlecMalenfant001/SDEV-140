"""This program will find :
the number of uppercase letter
The number of lowercase letters
The number of digits
and The number of whitespace characters
in the file
Alec Malenfant"""
print("Alec Malenfant\n")

#open file
f = open("text.txt", "r")
file = f.read()

def findUpper(file):
    numUpper = 0
    #Take out all of the spaces in the string
    file = file.replace(" ", "")
    #Check if the character is uppercase
    for char in file:
        if char == char.upper():
            numUpper += 1
    return numUpper

def findLower(file):
    numLower = 0
    # Take out all of the spaces in the string
    file = file.replace(" ", "")
    # Check if the character is lowercase
    for char in file:
        if char == char.lower():
            numLower += 1
    return numLower

def findDigit(file):
    numDigit = 0
    #check if the number is a digit
    for char in file:
        if char.isdigit():
            numDigit += 1
    return numDigit

def findWhite(file):
    numWhite = 0
    #check if each character is a whitespace
    for char in file:
        if char.isspace():
            numWhite += 1
    return numWhite

def main(file):
    numUpper = findUpper(file)
    print("number of uppercase characters: " + str(numUpper))
    numLower = findLower(file)
    print("number of lowercase characters: " + str(numLower))
    numDigit = findDigit(file)
    print("number of digits: " + str(numDigit))
    numWhite = findWhite(file)
    print("number of white spaces: " + str(numWhite))

main(file)
f.close()