def convert_time_zone(date_str, from_tz, to_tz):
    from datetime import datetime
    import pytz

    # Convert string to datetime object
    naive_datetime = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    
    # Localize to the original timezone
    from_timezone = pytz.timezone(from_tz)
    localized_datetime = from_timezone.localize(naive_datetime)
    
    # Convert to the target timezone
    to_timezone = pytz.timezone(to_tz)
    target_datetime = localized_datetime.astimezone(to_timezone)
    
    return target_datetime.strftime('%Y-%m-%d %H:%M:%S')

def create_summary_columns(df):
    # Assuming df has a datetime column named 'timestamp'
    df['hour'] = df['timestamp'].dt.hour
    df['day'] = df['timestamp'].dt.day
    df['week'] = df['timestamp'].dt.isocalendar().week
    return df

# Example usage
if __name__ == "__main__":
    import pandas as pd

    # Sample data
    data = {
        'timestamp': ['2023-10-01 12:00:00', '2023-10-02 15:30:00'],
    }
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Convert time zone
    print(convert_time_zone('2023-10-01 12:00:00', 'UTC', 'Asia/Ho_Chi_Minh'))

    # Create summary columns
    df = create_summary_columns(df)
    print(df)