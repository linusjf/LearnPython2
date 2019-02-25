# Assignimg cars
cars = 100
# space in car is 4, not 5.Small cars?
space_in_a_car = 4.0
# Drivers, not chauffeurs. Passenger as well.
drivers = 30
# Assigning passengers
passengers = 90
# As many cars on road as drivers. Only 
# one per vehicle.
cars_not_driven = cars - drivers
cars_driven = drivers
# Car pooling? Where's the meeting place?
# Car park for car poolers required.
carpool_capacity = cars_driven * space_in_a_car
# Avg passengers per car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
