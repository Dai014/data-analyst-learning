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

# OOP Example: DateHandler class
class DateHandler:
    """A class to handle date operations."""

    def __init__(self, date_str: str):
        """Initialize with a date string in the format YYYY-MM-DD."""
        self.date_format = "%Y-%m-%d"
        self.date_obj = datetime.strptime(date_str, self.date_format)

    def add_days(self, days: int) -> str:
        """Add a specified number of days to the date."""
        new_date = self.date_obj + timedelta(days=days)
        return new_date.strftime(self.date_format)

    def subtract_days(self, days: int) -> str:
        """Subtract a specified number of days from the date."""
        new_date = self.date_obj - timedelta(days=days)
        return new_date.strftime(self.date_format)

    def days_between(self, other_date: str) -> int:
        """Calculate the number of days between the current date and another date."""
        other_date_obj = datetime.strptime(other_date, self.date_format)
        delta = other_date_obj - self.date_obj
        return delta.days

# Example usage
if __name__ == "__main__":
    # Using functions
    print("Add 10 days:", add_days("2023-01-01", 10))
    print("Subtract 5 days:", subtract_days("2023-01-10", 5))
    print("Days between:", days_between("2023-01-01", "2023-01-10"))

    # Using OOP
    date_handler = DateHandler("2023-01-01")
    print("OOP - Add 10 days:", date_handler.add_days(10))
    print("OOP - Subtract 5 days:", date_handler.subtract_days(5))
    print("OOP - Days between:", date_handler.days_between("2023-01-10"))