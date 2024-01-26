#Alec Malenfant
#This Program will calculate the state and county sales tax from a user entered total
print('Alec Malenfant\n')

subTotal = float(input('What was your subtotal?: $'))

stateTax = subTotal * .05
countyTax = subTotal *.025
total = str(round((subTotal + stateTax + countyTax),2))
print('\nSub Total: $' + str(subTotal))
print('Sate Tax: $' + str(stateTax))
print('County Tax: $' + str(countyTax))
print('Total: $' + total)
