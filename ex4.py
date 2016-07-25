cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

# Calculate the cars that cannot be driven due to absense of driver
cars_not_driven = cars - drivers

# Each driver drives once car
cars_driven = drivers

# The number of people that can be added to a car
carpool_capacity = cars_driven * space_in_a_car

# Average passengers per car
average_passengers_per_car = passengers / cars_driven


# Printing the information we have
print "There are", cars, "cars avaliable."
print "There are only", drivers, "drivers avaliable."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."