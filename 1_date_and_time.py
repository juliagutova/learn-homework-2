"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta
def print_days():
    
    dt_now = datetime.now()
    delta1 = timedelta(days=1)
    delta30 = timedelta(days=30)
    yesterday = dt_now - delta1
    month_ago = dt_now - delta30
    print(yesterday, dt_now, month_ago)


def str_2_datetime(date_string):
   date_string = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
