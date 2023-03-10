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

  project:
    __init__.py
    animal.py:
      reptile.py:
         lizard.py
         snake.py
      mammal.py:
         gorilla.py
         bear.py

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

  project:
       __init__.py
       hero.py:
          elf.py:
            museelf.py
          wizard.py:
            darkwizard.py
            soulmaster.py
          knight.py:
            darkknight.py
            bladeknight.py

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

   project:
       __init__.py
       vehicle.py:
         motorcycle.py:
         racemotorcycle.py
         crossmotorcycle.py
       car.py:
         familycar.py
         sportcar.py

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

    5. Shop
Maria is expanding her business, and today, she is opening a grocery shop. You are hired to write a program that keeps track of the shop's inventory.

   project:
      __init__.py
      drink.py
      food.py
      product.py
      product_repository.py

In the product.py file, the class Product should be implemented. It is a base class for any type of food and drink.
The class should receive name: str, and quantity: int upon initialization. It should also have 3 additional methods:
    • decrease(quantity: int) - decreases the quantity of the product only if there is enough
    • increase(quantity: int) - increases the quantity of the product
    • __repr__() - override the method, so it returns the name of the product 
In the file drink.py, the class Drink should be implemented. The class should inherit from the Product class. An instance of the Drink class will have a name and a quantity of 10.
In the food.py file, the Food class should be implemented. The class should inherit from the Product class. An instance of the Food class will have a name and a quantity of 15.
In the product_repository.py file, the class ProductRepository should be implemented. It is a repository for all products that are delivered to the grocery shop.
The class should have products: list - an empty list, which will be containing all products (objects). Also, the class should have 4 additional methods:
    • add(product: Product) - adds a product to the repository
    • find(product_name: str) - returns a product (object) with that name
    • remove(product_name) - removes a product from the repository
    • __repr__() - override the method, so it returns information for all products in the repository: 
"{product_name1}: {quantity1}"
{product_name2}: {quantity2}
…
{product_nameN}: {quantityN}"