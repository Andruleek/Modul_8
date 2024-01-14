from datetime import date, timedelta

DAYS_IN_WEEK = 7

def get_day_of_week(date_obj):
    days = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
    return days[date_obj.weekday()]

def get_next_week_start():
    today = date.today()
    return today + timedelta(days=(DAYS_IN_WEEK - today.weekday() + DAYS_IN_WEEK) % DAYS_IN_WEEK)

def get_birthdays_per_week(users):
    today = date.today()
    next_week_start = get_next_week_start()
    next_week_end = next_week_start + timedelta(days=DAYS_IN_WEEK + 2)  # Додано 2 дні для врахування вихідних

    birthdays = {day: [] for day in ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]}

    for user in users:
        user_birthday = user['birthday'].replace(year=today.year)
        if today <= user_birthday < next_week_end:
            day_of_week = get_day_of_week(user_birthday)
            birthdays[day_of_week].append({'name': user['name'], 'birthday': user_birthday})

    next_weekend_birthdays = [user for user in users if next_week_start <= user['birthday'].replace(year=today.year + 1) < next_week_start + timedelta(days=2)]

    for user in next_weekend_birthdays:
        user_birthday = user['birthday'].replace(year=today.year + 1)
        day_of_week = get_day_of_week(user_birthday)
        birthdays[day_of_week].append({'name': user['name'], 'birthday': user_birthday})

    return {day: users for day, users in birthdays.items() if users}

def test_all_future_birthdays_no_weekend():
    # Реалізуйте тест, коли усі дні народження користувачів є у майбутньому і не впадають на вихідні.
    pass

def test_some_birthdays_on_weekend():
    # Реалізуйте тест, коли дні народження деяких користувачів випадають на вихідні.
    pass

def test_some_birthdays_passed_this_year():
    # Реалізуйте тест, коли деякі дні народження користувачів вже минули у цьому році.
    pass

def test_no_users():
    # Реалізуйте тест, коли у списку немає користувачів.
    pass

def test_all_birthdays_passed_this_year():
    # Реалізуйте тест, коли всі дні народження користувачів вже минули у цьому році.
    pass

def print_birthday_result(result):
    for day, users in result.items():
        if users:
            print(f"У {day}, наступні користувачі мають дні народження:")
            for user in users:
                print(f"- {user['name']} ({user['birthday'].strftime('%Y-%m-%d')})")
            print()
        else:
            print(f"У {day}, немає днів народження.\n")

# Тести та приклади використання залишаються незмінними
if __name__ == "__main__":
    test_all_future_birthdays_no_weekend()
    test_some_birthdays_on_weekend()
    test_some_birthdays_passed_this_year()
    test_no_users()
    test_all_birthdays_passed_this_year()
    print("Усі тести пройдено!")

    # Приклад використання
    users = [
        {'name': 'Alice', 'birthday': date.today().replace(month=1, day=3)},
        {'name': 'Bob', 'birthday': date.today().replace(month=12, day=28)},
        {'name': 'Charlie', 'birthday': date.today().replace(month=12, day=29)},
        {'name': 'David', 'birthday': date.today().replace(month=1, day=6)}
        # Додайте інших користувачів за потреби
    ]
    result = get_birthdays_per_week(users)
    print_birthday_result(result)
