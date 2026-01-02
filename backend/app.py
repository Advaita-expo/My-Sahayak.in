from flask import Flask, request, jsonify, render_template
import mysql.connector

import os
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))
# Route to render the main page
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# MySQL configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root@localhost',
    'password': '123456789',
    'database': 'mysahayak'
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/submit-form', methods=['POST'])
def submit_form():
    data = request.json
    print('Received data:', data)
    name = data.get('from_name')
    email = data.get('from_email')
    phone = data.get('phone')
    role = data.get('service')
    message = data.get('message')
    print('line 25')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO contact_messages (name, email, phone, role, message)
        VALUES (%s, %s, %s, %s, %s)
    ''', (name, email, phone, role, message))
    conn.commit()
    cursor.close()
    conn.close()
    print('post-close')
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
