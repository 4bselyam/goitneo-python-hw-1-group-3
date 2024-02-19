from collections import defaultdict
from datetime import datetime


def calculate_birthday_this_year(birthday, today):
    birthday_this_year = birthday.replace(year=today.year)
    if birthday_this_year < today:
        birthday_this_year = birthday_this_year.replace(year=today.year + 1)
    return birthday_this_year


def get_weekday_name(birthday_this_year):
    weekday = birthday_this_year.weekday()
    if weekday >= 5:
        return "Monday"
    else:
        return birthday_this_year.strftime("%A")


def get_birthdays_per_week(users):
    today = datetime.today().date()
    birthdays = defaultdict(list)

    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        birthday_this_year = calculate_birthday_this_year(birthday, today)

        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days < 7:
            weekday_name = get_weekday_name(birthday_this_year)
            birthdays[weekday_name].append(name)

    print("\n".join(f"{weekday}: {', '.join(names)}" for weekday, names in birthdays.items()))
