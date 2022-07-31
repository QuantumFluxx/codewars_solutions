def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])