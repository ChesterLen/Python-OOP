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

    Hero
      Elf
        Museelf
      Wizard
        DarkWizard
        SoulMaster
      Knight
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