    1. Vehicle
Create a class called Vehicle. Upon initialization, it should receive max_speed (integer, optional; 150 by default) and mileage (number).
Create an instance variable called gadgets - an empty list by default.

    Input: car = Vehicle(20)                     Output: 150
           print(car.max_speed)                          20
           print(car.mileage)                            []
           print(car.gadgets)                  	         ['Hudly Wireless']
           car.gadgets.append('Hudly Wireless')
           print(car.gadgets)

    2. Point
Create a class called Point. Upon initialization, it should receive x and y (numbers). Create 3 instance methods:

- set_x(new_x) - changes the x value of the point

- set_y(new_y) - changes the y value of the point

- __str__() - returns the coordinates of the point in the format "The point has coordinates ({x},{y})"

    Input: p = Point(2, 4)     Output: The point has coordinates (2,4)
           print(p)                    The point has coordinates (3,5)
           p.set_x(3)
	   p.set_y(5)
	   print(p)

    3. Circle
Create a class called Circle. Upon initialization, it should receive a radius (number).
Create a class attribute called pi which should be equal to 3.14. Create 3 instance methods: