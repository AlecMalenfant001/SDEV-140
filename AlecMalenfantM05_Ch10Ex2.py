"""The program will increase the speed 5 times and then get the speed after each acceleration
The program will then do the same thing with decreasing the speed
Alec Malenfant"""
print("Alec Malenfant\n")
#import the program that deines the car class
import car

def main():
    #create object
    ford = car.Car("2002", "Ford")
    #Accelerte 5 times
    for i in range(1,5):
        ford.accelerate()
        print(ford.get_speed())
    #Brake 5 times
    for i in range(1,5):
        ford.brake()
        print(ford.get_speed())

main()