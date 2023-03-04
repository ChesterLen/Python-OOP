    1. Vet
Create a class called Vet. Upon initialization, it should receive a name (string). It should also have an instance attribute called animals (empty list by default).
There should also be 2 class attributes: animals (empty list) which will store the total amount of animals for all vets; and space (5 by default). You should create 3 additional instance methods:
    • register_animal(animal_name)
        ◦ If there is space in the vet clinic, adds the animal to both animals' lists and returns a message: "{name} registered in the clinic"
        ◦ Otherwise, returns "Not enough space"
    • unregister_animal(animal_name)
        ◦ If the animal is in the clinic, removes it from both animals' lists and returns "{animal} unregistered successfully"
        ◦ Otherwise, returns "{animal} not in the clinic"
    • info()
    • Returns info about the vet, the number of animals in his list and the free space in the clinic:
"{vet_name} has {number_animals} animals. {space_left_in_clinic} space left in clinic"

    Test code: peter = Vet("Peter")                      Output: Tom registered in the clinic
               george = Vet("George")                            Cory registered in the clinic
               print(peter.register_animal("Tom"))               Fishy registered in the clinic
               print(george.register_animal("Cory"))             Bobby registered in the clinic
               print(peter.register_animal("Fishy"))             Kay registered in the clinic
               print(peter.register_animal("Bobby"))             Cory unregistered successfully
               print(george.register_animal("Kay"))              Silky registered in the clinic
               print(george.unregister_animal("Cory"))           Molly not in the clinic
               print(peter.register_animal("Silky"))             Tom unregistered successfully
               print(peter.unregister_animal("Molly"))           Peter has 3 animals. 1 space left in clinic
               print(peter.unregister_animal("Tom"))             George has 1 animals. 1 space left in clinic
               print(peter.info())
	       print(george.info())

    2. Time
Create a class called Time. Upon initialization, it should receive hours, minutes, and seconds (integers).
The class should also have class attributes max_hours equal to 23, max_minutes equal to 59, and max_seconds equal to 59. You should also create 3 additional instance methods:
    • set_time(hours, minutes, seconds) - updates the time with the new values
    • get_time() - returns "{hh}:{mm}:{ss}"
    • next_second() - updates the time with one second (use the class attributes for validation) and returns the new time (use the get_time() method)

    Test code: time = Time(9, 30, 59)       Output: 09:31:00
               print(time.next_second())

    Test code: time = Time(10, 59, 59)      Output: 11:00:00
               print(time.next_second())

    Test code: time = Time(23, 59, 59)      Output: 00:00:00
               00:00:00