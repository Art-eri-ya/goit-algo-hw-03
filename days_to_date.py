from datetime import datetime


def get_days_from_today(date):
    try:
        dt_obj = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        days_difference = (today - dt_obj).days
        return days_difference
    except ValueError:
        return "Wrong format! Please enter date in YYYY-MM-DD."



date_input = input("Enter a date in format YYYY-MM-DD: ")

print(get_days_from_today(date_input))
