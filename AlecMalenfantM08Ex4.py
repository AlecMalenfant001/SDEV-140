# Program: Class-C Subnet Calculator
# Author: Alec Malenfant
print("Alec Malenfant")

def printNetworkPortion1Bit(IP_Address):
    networkPortion = ""
    numOfDots = 0
    for x in range(len(IP_Address)):
        if IP_Address[x] == "." and int(numOfDots) == 2:
            break
        else:
            networkPortion = networkPortion + IP_Address[x]  # 192.168.1.99
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
        # b8Val = int(b8) * int(x)  # b8Val = 128 MSB, borrow from left to right
        b7Val = int(b7)  # b7Val = 64 borrow from left to right
        totalBitVal = b7Val
        # print(str(x) + str(y) + ": " + networkPortion + "." + str(totalBitVal), sep="",end="\n")
        print(str(x) + ": ", sep="", end="\n")
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


def printNetworkPortion2Bit(IP_Address):
    networkPortion = ""
    numOfDots = 0
    for x in range(len(IP_Address)):    # Read the first 3 Octects from an IP Address
        if IP_Address[x] == "." and int(numOfDots) == 2:
            break
        else:
            networkPortion = networkPortion + IP_Address[x]  #192.168.1.99
            if IP_Address[x] == ".":
                numOfDots = int(numOfDots) + 1  

    # Print 4 subnets
    b8 = 128
    b7 = 64
    borrowedSubnetBits = 2  # borrowed 2 subnet bits
    subnetMask = 24         # Class C subnet Mask = /24
    prefix = int(borrowedSubnetBits) + int(subnetMask)  #prefix=/24+2=/26
    
    totalSizeOfSubnet = 2**(32 - prefix)
    
    for x in range(2):
        for y in range(2):
            #if x == 0 and y == 0:
            b8Val = int(b8) * int(x) #b8Val = 128 MSB, borrow from left to right
            b7Val = int(b7) * int(y) #b7Val = 64 borrow from left to right
            totalBitVal = b8Val + b7Val
            #print(str(x) + str(y) + ": " + networkPortion + "." + str(totalBitVal), sep="",end="\n")
            print(str(x) + str(y) + ": ", sep="",end="\n")
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
            
#========
def printNetworkPortion3Bit(IP_Address):
    networkPortion = ""
    numOfDots = 0
    for x in range(len(IP_Address)):    # Read the first 3 Octects from an IP Address
        if IP_Address[x] == "." and int(numOfDots) == 2:
            break
        else:
            networkPortion = networkPortion + IP_Address[x]  #192.168.1.99
            if IP_Address[x] == ".":
                numOfDots = int(numOfDots) + 1  

    # Print 8 subnets
    b8 = 128
    b7 = 64
    b6 = 32
    borrowedSubnetBits = 3  # borrowed 3 subnet bits
    subnetMask = 24         # Class C subnet Mask = /24
    prefix = int(borrowedSubnetBits) + int(subnetMask)  #prefix=/24+3=/27
    
    totalSizeOfSubnet = 2**(32 - prefix)
    
    for x in range(2):
        for y in range(2):
            for z in range(2):
                b8Val = int(b8) * int(x) #b8Val = 128 MSB, borrow from left to right
                b7Val = int(b7) * int(y) #b7Val = 64 borrow from left to right
                b6Val = int(b6) * int(z) #b6Val = 32 borrow from left to right
                
                totalBitVal = b8Val + b7Val + b6Val                
                print(str(x) + str(y) + str(z) + ": ", sep="",end="\n")
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

            
#========

