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

    5. To-do List
You are tasked to create two classes: a Task class and a Section class. 
    project
      __init__.py
      section.py
      task.py
Create separate files for each class, as shown above. You are tasked to create two classes: a Task class and a Section class.
The Task class should receive a name (string) and a due_date (str) upon initialization. A task also has two attributes: comments (empty list) and completed set to False by default.
The Task class should also have five additional methods:
    • change_name(new_name: str)
        ◦ Changes the name of the task and returns the new name.
        ◦ If the new name is the same as the current name, returns "Name cannot be the same."
    • change_due_date(new_date: str) 
        ◦ Changes the due date of the task and returns the new date.
        ◦ If the new date is the same as the current date, returns "Date cannot be the same."
    • add_comment(comment: str)
        ◦ Adds a comment to the task.
    • edit_comment(comment_number: int, new_comment: str)
        ◦ The comment number value represents the index of the comment we want to edit. The method should change the comment and return all the comments, separated by comma and space (", ")
        ◦ If the comment number is out of range, returns "Cannot find comment."
    • details()
        ◦ Returns the task's details in this format:
"Name: {task_name} - Due Date: {due_date}"
The Section class should receive a name (string) upon initialization. The task also has one instance attribute: tasks (empty list)
The Section class should also have four methods:
    • add_task(new_task: Task)
        ◦ Adds a new task to the collection and returns "Task {task details} is added to the section"
        ◦ If the task is already in the collection, returns "Task is already in the section {section_name}"
    • complete_task(task_name: str) 
        ◦ Changes the task to completed (True) and returns "Completed task {task_name}"
        ◦ If the task is not found, returns "Could not find task with the name {task_name}"
    • clean_section()
        ◦ Removes all the completed tasks and returns "Cleared {amount of removed tasks} tasks."
    • view_section()
        ◦ Returns information about the section and its tasks in this format:
    "Section {section_name}:
     {details of the first task}
     {details of the second task}
     …
     {details of the n task}"

    Test code: task = Task("Make bed", "27/05/2020")                            Output: Go to University
               print(task.change_name("Go to University"))                              28.05.2020
               print(task.change_due_date("28.05.2020"))                                Don't forget laptop and notebook
               task.add_comment("Don't forget laptop")                                  Name: Go to University - Due Date: 28.05.2020
               print(task.edit_comment(0, "Don't forget laptop and notebook"))          Task Name: Go to University - Due Date: 28.05.2020 is added to the section
               print(task.details())                                                    Cleared 0 tasks.
               section = Section("Daily tasks")                                         Section Daily tasks:
               print(section.add_task(task))                                            Name: Go to University - Due Date: 28.05.2020
               second_task = Task("Make bed", "27/05/2020")                             Name: Make bed - Due Date: 27/05/2020
               section.add_task(second_task)
	       print(section.clean_section())
	       print(section.view_section())

    6. Guild System
You are tasked to create two classes: a Player class and a Guild class.
    project
      __init__.py
      guild.py
      player.py
The Player class should receive a name (string), a hp (int), and a mp (int) upon initialization. The Player also has 2 instance attributes: skills (empty dictionary that will contain the skills of each player and its mana cost) and a guild set to "Unaffiliated" by default.
The Player class should also have two additional methods:
    • add_skill(skill_name, mana_cost)
        ◦ Adds the skill and the corresponding mana cost to the dictionary of skills. Returns "Skill {skill_name} added to the collection of the player {player_name}"
        ◦ If the skill is already in the collection, returns "Skill already added"
    • player_info() 
        ◦ Returns the player's information, including their skills, in this format:
"Name: {player_name}
 Guild: {guild_name}
 HP: {hp}
 MP: {mp}
 ==={skill_name_1} - {skill_mana_cost}
 ==={skill_name_2} - {skill_mana_cost}
 …
 ==={skill_name_N} - {skill_mana_cost}"

The Guild class receives a name (string). The Guild should also have one instance attribute players (an empty list which will contain the players of the guild). The class also has 3 additional methods:
    • assign_player(player: Player)
        ◦ Adds the player to the guild and returns "Welcome player {player_name} to the guild {guild_name}". Remember to change the player's guild in the player class.
        ◦ If he is already in the guild, returns "Player {player_name} is already in the guild."
        ◦ If the player is in another guild, returns "Player {player_name} is in another guild."
    • kick_player(player_name: str)
        ◦ Removes the player from the guild and returns "Player {player_name} has been removed from the guild.". Remember to change the player's guild in the player class to "Unaffiliated".
        ◦ If there is no such player in the guild, returns "Player {player_name} is not in the guild."
    • guild_info() 
        ◦ Returns the guild's information, including the players in the guild, in the format:
          "Guild: {guild_name}
          {first_player's info}
          …
          {Nplayer's info}"