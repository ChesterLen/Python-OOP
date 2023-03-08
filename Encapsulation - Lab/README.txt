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

    3. Profile
Create a class called Profile. Upon initialization, it should receive:
  · username: str - the username should be between 5 and 15 characters (inclusive). If it is not, raise a ValueError with the message "The username must be between 5 and 15 characters."
  · password: str - the password must be at least 8 characters long; it must contain at least one upper case letter and at least one digit. If it does not, raise a ValueError with the message "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter."
Hint: Use Getters and Setters to name-mangle them.
Override the __str__() method of the base class, so it returns: "You have a profile with username: "{username}" and password: {"*" with the length of password}".