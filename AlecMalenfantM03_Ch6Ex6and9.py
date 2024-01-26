#This program will read the integers from numbers.txt and calculate the average of all the numbers in the file
#This program will also handle any IoError and ValueError
#Alec Malenfant
print('Alec Malenfant\n')


global total
global count
total = 0
count = 0


try:
    #Open the file
    file = open('numbers.txt', 'r')

    #Read every line in the file and add it to the total
    for line in file :
        total += int(line)
        count += 1

    #close the file
    file.close()
    #find the average and print it
    total /= count
    print('The average is: ' + str(total))

#Make sure there are no errors
except ValueError:
    print('ERROR!: There was an error reading the data in the file')
except IOError:
    print('ERROR! An error has occured reading the file')
