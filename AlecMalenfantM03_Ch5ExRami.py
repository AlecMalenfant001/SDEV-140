"""This Program will print all the odd and even values by an upper bound limit set by the user
-Alec Malenfant"""
print("Alec Malenfant\n")

min = int(input("Enter the minimum value: "))
max = int(input("Enter the maximum value: "))
global output

if min % 2 == 0: #checks to see if the number is even
    for i in range(min,max,2):
        print("Even Number: " + str(i) + ", Odd Number: " + str(i+1))
    if max % 2 == 0: #Outputs the last number if the loop ended on the second to last number
        print("Even Number: " + str(max))
else:
    for i in range(min, max, 2):
        print("Odd Number: " + str(i) + ", Even Number: " + str(i + 1))
    if max % 2 != 0: #Outputs the last number eif the loop ended on the second to last number
        print("Odd Number: " + str(max))


print("End of Program")

