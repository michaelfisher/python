#How many cars are available in total?
cars = 100

#How many seats are available in each car
space_in_a_car = 4.0

#How many people will be driving a car
drivers = 30

#How many people will not be driving, but still need a ride
passengers = 90

#How many cars will not be driven?
cars_not_driven = cars - drivers

#How many cars will be driven?
cars_driven = drivers

#Including drivers, how many people can our system accomodate
carpool_capacity = cars_driven * space_in_a_car

#On average, how many passengers need to ride in each car?
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars."
print "We can transport", carpool_capacity, "total people today."
print "We have", passengers, "passengers to carpool."
print "We need to put about", average_passengers_per_car, "passengers in each car."