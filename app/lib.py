def petrol_consumption_in_litre_per_100_km (petrol_filling_in_litre, driving_on_this_petrol):
    """
    >>> petrol_consumption_in_litre_per_100_km (5, 100)
    5.0

    """
    data = petrol_consumption_in_litre_per_100_km
    data = petrol_filling_in_litre / driving_on_this_petrol * 100
    return data
def max_distance_on_this_petrol (petrol_volume, data):
    """
    >>> max_distance_on_this_petrol(10, 5)
    200.0

    """
    result = petrol_volume / data *100
    return result