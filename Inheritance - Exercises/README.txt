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