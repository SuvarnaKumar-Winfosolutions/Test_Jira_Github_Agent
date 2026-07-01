import unittest
from unittest.mock import patch
from datetime import datetime, timezone

# Assuming proj1_utils is accessible in the Python path for testing.
# In a real project, this might involve setting up PYTHONPATH or using a test runner
# that handles package structure.
from proj1_utils.date_time_helpers import get_current_utc_date_string

class TestDateTimeHelpers(unittest.TestCase):

    def test_get_current_utc_date_string_format(self):
        """Test that the returned string adheres to the YYYY-MM-DD format."""
        date_string = get_current_utc_date_string()
        self.assertRegex(date_string, r"^\d{4}-\d{2}-\d{2}$")

        parts = date_string.split('-')
        self.assertEqual(len(parts), 3)
        self.assertTrue(1900 <= int(parts[0]) <= 2200) # Reasonable year range
        self.assertTrue(1 <= int(parts[1]) <= 12)    # Month range
        self.assertTrue(1 <= int(parts[2]) <= 31)    # Day range

    @patch('proj1_utils.date_time_helpers.datetime')
    def test_get_current_utc_date_string_specific_utc(self, mock_datetime):
        """Test with a specific mocked UTC datetime to ensure correct date is returned."""
        # Simulate a specific UTC datetime: January 15, 2023, 10:30:00 UTC
        # The mocked datetime.now(timezone.utc) will return this exact datetime object.
        fixed_utc_dt = datetime(2023, 1, 15, 10, 30, 0, tzinfo=timezone.utc)
        mock_datetime.now.return_value = fixed_utc_dt
        
        result = get_current_utc_date_string()
        self.assertEqual(result, "2023-01-15")

        # Another specific date with different month/day values
        fixed_utc_dt = datetime(2024, 7, 21, 23, 59, 59, tzinfo=timezone.utc)
        mock_datetime.now.return_value = fixed_utc_dt
        result = get_current_utc_date_string()
        self.assertEqual(result, "2024-07-21")

    @patch('proj1_utils.date_time_helpers.datetime')
    def test_get_current_utc_date_string_midnight_crossover(self, mock_datetime):
        """Test correct behavior around UTC midnight, especially across day/month/year boundaries."""
        # Simulate UTC time just past midnight into a new day (e.g., New Year's Day UTC)
        mock_datetime.now.return_value = datetime(2024, 1, 1, 3, 0, 0, tzinfo=timezone.utc)
        result = get_current_utc_date_string()
        self.assertEqual(result, "2024-01-01")

        # Simulate UTC time just before midnight of a day
        mock_datetime.now.return_value = datetime(2023, 12, 31, 23, 59, 59, tzinfo=timezone.utc)
        result = get_current_utc_date_string()
        self.assertEqual(result, "2023-12-31")
        
        # Simulate crossing from a single-digit month to a double-digit one
        mock_datetime.now.return_value = datetime(2023, 9, 30, 23, 0, 0, tzinfo=timezone.utc)
        result = get_current_utc_date_string()
        self.assertEqual(result, "2023-09-30")

        # Simulate crossing to a new month with single-digit day
        mock_datetime.now.return_value = datetime(2023, 10, 1, 0, 0, 1, tzinfo=timezone.utc)
        result = get_current_utc_date_string()
        self.assertEqual(result, "2023-10-01")


    @patch('proj1_utils.date_time_helpers.datetime')
    def test_get_current_utc_date_string_padding(self, mock_datetime):
        """Test that single-digit months and days are correctly zero-padded."""
        # Simulate a date with single-digit month and day (e.g., May 7th)
        mock_datetime.now.return_value = datetime(2023, 5, 7, 12, 0, 0, tzinfo=timezone.utc)
        result = get_current_utc_date_string()
        self.assertEqual(result, "2023-05-07")

        # Simulate a date with single-digit month and double-digit day (e.g., September 10th)
        mock_datetime.now.return_value = datetime(2023, 9, 10, 12, 0, 0, tzinfo=timezone.utc)
        result = get_current_utc_date_string()
        self.assertEqual(result, "2023-09-10")

        # Simulate a date with double-digit month and single-digit day (e.g., October 3rd)
        mock_datetime.now.return_value = datetime(2023, 10, 3, 12, 0, 0, tzinfo=timezone.utc)
        result = get_current_utc_date_string()
        self.assertEqual(result, "2023-10-03")
