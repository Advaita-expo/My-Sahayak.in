import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Set up Google Sheets API credentials
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_NAME = 'My Sahayak Database'
WORKSHEET_NAME = 'My Sahayak Data'

def initialize_google_sheets():
    """
    Initialize Google Sheets connection.
    You need to:
    1. Create a Google Cloud Project
    2. Enable Google Sheets API
    3. Create a Service Account
    4. Download the JSON key file
    5. Save it as 'google_credentials.json' in the backend folder
    """
    try:
        creds = Credentials.from_service_account_file('backend/google_credentials.json', scopes=SCOPES)
        client = gspread.authorize(creds)
        return client
    except Exception as e:
        print(f"Error initializing Google Sheets: {e}")
        return None

def append_booking_to_sheets(booking_data):
    """
    Append booking data to Google Sheets.
    
    booking_data should be a dictionary with:
    - bookingReference
    - service
    - tier
    - price
    - fullName
    - phone
    - email
    - city
    - address
    - startDate
    - familySize
    - requirements
    """
    try:
        client = initialize_google_sheets()
        if not client:
            print("Failed to initialize Google Sheets client")
            return False
        
        # Open the spreadsheet
        spreadsheet = client.open(SPREADSHEET_NAME)
        worksheet = spreadsheet.worksheet(WORKSHEET_NAME)
        
        # Prepare row data
        row = [
            booking_data.get('bookingReference', ''),
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            booking_data.get('fullName', ''),
            booking_data.get('email', ''),
            booking_data.get('phone', ''),
            booking_data.get('service', ''),
            booking_data.get('tier', ''),
            booking_data.get('price', ''),
            booking_data.get('city', ''),
            booking_data.get('address', ''),
            booking_data.get('startDate', ''),
            booking_data.get('familySize', ''),
            booking_data.get('requirements', ''),
        ]
        
        # Append row to worksheet
        worksheet.append_row(row)
        print(f"Booking {booking_data.get('bookingReference')} added to Google Sheets")
        return True
        
    except Exception as e:
        print(f"Error appending to Google Sheets: {e}")
        return False

def get_all_bookings():
    """Get all bookings from Google Sheets"""
    try:
        client = initialize_google_sheets()
        if not client:
            return []
        
        spreadsheet = client.open(SPREADSHEET_NAME)
        worksheet = spreadsheet.worksheet(WORKSHEET_NAME)
        records = worksheet.get_all_records()
        return records
        
    except Exception as e:
        print(f"Error retrieving bookings: {e}")
        return []
