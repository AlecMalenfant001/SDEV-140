#Alec Malenfant
#This program will give the correct amount of ingredients based on how many cookies the user would like to make
print('Student: ALEC MALENFANT\n')



cookieRatio = float(input('How many cookies would you like to make?: '))/ 48
#The ratio of the desiered ammount of cookies to the number of cookes made by the original recipie

print('Sugar: ' + str(1.5 * cookieRatio) + ' cups')
print('Butter: ' + str(1 * cookieRatio) + ' cups')
print('Flour: ' + str(2.75 * cookieRatio) + ' cups')
