from flask import Flask, request, jsonify, render_template
from google_sheets import append_booking_to_sheets
import os
import json
from datetime import datetime

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))

# Route to render the main page
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/submit-booking', methods=['POST'])
def submit_booking():
    """Handle booking submission to Google Sheets"""
    try:
        data = request.json
        print('Received booking data:', data)
        
        # Append to Google Sheets
        success = append_booking_to_sheets(data)
        
        if success:
            return jsonify({'status': 'success', 'message': 'Booking submitted successfully'})
        else:
            return jsonify({'status': 'error', 'message': 'Failed to save booking'}), 500
            
    except Exception as e:
        print(f'Error processing booking: {e}')
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/submit-form', methods=['POST'])
def submit_form():
    """Handle contact form submissions (existing endpoint)"""
    try:
        data = request.json
        print('Received contact data:', data)
        
        # Prepare data for Google Sheets
        contact_data = {
            'bookingReference': f"CONTACT-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            'fullName': data.get('from_name'),
            'email': data.get('from_email'),
            'phone': data.get('phone'),
            'service': data.get('service'),
            'city': 'Contact Form',
            'address': data.get('message'),
            'startDate': datetime.now().strftime('%Y-%m-%d'),
            'familySize': 'N/A',
            'requirements': 'Contact Form Inquiry',
            'tier': 'Inquiry'
        }
        
        # Append to Google Sheets
        success = append_booking_to_sheets(contact_data)
        
        if success:
            return jsonify({'status': 'success'})
        else:
            return jsonify({'status': 'error', 'message': 'Failed to save contact info'}), 500
            
    except Exception as e:
        print(f'Error processing contact form: {e}')
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
