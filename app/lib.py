def petrol_consumption_in_litre_per_100_km (petrol_filling_in_litre, driving_on_this_petrol):
    """
    >>>petrol_consumption_in_litre_per_100_km(5, 100)
    5.0

    :param petrol_filling_in_litre:
    :param driving_on_this_petrol:
    :return:
    """
    data = petrol_filling_in_litre / driving_on_this_petrol * 100
    return data
def max_distance_on_this_petrol (petrol_volume, petrol_consumption_in_litre_per_100_km):
    """
    >>> max_distance_on_this_petrol(10, 5)
    200.0

    :param petrol_volume:
    :param petrol_consumption_in_litre_per_100_km:
    :return:
    """
    result = petrol_volume / petrol_consumption_in_litre_per_100_km *100
    return result