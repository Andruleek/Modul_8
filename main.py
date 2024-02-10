from datetime import date, timedelta


def get_birthdays_per_week(users):
    """
    Returns a dictionary where keys are days of the week and values are lists of users with birthdays in the next week.
    """
    today = date.today()
    next_week_start = get_next_week_start()
    next_week_end = next_week_start + timedelta(days=7)

    birthdays = {day: [] for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}

    for user in users:
        user_birthday = user['birthday'].replace(year=today.year)
        if today <= user_birthday < next_week_end:
            day_of_week = get_day_of_week(user_birthday)
            if day_of_week in ["Saturday", "Sunday"]:
                day_of_week = "Monday"  # Move weekend birthdays to Monday
            birthdays[day_of_week].append(user['name'])

    next_weekend_birthdays = [user for user in users if next_week_start <= user['birthday'].replace(year=today.year + 1) < next_week_start + timedelta(days=2)]

    for user in next_weekend_birthdays:
        user_birthday = user['birthday'].replace(year=today.year + 1)
        day_of_week = get_day_of_week(user_birthday)
        birthdays[day_of_week].append(user['name'])

    return {day: users for day, users in birthdays.items() if users}


def print_birthday_result(result):
    """
    Prints the result of get_birthdays_per_week function.
    """
    for day, users in result.items():
        if users:
            print(f"On {day}, the following users have birthdays:")
            for user in users:
                print(f"- {user}")
            print()
        else:
            print(f"On {day}, there are no birthdays.\n")


def get_next_week_start():
    """
    Returns the start date of the next week.
    """
    today = date.today()
    return today + timedelta(days=(7 - today.weekday() + 7) % 7)


def get_day_of_week(date_obj):
    """
    Returns the day of the week as a string.
    """
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[date_obj.weekday()]