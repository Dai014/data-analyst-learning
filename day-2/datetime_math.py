from datetime import datetime, timedelta

def add_days(start_date: str, days: int) -> str:
    """Add a specified number of days to a given date."""
    date_format = "%Y-%m-%d"
    date_obj = datetime.strptime(start_date, date_format)
    new_date = date_obj + timedelta(days=days)
    return new_date.strftime(date_format)

def subtract_days(start_date: str, days: int) -> str:
    """Subtract a specified number of days from a given date."""
    date_format = "%Y-%m-%d"
    date_obj = datetime.strptime(start_date, date_format)
    new_date = date_obj - timedelta(days=days)
    return new_date.strftime(date_format)

def days_between(start_date: str, end_date: str) -> int:
    """Calculate the number of days between two dates."""
    date_format = "%Y-%m-%d"
    start_date_obj = datetime.strptime(start_date, date_format)
    end_date_obj = datetime.strptime(end_date, date_format)
    delta = end_date_obj - start_date_obj
    return delta.days

# Example usage
if __name__ == "__main__":
    print("Add 10 days:", add_days("2023-01-01", 10))
    print("Subtract 5 days:", subtract_days("2023-01-10", 5))
    print("Days between:", days_between("2023-01-01", "2023-01-10"))