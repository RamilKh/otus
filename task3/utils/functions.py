from datetime import datetime, timedelta


def get_last_days(count: int = 7) -> list:
    dates = []
    today = datetime.today()
    for day in range(0, count):
        today_before = today - timedelta(day)
        dates.append(today_before.date())

    return dates
