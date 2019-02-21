from app.lib import petrol_consumption_in_litre_per_100_km, max_distance_on_this_petrol

petrol_filling_in_litre = int (input('Сколько бензина заправили? '))
print(petrol_filling_in_litre)
print(type(petrol_filling_in_litre))

driving_on_this_petrol = int (input('Сколько проехали после заправки? '))
print (driving_on_this_petrol)
print (type (driving_on_this_petrol))

petrol_consumption_in_litre_per_100_km (petrol_filling_in_litre, driving_on_this_petrol)
value = petrol_filling_in_litre / driving_on_this_petrol * 100
print(value)
print(petrol_consumption_in_litre_per_100_km)

petrol_volume = int (input('Сколько залили в бак потом? '))
print(petrol_volume)
print(type(petrol_volume))

max_distance_on_this_petrol (petrol_volume, petrol_consumption_in_litre_per_100_km)
value= petrol_volume / petrol_consumption_in_litre_per_100_km
print(value)
print(max_distance_on_this_petrol)