# language = {"name": "Python", "version": 3.11}
# print(language)
# language["version"] = 3.12
# language["year"] =1991
# print(language)
# del language["year"]
# print(language)

# get_days_from_today(date)
from datetime import datetime, timedelta    
def get_days_from_today(date_str):
    try:
        start_date = datetime.strptime(date_str, '%Y-%m-%d')
        return(datetime.today() - start_date)
    except ValueError:
        return None
print(get_days_from_today('2021-10-09'))

#get_numbers_tickets(min, max, quantity)
import random
def get_numbers_tickets(min, max, quantity):
    if quantity > (max - min + 1):
        raise ValueError("Quantity exceeds the range of unique numbers available.")
    
    return random.sample(range(min, max + 1), quantity)

lottery_ticket = get_numbers_tickets(1, 36, 5)
print(f"Lottery ticket numbers: {lottery_ticket}")

# normalize_phone(phone_number)
# import re
# def normalize_phone(phone_number):
#     phone_number = re.