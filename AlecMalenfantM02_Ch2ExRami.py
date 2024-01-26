#Alec Malenfant
#This Program will find the normal and overtime wages based on the number of hours and wage provided by the user
print("Alec Malenfant\n")



numHours = int(input("Enter the number of hours worked: "))
payRate = float(input("Enter the Pay Rate per Hour: "))
overtimePay = payRate * 1.5

if numHours > 40:
    netPay = (40 * payRate) + ((numHours - 40) * overtimePay)
    print(numHours - 40)
else:
    netPay = numHours * payRate


print("Your pay is: " + str(netPay))
    


input()