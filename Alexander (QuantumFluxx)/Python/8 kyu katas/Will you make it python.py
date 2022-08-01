def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if distance_to_pump <= mpg * fuel_left else False