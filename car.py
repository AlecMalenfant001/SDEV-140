"""This python program will create a class names car that has the year, make and speed. The class will have methods
to increase the speed by 5, decrease the speed by 5, and get the speed
Alec Malenfant"""

class Car:

    #inifialize the attributes
    def __init__(self, year, make):
        self.__year_model = year
        self.__make = make
        self.__speed = 0
    #increase speed by 5
    def accelerate(self):
        self.__speed += 5
    #decrease speed by 5
    def brake(self):
        self.__speed -= 5
    #return speed
    def get_speed(self):
        return 'Current speed:' + str(self.__speed) + ' MPH'
    #print the info for the car
    def __str__(self):
        return 'year: ' + self.__year_model + '\nmake:' + self.__make + "\nspeed: " + str(self.__speed)
