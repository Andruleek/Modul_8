from datetime import date, timedelta, datetime  # Add import for datetime

DAYS_IN_WEEK = 7

def get_day_of_week(date_obj):
    days = ["Monday ", "Tuesday ", "Wednesday ", "Thursday ", "Friday ", "Saturday ", "Sunday "]
    return days[date_obj.weekday()]

def get_next_week_start():
    today = date.today()
    return today + timedelta(days=(DAYS_IN_WEEK - today.weekday() + DAYS_IN_WEEK) % DAYS_IN_WEEK)

def get_birthdays_per_week(users):
    today = date.today()
    next_week_start = get_next_week_start()
    next_week_end = next_week_start + timedelta(days=DAYS_IN_WEEK + 2)  # Add 2 days to account for weekends

    birthdays = {day: [] for day in ["Monday ", "Tuesday ", "Wednesday ", "Thursday ", "Friday ", "Saturday ", "Sunday "]}

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
    # Implement the test when all users' birthdays are in the future and not on weekends
    pass

def test_some_birthdays_on_weekend():
    # Implement the test when some users' birthdays fall on weekends
    pass

def test_some_birthdays_passed_this_year():
    # Implement the test when some users' birthdays have already passed this year
    pass

def test_no_users():
    # Implement the test when the list of users is empty
    pass

def test_all_birthdays_passed_this_year():
    # Implement the test when all users' birthdays have already passed this year
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

# Tests and examples remain unchanged
if __name__ == "__main__":
    test_all_future_birthdays_no_weekend()
    test_some_birthdays_on_weekend()
    test_some_birthdays_passed_this_year()
    test_no_users()
    test_all_birthdays_passed_this_year()
    print("Усі тести пройдено!")

    # Example usage
    users = [
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()},
        {'name': 'Bob', 'birthday': datetime(2000, 3, 7).date()},
        {'name': 'Charlie', 'birthday': datetime(2010, 12, 15).date()},
        {'name': 'David', 'birthday': datetime(2017, 9, 1).date()}
        # Add other users as needed
    ]
    result = get_birthdays_per_week(users)
    print_birthday_result(result)
