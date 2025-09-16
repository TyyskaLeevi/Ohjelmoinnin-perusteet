print("Calulate fuel consumption")
feed = input("Enter travel distance(kilometers): ")
Distance = int(feed)

feed = input("Enter fuel usage(liters): ")
FuelUsage = int(feed)

Consumption = (FuelUsage / Distance) * 100
Consumption = int(Consumption)

print("Fuel consumption is", Consumption, "l per 100 km")