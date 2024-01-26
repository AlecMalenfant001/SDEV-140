"""This program will ask the user to enter the sales for each day of the week and store it in a list
The program will then add up the sales for the entire week
Alec Malenfant"""
print("Alec Malenfant\n")

#Define the lists and variables
daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weeklySales = []
totalSales = 0

for i in range(7):
    #Ask for the number of sales for each day
    weeklySales.append(float(input("Enter the sales for day " + daysOfWeek[i] + " : $")))
    #Add the daily sales to the weeekly total
    totalSales += float(weeklySales[i])

#Print the results
print("Sales for the week: $" + str(totalSales))