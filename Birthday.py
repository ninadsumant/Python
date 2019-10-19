from datetime import datetime
class birthday:
    def get_user_birthday():
        year = int(input('When is your birthday? [YYYY] '))
        month = int(input('When is your birthday? [MM] '))
        day = int(input('When is your birthday? [DD] '))

        birthday = datetime(year,month,day)
        return birthday

    def calculate_dates(original_date, now):
        delta1 = datetime(now.year, original_date.month, original_date.day)
        delta2 = datetime(now.year+1, original_date.month, original_date.day)
        days = (max(delta1, delta2) - now).days
        # alternatively:
        # days = max(delta1, delta2).total_seconds() / 60 / 60 /24

        return days

bd = birthday.get_user_birthday()
now = datetime.now()
c = birthday.calculate_dates(bd, now)

print(c)



















# from datetime import date

# year = int(input('Enter a year'))
# month = int(input('Enter a month'))
# day = int(input('Enter a day'))
# date1 = date(year, month, day)
# def calculate_age(dtob):
#     today = date.today()
#     return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))
# print()
# print(calculate_age(date1))
# # print(calculate_age(date(1989,1,12)))
