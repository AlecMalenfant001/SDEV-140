#Alec Malenfant
#This program will output the ammount of money in a compound interest savings account after the user enters in all of the information
print('Student: ALEC MALENFANT\n')


principal = float(input('What is the original deposited principal?: '))
rate = float(input('What is the annual interest rate paid by the account?(as a decimal): '))
compound = float(input('How many times does the interest compound a year?: '))
time = float(input('How many years will the account earn interest?: '))
total = (principal*(1 + rate/compound)**(compound*time))


print('\n After ' + str(compound) + 'years, the account will have $' + str(round(total,2)))
