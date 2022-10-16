from datetime import datetime

def is_today(date): 
    return date.strftime('%Y.%m.%d') == datetime.now().strftime('%Y.%m.%d')