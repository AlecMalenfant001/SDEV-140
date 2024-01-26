# Program: Class-C Subnet Calculator
# Author: Alec Malenfant
print("Alec Malenfant\n")

def printNetworkPortionOneBit(IP_Address):
    networkPortion = ""
    numOfDots = 0
    for x in range(len(IP_Address)):
        if IP_Address[x] == "." and int(numOfDots) == 2:
            break
        else:
            networkPortion = networkPortion + IP_Address[x]  #192.168.1.99
            if IP_Address[x] == ".":
                numOfDots = int(numOfDots) + 1

    # Print 4 subnets
    b7 = 64
    borrowedSubnetBits = 2  # borrowed 2 subnet bits
    subnetMask = 24  # Class C subnet Mask = /24
    prefix = int(borrowedSubnetBits) + int(subnetMask)  # prefix=/24+2=/26

    totalSizeOfSubnet = 2 ** (32 - prefix)

    for x in range(2):
        # if x == 0 and y == 0:
        #b8Val = int(b8) * int(x)  # b8Val = 128 MSB, borrow from left to right
        b7Val = int(b7)   # b7Val = 64 borrow from left to right
        totalBitVal = b7Val
        # print(str(x) + str(y) + ": " + networkPortion + "." + str(totalBitVal), sep="",end="\n")
        print(str(x)  + ": ", sep="", end="\n")
        # For Each Subnet, Print NA,FHA,LHA,BA
        subnetID = totalBitVal
        FHA = subnetID + 1
        BA = (subnetID + totalSizeOfSubnet) - 1
        LHA = BA - 1
        print("NA : " + networkPortion + "." + str(subnetID))
        print("FHA: " + networkPortion + "." + str(FHA))
        print("LHA: " + networkPortion + "." + str(LHA))
        print("BA : " + networkPortion + "." + str(BA))
        print("\n\n")

def calculateSubnet(borrowedBits,IP_Address):
    if int(borrowedBits) == 1:
        #Display NA,BA,FHA,LHA
        print("Ok")
        printNetworkPortionOneBit(IP_Address)
 
    elif int(borrowedBits) == 2:
        #Display NA,BA,FHA,LHA
        print("Bit = 2")
    elif int(borrowedBits) == 3:
        #Display NA,BA,FHA,LHA
        print("Bit = 3")
    elif int(borrowedBits) == 4:
        #Display NA,BA,FHA,LHA
        print("Bit = 4")
    elif int(borrowedBits) == 5:
        #Display NA,BA,FHA,LHA
        print("Bit = 5")
    elif int(borrowedBits) == 6:
        #Display NA,BA,FHA,LHA
        print("Bit = 6")
    else:
        print("Something")
        #Say something.
        
answer = "y"
while answer == "y":
    octet = ""    
    ip = input("Enter a class-C IP Address, Ex: 192.168.1.0 \n")
    for x in range(len(ip)):
        if ip[x] == ".":
            break
        else:
            octet = octet + ip[x]
    # Testing to see if the IP Address is class-C 
    if (int(octet) < 192) or (int(octet) > 223):
        print("Invalid Class-C IP Address: ")
        print("Your First Octect Value must be [192-223],Try again: ")
        
    else:
        print("You Entered a Valid Class-C IP Address: " + ip)
        #   Calculating how many bits to borrow
        numOfSubnet = int(input("How many subnets to create: "))   
        
        if numOfSubnet <= 2:    # if you borrow 1 bit then you got 2^1 = 2 subnets
            print("You will borrow 1 subnet bit: ")
            print("2^1 = 2 subnets")
            x=1
            calculateSubnet(x,ip)
        else:
            print("Invalid number of borrowed Bits\n"
                  "This program can oly ")
            print("Class-C: Max number of borrowed bits is 6")
            print("Class-C: Max number of Subnets is 64")

    
    answer = input("Continue(y)es/(n)0): ")
    
print("End of Program")

