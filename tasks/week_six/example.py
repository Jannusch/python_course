# This file contains the example code from the slides for week six

# First we have to define a class (the blueprint)
# We use the keyword class and then the name of the class

class Car:
    # every class needs a init function. This is the constructor
    # This function is called when we create a new object
    # You can see that we have a parameter called self. This is a reference to the object
    # Every function in a class needs this parameter
    def __init__(self) -> None:
        print("Created a nwe car")

# Now we can create a new object from the class
car1 = Car()
car2 = Car()
car3 = Car()


# We can also add attributes to the class
# We also added a getter method to the class to get the color
class Car:
    def __init__(self, color: str) -> None:
        print("Created a new car")
        self.color = color

    def get_color(self) -> str:
        return self.color

car_blue = Car("blue")
color = car_blue.get_color()
print(f"The color of the car is: {color}")

# This class inherits from the Car class
# This means that it has all the attributes and methods from the Car class
# This is done by adding the name of the class in the parentheses 
class SportCar(Car):
    # we have a init function here as well
    # We have to call the init function from the Car class if we want to use it
    # We do this by calling super().__init__()
    # super() is a reference to the parent class
    def __init__(self, color: str, license: bool):
        super().__init__(color)
        self.license = license

sport_car = SportCar("red", True)


class SportCar(Car):
    # we have a init function here as well
    # We have to call the init function from the Car class if we want to use it
    # We do this by calling super().__init__()
    # super() is a reference to the parent class
    def __init__(self, color: str, license: bool):
        super().__init__(color)
        self.license = license

sport_car = SportCar("red", True)    



# We now add a hp attribute to the SportCar class
# Because we are interested in the comparison of the hp of two cars    
class SportCar(Car):

    def __init__(self, color: str, license: bool, hp: int):
        super().__init__(color)
        self.license = license
        self.hp = hp


sport_car = SportCar("red", True, 200)
sport_car_big = SportCar("yellow", True, 700)

# We can use the hp attribute to compare the two cars
if sport_car.hp > sport_car_big.hp:
    print("The first car is stronger")
elif sport_car.hp < sport_car_big.hp:
        print("The second car is stronger")

# But we also want to compare the cars directly
# We do this by adding the __gt__ method
# This method is called when we use the > operator
class SportCar(Car):

    def __init__(self, color: str, license: bool, hp: int):
        super().__init__(color)
        self.license = license
        self.hp = hp

    def __gt__(self, other):
        return self.hp > other.hp
    
    #  This method allows us to print the object
    # otherwise the object would be printed as <__main__.SportCar object at 0x0000022C6E3F4D60>
    def __str__(self) -> str:
        return f"{self.color} sportCar with {self.hp}hp"
    

sport_car = SportCar("red", True, 200)
sport_car_big = SportCar("yellow", True, 700)

# And now even this works
if sport_car > sport_car_big:
    print("The first car is stronger")
    print(sport_car)
elif sport_car < sport_car_big:
        print("The second car is stronger:")
        print(sport_car_big)

