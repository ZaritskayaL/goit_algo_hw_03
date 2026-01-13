language = {"name": "Python", "version": 3.11}
print(language)
language["version"] = 3.12
language["year"] =1991
print(language)
del language["year"]
print(language)

# get_days_from_today(date)
from datetime import datetime, timedelta    
def get_days_from_today(date_str):
    try:
        start_date = datetime.strptime(date_str, '%Y-%m-%d')
        return(datetime.today() - start_date)
    except ValueError:
        return None
print(get_days_from_today('2021-10-09'))