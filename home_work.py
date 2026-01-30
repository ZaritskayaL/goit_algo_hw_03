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

import re
phone_number = ["067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ", 
    ]
def normalize_phone(phone_number: str)-> str:
cleaned = re.sub(r'[^\d+]', '', phone_number)

# вот здесь я запуталась )))
  
print(f'Normalize phone numbers for spam:', normalize_phone)


    