from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS
from flask_mail import Mail, Message
import os
from datetime import datetime
import json
import sqlite3
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

mail = Mail(app)


# Database setup
DB_PATH = 'submissions.db'

def init_db():
    """Initialize the database with all necessary tables"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create submissions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service_type TEXT NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            description TEXT,
            deadline DATE,
            urgency TEXT,
            platform TEXT,
            timeline TEXT,
            budget TEXT,
            additional_data TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

# Initialize database on startup
init_db()

def save_submission(service_type, data):
    """Save form submission to database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO submissions 
        (service_type, name, email, description, deadline, urgency, platform, timeline, budget, additional_data)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        service_type,
        data.get('name', ''),
        data.get('email', ''),
        data.get('description', ''),
        data.get('deadline', ''),
        data.get('urgency', ''),
        data.get('platform', ''),
        data.get('timeline', ''),
        data.get('budget', ''),
        json.dumps(data)
    ))
    
    conn.commit()
    submission_id = cursor.lastrowid
    conn.close()
    
    return submission_id

def send_notification_email(service_type, data):
    """Send email notification to admin"""
    try:
        msg = Message(
            subject=f'New {service_type} Submission - Byts of Everything',
            recipients=[app.config['MAIL_USERNAME']],
            body=f"""
New service request received!

Service Type: {service_type}
Name: {data.get('name', 'N/A')}
Email: {data.get('email', 'N/A')}
Deadline: {data.get('deadline', 'N/A')}

Description:
{data.get('description', 'N/A')}

Additional Details:
{json.dumps(data, indent=2)}

Submitted at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            """
        )
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False

def send_confirmation_email(email, name, service_type):
    """Send confirmation email to customer"""
    try:
        msg = Message(
            subject=f'Thank you for contacting Byts of Everything',
            recipients=[email],
            body=f"""
Dear {name},

Thank you for reaching out to Byts of Everything!

We have received your request for {service_type} services. Our team will review your submission and get back to you within 24-48 hours.

In the meantime, feel free to schedule a meeting with us at:
https://calendly.com/moussamb1901/30min

Best regards,
Byts of Everything Team
            """
        )
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error sending confirmation email: {str(e)}")
        return False

# Route for serving HTML pages
@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def serve_page(path):
    if path.endswith('.html'):
        return app.send_static_file(path)
    return app.send_static_file(path)

# Helper function to handle form submissions
def handle_submission(service_type, data):
    """Handle form submission and return JSON response"""
    try:
        submission_id = save_submission(service_type, data)
        send_notification_email(service_type, data)
        send_confirmation_email(data.get('email'), data.get('name'), service_type)
        
        return jsonify({
            'success': True,
            'message': 'Thank you! Your submission has been received. We will contact you shortly.',
            'submission_id': submission_id
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'An error occurred: {str(e)}'
        }), 500

# API Integration Services
@app.route('/submit-simple-api', methods=['POST'])
def submit_simple_api():
    data = request.form.to_dict()
    return handle_submission('Simple API Integration', data)

@app.route('/submit-moderate-api', methods=['POST'])
def submit_moderate_api():
    data = request.form.to_dict()
    return handle_submission('Moderate API Integration', data)

@app.route('/submit-complex-api', methods=['POST'])
def submit_complex_api():
    data = request.form.to_dict()
    return handle_submission('Complex API Integration', data)

@app.route('/submit-enterprise-api', methods=['POST'])
def submit_enterprise_api():
    data = request.form.to_dict()
    return handle_submission('Enterprise API Integration', data)

# Unit Testing Services
@app.route('/submit-basic-unit-testing', methods=['POST'])
def submit_basic_unit_testing():
    data = request.form.to_dict()
    return handle_submission('Basic Unit Testing', data)

@app.route('/submit-intermediate-unit-testing', methods=['POST'])
def submit_intermediate_unit_testing():
    data = request.form.to_dict()
    return handle_submission('Intermediate Unit Testing', data)

@app.route('/submit-advanced-unit-testing', methods=['POST'])
def submit_advanced_unit_testing():
    data = request.form.to_dict()
    return handle_submission('Advanced Unit Testing', data)

@app.route('/submit-enterprise-unit-testing', methods=['POST'])
def submit_enterprise_unit_testing():
    data = request.form.to_dict()
    return handle_submission('Enterprise Unit Testing', data)

# Integration Testing Services
@app.route('/submit-basic-integration-testing', methods=['POST'])
def submit_basic_integration_testing():
    data = request.form.to_dict()
    return handle_submission('Basic Integration Testing', data)

@app.route('/submit-intermediate-integration-testing', methods=['POST'])
def submit_intermediate_integration_testing():
    data = request.form.to_dict()
    return handle_submission('Intermediate Integration Testing', data)

@app.route('/submit-advanced-integration-testing', methods=['POST'])
def submit_advanced_integration_testing():
    data = request.form.to_dict()
    return handle_submission('Advanced Integration Testing', data)

@app.route('/submit-enterprise-integration-testing', methods=['POST'])
def submit_enterprise_integration_testing():
    data = request.form.to_dict()
    return handle_submission('Enterprise Integration Testing', data)

# Software Testing Services
@app.route('/submit-basic-software-testing', methods=['POST'])
def submit_basic_software_testing():
    data = request.form.to_dict()
    return handle_submission('Basic Software Testing', data)

@app.route('/submit-intermediate-software-testing', methods=['POST'])
def submit_intermediate_software_testing():
    data = request.form.to_dict()
    return handle_submission('Intermediate Software Testing', data)

@app.route('/submit-advanced-software-testing', methods=['POST'])
def submit_advanced_software_testing():
    data = request.form.to_dict()
    return handle_submission('Advanced Software Testing', data)

@app.route('/submit-enterprise-software-testing', methods=['POST'])
def submit_enterprise_software_testing():
    data = request.form.to_dict()
    return handle_submission('Enterprise Software Testing', data)

# Custom Services
@app.route('/submit-code-rescue', methods=['POST'])
def submit_code_rescue():
    data = request.form.to_dict()
    return handle_submission('Code Rescue Mission', data)

@app.route('/submit-mvp-launch', methods=['POST'])
def submit_mvp_launch():
    data = request.form.to_dict()
    return handle_submission('MVP Launch Pad', data)

@app.route('/submit-ai-integration', methods=['POST'])
def submit_ai_integration():
    data = request.form.to_dict()
    # Handle multiple checkbox values for AI features
    ai_features = request.form.getlist('ai-features')
    data['ai-features'] = ', '.join(ai_features)
    return handle_submission('AI Integration Wizard', data)

@app.route('/submit-devops-transformation', methods=['POST'])
def submit_devops_transformation():
    data = request.form.to_dict()
    # Handle multiple checkbox values for pain points
    pain_points = request.form.getlist('pain-points')
    data['pain-points'] = ', '.join(pain_points)
    return handle_submission('DevOps Transformation', data)

# Admin dashboard to view submissions
@app.route('/admin/submissions')
def view_submissions():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM submissions ORDER BY created_at DESC LIMIT 100')
    submissions = cursor.fetchall()
    conn.close()
    
    return jsonify({
        'submissions': [
            {
                'id': s[0],
                'service_type': s[1],
                'name': s[2],
                'email': s[3],
                'description': s[4],
                'deadline': s[5],
                'created_at': s[11]
            }
            for s in submissions
        ]
    })

# Health check endpoint
@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    # Run on port 5000 in development mode
    app.run(debug=True, host='0.0.0.0', port=5000)