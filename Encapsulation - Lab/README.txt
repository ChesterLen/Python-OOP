    1. Person
Create a class called Person. Upon initialization, it should receive a name and an age. Name mangle the name and the age attributes (should not be accessed outside the class).
Create two instance methods called get_name and get_age to return the values of the private attributes

    Test code: person = Person("George", 32)     Output: George
               print(person.get_name())                  32
               print(person.get_age())

    2. Mammal
Create a class called Mammal. Upon initialization, it should receive a name, a type, and a sound. Create a class attribute called kingdom which should not be accessed outside the class and set it to be "animals". Create three more instance methods:
  · make_sound() - returns a string in the format "{name} makes {sound}"
  · get_kingdom() - returns the private kingdom attribute
  · info() - returns a string in the format "{name} is of type {type}"

    Test code: mammal = Mammal("Dog", "Domestic", "Bark")    Output: Dog makes Bark
               print(mammal.make_sound())                            animals
               print(mammal.get_kingdom())                           Dog is of type Domestic
               print(mammal.info())