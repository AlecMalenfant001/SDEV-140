"""This program will check to see if a user name was in the top 200 names betwen 2000 and 2009
Alec Malenfant"""
print("Alec Malenfant")

#Define the variables and lists
f_boyNames = open("BoyNames.txt", "r")
f_girlNames = open("GirlNames.txt", "r")

names = []

#put all of the top names into a list
def appendNames():
    #put the top boys names into the names list
    for line in f_boyNames:
        #strip the line of the new line
        line = line.rstrip('\n')
        #append the lowercase name into a list
        names.append(line.lower())

    #do the same thing but with the top girls names
    for line in f_girlNames:
        line = line.rstrip('\n')
        names.append(line.lower())

#ask the user for  a name to check
def askName():
    check = str(input("\nEnter a name to guess: "))
    #make it lowercase to match the list
    check = check.lower()
    checkName(check)

#check if the user entered name is in the list
def checkName(check):
    appended = False
    #Go through each name in the list to see if the item matches the user entered name
    for word in names:
        if check == word:
            print(check + " WAS in the top names from 2000 - 2009")
            appended = True
    #prints if the user entered name did not match anything
    if appended == False:
        print(check + " WAS NOT in the top names from 2000 - 2009")

#ask to run the program again
def again():
    yn = input("Press ENTER to run this program again, type N to quit: ")
    if yn == "":
        main()
    else:
        quit()

def main():
    appendNames()
    askName()
    again()

main()