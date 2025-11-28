# Byts of Everything - Backend Setup

## Overview
Flask backend to handle form submissions from all service pages, send email notifications, and store data in SQLite database.

## Features
✅ Form submission handling for all services
✅ Email notifications to admin
✅ Confirmation emails to customers
✅ SQLite database storage
✅ Admin dashboard API
✅ CORS enabled for frontend integration

## Installation

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Email Settings
1. Copy `.env.example` to `.env`
2. Update with your email credentials:
   - For Gmail: Enable 2FA and create an App Password
   - Update `MAIL_USERNAME` and `MAIL_PASSWORD`

### 3. Run the Application
```bash
python app.py
```

The server will start on `http://localhost:5000`

## API Endpoints

### Service Submissions
All form submissions follow this pattern:
- **POST** `/submit-{service-name}` - Submit form data
- Returns: Redirect to service page with success parameter

### Services Covered:
**API Integration:**
- `/submit-simple-api`
- `/submit-moderate-api`
- `/submit-complex-api`
- `/submit-enterprise-api`

**Unit Testing:**
- `/submit-basic-unit-testing`
- `/submit-intermediate-unit-testing`
- `/submit-advanced-unit-testing`
- `/submit-enterprise-unit-testing`

**Integration Testing:**
- `/submit-basic-integration-testing`
- `/submit-intermediate-integration-testing`
- `/submit-advanced-integration-testing`
- `/submit-enterprise-integration-testing`

**Software Testing:**
- `/submit-basic-software-testing`
- `/submit-intermediate-software-testing`
- `/submit-advanced-software-testing`
- `/submit-enterprise-software-testing`

**Custom Services:**
- `/submit-code-rescue` - Code Rescue Mission
- `/submit-mvp-launch` - MVP Launch Pad
- `/submit-ai-integration` - AI Integration Wizard
- `/submit-devops-transformation` - DevOps Transformation

### Admin Endpoints
- **GET** `/admin/submissions` - View all submissions (JSON)
- **GET** `/health` - Health check endpoint

## Database
SQLite database (`submissions.db`) stores all form submissions with:
- Service type
- Customer details (name, email)
- Project description
- Deadline
- Additional service-specific data
- Timestamp

## Email Notifications
Two types of emails are sent:
1. **Admin Notification** - Sent to business owner with submission details
2. **Customer Confirmation** - Sent to customer confirming receipt

## Production Deployment

### Environment Variables
Set these in your production environment:
```
MAIL_USERNAME=your-production-email@gmail.com
MAIL_PASSWORD=your-production-app-password
FLASK_ENV=production
SECRET_KEY=generate-a-secure-random-key
```

### Recommended Setup
- Use Gunicorn for production: `gunicorn -w 4 app:app`
- Set up proper email service (SendGrid, Mailgun, etc.)
- Use PostgreSQL instead of SQLite for production
- Add authentication for admin endpoints
- Set up SSL/HTTPS

## Security Notes
⚠️ **Important:**
- Never commit `.env` file to version control
- Use strong app passwords
- Add authentication to admin endpoints before production
- Enable HTTPS in production
- Consider rate limiting for form submissions

## Troubleshooting

### Email Not Sending
- Check Gmail App Password is correct
- Verify 2FA is enabled on Gmail account
- Check firewall/antivirus isn't blocking SMTP

### Database Errors
- Ensure write permissions in project directory
- Check `submissions.db` file is created

### CORS Issues
- Flask-CORS is configured for all origins in development
- Restrict origins in production

## Support
For issues or questions, contact: your-email@example.com