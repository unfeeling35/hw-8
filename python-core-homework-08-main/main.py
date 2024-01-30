from datetime import date, datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    if not users:
        return {}

    today = date.today()
    current_year = today.year

    def current_week_range(date_today):
        week_start = date_today
        week_end = date_today + timedelta(days=6)
        return week_start, week_end

    week_start, week_end = current_week_range(today)
    birthdays_by_weekday = defaultdict(list)

    for user in users:
        birthday_this_year = user["birthday"].replace(year=current_year)
        birthday_next_year = user["birthday"].replace(year=current_year + 1)

        if birthday_this_year < today:
            birthday_date = birthday_next_year
        else:
            birthday_date = birthday_this_year

        if week_start <= birthday_date <= week_end:
            weekday = birthday_date.strftime("%A")
            if weekday in ('Saturday', 'Sunday'):
                weekday = 'Monday'
            birthdays_by_weekday[weekday].append(user["name"])

    return dict(birthdays_by_weekday)


if __name__ == "__main__":
    today = datetime(2024, 1, 30)
    users = [
        {"name": "John", "birthday": today + timedelta(days=5)},
        {"name": "Doe", "birthday": today + timedelta(days=6)},
        {"name": "Alice", "birthday": today + timedelta(days=3)},
    ]

    result = get_birthdays_per_week(users)
    print(result)
