    1. Person
You are asked to model an application for storing data about people. You should be able to have a Person and a Child. Every person receives name and age upon initialization. Your task is to model the application.
Create a Child class that inherits Person and has the same constructor definition. However, do not copy the code from the Person class - reuse the Person class's constructor.

    Test code: person = Person("Peter", 25)                     Output: Peter
               child = Child("Peter Junior", 5)                         25
               print(person.name)                                       Person
               print(person.age)
               print(child.__class__.__bases__[0].__name__)

    2. Zoo
Create a zoo project that contains the following classes:

    Animal:
      Reptile:
         Lizard
         Snake
      Mammal:
         Gorilla
         Bear

Follow the diagram and create all the classes. Except for the Animal class, each class should inherit from another class, as shown in the diagram. The Animal class should receive a name - string upon initialization.
Every class should have a constructor, which accepts one parameter: name

    Test code: mammal = Mammal("Stella")                        Output: Animal
               print(mammal.__class__.__bases__[0].__name__)            Stella
               print(mammal.name)                                       Reptile
               lizard = Lizard("John")                                  John
               print(lizard.__class__.__bases__[0].__name__)
	       print(lizard.name)

    3. Players and Monsters
Your task is to create the following game hierarchy:

    Hero:
       Elf:
         Museelf
       Wizard:
         DarkWizard
         SoulMaster
       Knight:
         DarkKnight
         BladeKnight

Create a class Hero. It should contain the following attributes:
    • username: string
    • level: int
Override the __str__() method of the base class so it returns: "{name} of type {class_name} has level {level}"

    Test code: hero = Hero("H", 4)                          Output: H
               print(hero.username)                                 4
               print(hero.level)                                    H of type Hero has level 4
               print(str(hero))                                     E of type Elf has level 4
               elf = Elf("E", 4)                                    Hero
               print(str(elf))                                      E
               print(elf.__class__.__bases__[0].__name__)           4
               print(elf.username)
               print(elf.level)

    4. Need for Speed
Create the following hierarchy with the following classes:

    Vehicle:
      Motorcycle:
        RaceMotorcycle
        CrossMotorcycle
      Car:
        FamilyCar
        SportCar

Create a base class Vehicle. It should contain the following attributes:
    • DEFAULT_FUEL_CONSUMPTION: float (constant)
    • fuel_consumption: float - represents the fuel consumption per kilometer
    • fuel: float - represents the quantity of fuel in a specific vehicle
    • horse_power: int
Upon initialization, the class should receive fuel and horse_power. The DEFAULT_FUEL_CONSUMPTION value should be set to the fuel_consumption value. 
Each class should have the following methods:
    • drive(kilometers) - reduces the fuel based on the traveled kilometers and fuel consumption (km * fuel consumption). Keep in mind that you can start driving the vehicle only if you have enough fuel to finish the driving.
The default fuel consumption for the different vehicles is:
    • Vehicle is 1.25
    • SportCar is 10
    • RaceMotorcycle is 8
    • Car is 3

    Test code: vehicle = Vehicle(50, 150)                          Output: 1.25
               print(Vehicle.DEFAULT_FUEL_CONSUMPTION)                     3
               print(FamilyCar.DEFAULT_FUEL_CONSUMPTION)                   50
               print(vehicle.fuel)                                         150
               print(vehicle.horse_power)                                  1.25
               print(vehicle.fuel_consumption)                             50
               vehicle.drive(100)                                          0
               print(vehicle.fuel)                                         0
               family_car = FamilyCar(150, 150)                            Car
               family_car.drive(50)
               print(family_car.fuel)
               family_car.drive(50)
               print(family_car.fuel)
               print(family_car.__class__.__bases__[0].__name__)