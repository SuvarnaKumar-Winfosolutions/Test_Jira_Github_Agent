from datetime import datetime, timezone

def get_current_utc_date_string() -> str:
    """
    Retrieves the current date in Coordinated Universal Time (UTC) and
    formats it as a string in YYYY-MM-DD format.

    This function is pure and does not take any parameters. It uses the
    system's current time and converts it to UTC before formatting.

    Returns:
        str: The current UTC date formatted as 'YYYY-MM-DD'.
             Example: '2023-10-27'
    """
    # Obtain the current date and time in UTC.
    now_utc = datetime.now(timezone.utc)

    # Format the UTC datetime object into 'YYYY-MM-DD' string.
    # strftime handles extracting year, month, day and applies zero-padding automatically.
    return now_utc.strftime('%Y-%m-%d')
