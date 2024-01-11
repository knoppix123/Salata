from datetime import date
import random

def print_today_date():
    dayselection_list = [1,2,3,4,5,6,7,]
    today = str(date.today())
    last_two_letters = today[-2:]
    last_two_letters = int(last_two_letters)
    order_date = last_two_letters + random.choice(dayselection_list)
    return order_date
    # print(last_two_letters)
