from datetime import date


def calculate_hours(start_date, end_date, hours_per_week):

    delta = end_date - start_date
    weeks = delta.days / 7
    hours = weeks * hours_per_week
    return hours


if __name__ == "__main__":
    start_date = date(2023, 10, 1)
    end_date = date(2025, 12, 31)
    hours_per_week = 5

    hours = calculate_hours(start_date, end_date, hours_per_week)
    print(
        f"Von {start_date} bis {end_date} mit {hours_per_week} Stunden pro Woche:\n{hours} Stunden gearbeitet."
    )
