def check_availability(schedule, current_time):
    for time in schedule:
        start, finish = time[0], time[1]
        if int(start[:2]) <= int(current_time[:2]) <= int(finish[:2]) and int(current_time[3:]) < int(finish[3:]):
            return time[1]
    else:
        return True