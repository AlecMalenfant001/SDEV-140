#I have no idea what Rami wanted me to do here
#Alec Malenfant
print("Alec Malenfant")

import random
for roll in range(1,20,1):
    val=random.randint(1,9)
    if val >= 5:
        print("Val: " + str(val))
    else:
        print("val+1: " + str(val+1))
