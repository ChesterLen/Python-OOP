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

    3. Account
Create a class called Account. Upon initialization, it should receive an id (number), a name (string), and a balance (integer; optional; 0 by default). The class should also have 3 additional instance methods:
    • credit(amount) - adds the amount to the balance and returns the new balance
    • debit(amount) - if the amount is less than or equal to the balance, reduces the balance by the amount and returns the new balance. Otherwise, return "Amount exceeded balance"
    • info() - returns "User {name} with account {id} has {balance} balance"

    Test code: account = Account(1234, "George", 1000)     Output: 1500
               print(account.credit(500))                          0
               print(account.debit(1500))                          User George with account 1234 has 0 balance

    Test code: account = Account(5411256, "Peter")         Output: Amount exceeded balance
               print(account.debit(500))                           1000
               print(account.credit(1000))                         500
               print(account.debit(500))                           User Peter with account 5411256 has 500 balance

    4. Pizza Delivery
Create a class called PizzaDelivery. Upon initialization, it should receive a name (string), a price (float), and ingredients (dictionary). The class should also have an instance attribute ordered set to False by default.
You should also create 3 additional instance methods:
    • add_extra(ingredient: str, quantity: int, price_per_quantity: float):
        ◦ If we already have this ingredient in our pizza, increase the ingredient quantity with the given one and update the pizza price by adding the ingredient price for the given quantity
        ◦ If we do not have this ingredient in our pizza, we should add it and update the pizza price
    • remove_ingredient(ingredient: str, quantity: int, price_per_quantity: float):
        ◦ If we do not have this ingredient in our pizza, we should return the following message "Wrong ingredient selected! We do not use {ingredient} in {pizza_name}!"
        ◦ If we have the ingredient, but we try to remove more than we have available, we should return the following message "Please check again the desired quantity of {ingredient}!"
        ◦ Otherwise, remove the given quantity of the ingredient and update the pizza price by removing the ingredient price for the given quantity

    • make_order()
    • Set the attribute ordered to True and return the following message "You've ordered pizza {pizza_name} prepared with {ingredient: quantity} and the price will be {price}lv.". The ingredients should be separated by a comma and a space ", "
    • Keep in mind that once the pizza is ordered, no further changes are allowed. We should return the following message if the customer tries to change it: "Pizza {name} already prepared, and we can't make any changes!"

    Test code: margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})     Output: Wrong ingredient selected! We do not use bacon in Margarita!
	       margarita.add_extra('mozzarella', 1, 0.5)                                            Please check again the desired quantity of tomatoes!
	       margarita.add_extra('cheese', 1, 1)                                                  You've ordered pizza Margarita prepared with cheese: 0, tomatoes: 1, mozzarella: 1 and the price will be 9.5lv.
	       margarita.remove_ingredient('cheese', 1, 1)                                          Pizza Margarita already prepared, and we can't make any changes!
	       print(margarita.remove_ingredient('bacon', 1, 2.5))
	       print(margarita.remove_ingredient('tomatoes', 2, 0.5))
	       margarita.remove_ingredient('cheese', 2, 1)
	       print(margarita.make_order())
	       print(margarita.add_extra('cheese', 1, 1))