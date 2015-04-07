__author__ = 'Nando'
# Exercise 4: Variables and names
# http://learnpythonthehardway.org/book/ex4.html

cars = 100 #Total amount of cars avilable
space_in_a_car = 4.0 #How many people can sit in a car?
drivers = 30 #Total amount of drivers
passengers = 90 #Total amount of passengers
cars_not_driven = cars - drivers #Cars without a driver
cars_driven = drivers #Cars with a driver
carpool_capacity = cars_driven * space_in_a_car #Total capacity of the car pool
average_passengers_per_car = passengers / cars_not_driven #Passengers per car on average

print ("There are ", cars, " cars available.")
print ("There are only ", drivers, " drivers available.")
print ("There will be ", cars_not_driven, " empty cars today.")
print ("We can transport ", carpool_capacity, " people today.")
print ("We have ", passengers, " to carpool today.")
print ("We need to put about ", average_passengers_per_car, " in each car.")

#Study Drills
#space_in_a_car: no need to be setted in floating point...