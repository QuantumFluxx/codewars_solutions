def whatday(num):
    days = {1: 'Sunday',
            2: 'Monday',
            3: 'Tuesday',
            4: 'Wednesday',
            5: 'Thursday',
            6: 'Friday',
            7: 'Saturday'}
    return days[num] if 0 < num <=7 else 'Wrong, please enter a number between 1 and 7'