def printNetworkPortion4Bit(IP_Address):
    networkPortion = ""
    numOfDots = 0
    for x in range(len(IP_Address)):  # Read the first 3 Octects from an IP Address
        if IP_Address[x] == "." and int(numOfDots) == 2:
            break
        else:
            networkPortion = networkPortion + IP_Address[x]  # 192.168.1.99
            if IP_Address[x] == ".":
                numOfDots = int(numOfDots) + 1

                # Print 8 subnets
    b8 = 128
    b7 = 64
    b6 = 32
    b5 = 16
    borrowedSubnetBits = 3  # borrowed 3 subnet bits
    subnetMask = 24  # Class C subnet Mask = /24
    prefix = int(borrowedSubnetBits) + int(subnetMask)  # prefix=/24+3=/27

    totalSizeOfSubnet = 2 ** (32 - prefix)

    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    b8Val = int(b8) * int(x)  # b8Val = 128 MSB, borrow from left to right
                    b7Val = int(b7) * int(y)  # b7Val = 64 borrow from left to right
                    b6Val = int(b6) * int(z)  # b6Val = 32 borrow from left to right
                    b5Val = int(b5) * int(w)  # b6Val = 32 borrow from left to right

                    totalBitVal = b8Val + b7Val + b6Val
                    print(str(x) + str(y) + str(z) + str(w) + ": ", sep="", end="\n")
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
    if int(borrowedBits) == 1:              #Done
        #Display NA,BA,FHA,LHA
        print("1 borrowed bit:\n")
        printNetworkPortion1Bit(IP_Address)
 
    elif int(borrowedBits) == 2:            #Done
        #Display NA,BA,FHA,LHA
        print("2 borrowed bit:\n")
        printNetworkPortion2Bit(IP_Address)

        
    elif int(borrowedBits) == 3:            #Here
        #Display NA,BA,FHA,LHA
        print("3 borrowed bit:\n")
        printNetworkPortion3Bit(IP_Address)
        
    elif int(borrowedBits) == 4:
        #Display NA,BA,FHA,LHA
        print("4 borrowed bit:\n")
        printNetworkPortion4Bit(IP_Address)
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
    for x in range(len(ip)): # Read first Octect only
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
            x=1 # Number of Borrowed bits
            calculateSubnet(x,ip)
            #Print New Subnet Mask /25
            print("New Subnet Mask: 255.255.255.128")
            numOfHostBits = 8 - int(x)
            numOfUsableHostsPerSubnet = (2**numOfHostBits) - 2
            print("Number of usuable hosts per subnet is: " + str(numOfUsableHostsPerSubnet) )
            
        elif numOfSubnet <= 4:  # if you borrow 2 bit then you got 2^2 = 4 subnets
            print("You will borrow 2 subnets bits: ")
            print("2^2 = 4 subnets")
            x=2
            calculateSubnet(x,ip)
            #Print New Subnet Mask /26
            print("New Subnet Mask: 255.255.255.192")
            numOfHostBits = 8 - int(x)
            numOfUsableHostsPerSubnet = (2**numOfHostBits) - 2
            print("Number of usuable hosts per subnet is: " + str(numOfUsableHostsPerSubnet) )
            
        elif numOfSubnet <= 8:  # if you borrow 3 bit then you got 2^3 = 8 subnets
            print("You will borrow 3 subnets bits: ")
            print("2^3 = 8 subnets")
            x=3
            calculateSubnet(x,ip)
            #Print New Subnet Mask /27
            print("New Subnet Mask: 255.255.255.224")
            numOfHostBits = 8 - int(x)
            numOfUsableHostsPerSubnet = (2**numOfHostBits) - 2
            print("Number of usuable hosts per subnet is: " + str(numOfUsableHostsPerSubnet) )

            
        elif numOfSubnet <= 16:
            print("You will borrow 4 subnets bit: ")
            print("2^4 = 16 subnets")
            x = 4
            calculateSubnet(x, ip)
            # Print New Subnet Mask /27
            print("New Subnet Mask: 255.255.255.224")
            numOfHostBits = 8 - int(x)
            numOfUsableHostsPerSubnet = (2 ** numOfHostBits) - 2
            print("Number of usuable hosts per subnet is: " + str(numOfUsableHostsPerSubnet))
        elif numOfSubnet <= 32:
            print("You will borrow 5 subnets bit: ")
            print("2^5 = 32 subnets")
        elif numOfSubnet <= 64:
            print("You will borrow 6 subnets bit: ")
            print("2^6 = 64 subnets")
        else:
            print("Invalid number of borrowed Bits")
            print("Class-C: Max number of borrowed bits is 6")
            print("Class-C: Max number of Subnets is 64")

    
    answer = input("Continue(y)es/(n)0): ")
    
print("End of Program")

