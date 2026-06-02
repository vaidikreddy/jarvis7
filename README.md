# 🤖 JARVIS AI Assistant - Communication Module

This module extends the JARVIS AI Assistant with communication capabilities, including WhatsApp messaging, email automation, file attachments, and message scheduling. It allows users to send messages and emails using voice commands or direct input. :contentReference[oaicite:0]{index=0}

---

## Features

### 📱 WhatsApp Automation
- Send WhatsApp messages instantly
- Contact management using `contacts.json`
- Schedule WhatsApp messages
- Voice-controlled messaging

### 📧 Email Automation
- Send emails through Gmail
- Voice-based email content
- Send email attachments
- Custom email subjects

### ⏰ Scheduling
- Schedule recurring tasks
- Background job execution
- Automated reminders and messaging

---

## Project Structure

```text
communication/
│
├── whatsapp.py
├── email_sender.py
├── scheduler.py
├── contacts.json
└── README.md
```

---

## Installation

Install required dependencies:

```bash
pip install pywhatkit
pip install yagmail
pip install schedule
pip install python-dotenv
```

---

## Contacts Configuration

Create a `contacts.json` file:

```json
{
    "mom": "+911234567890",
    "dad": "+919876543210",
    "friend": "+911112223334"
}
```

---

## Environment Variables

Create a `.env` file:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_APP_PASSWORD=your_gmail_app_password
```

---

## WhatsApp Functions

### Send Message

```python
send_whatsapp(contact_name, message)
```

Example:

```python
send_whatsapp(
    "mom",
    "Hello from Jarvis!"
)
```

### Schedule Message

```python
schedule_whatsapp(
    contact_name,
    message,
    hour,
    minute
)
```

Example:

```python
schedule_whatsapp(
    "friend",
    "Meeting at 5 PM",
    16,
    45
)
```

---

## Email Functions

### Send Email

```python
send_email(
    recipient,
    body,
    subject="Jarvis Message"
)
```

Example:

```python
send_email(
    "user@example.com",
    "Hello from Jarvis!"
)
```

### Send Email with Attachment

```python
send_email_attachment(
    recipient,
    subject,
    body,
    attachment
)
```

Example:

```python
send_email_attachment(
    "user@example.com",
    "Project File",
    "Please find attached.",
    "report.pdf"
)
```

---

## Scheduler Functions

### Add Scheduled Job

```python
add_job(
    func,
    interval_minutes=1
)
```

### Start Scheduler

```python
run_scheduler()
```

---

## Voice Commands

### WhatsApp

```text
Hey Jarvis

Send WhatsApp
```

Jarvis will ask:

```text
Who should receive the message?

What is the message?
```

### Email

```text
Hey Jarvis

Send email
```

Jarvis will ask:

```text
Recipient Email

What should I send?
```

### File Email

```text
Hey Jarvis

Send file email
```

Jarvis will ask:

```text
Recipient Email

File Path
```

---

## Error Handling

The module handles:

- Invalid contacts
- Missing phone numbers
- WhatsApp delivery failures
- Invalid email addresses
- Attachment errors
- SMTP authentication issues

---

## Security Notes

- Store credentials in `.env`
- Never hardcode passwords
- Use Gmail App Passwords
- Protect contact information

---

## Future Enhancements

- Bulk WhatsApp Messaging
- Voice Contact Creation
- SMS Integration
- Outlook Support
- Telegram Integration
- Scheduled Email Campaigns
- Contact Groups

---

## Technologies Used

- Python 3
- PyWhatKit
- Yagmail
- Schedule
- JSON
- Gmail SMTP

---

## Author

**Vaidik Reddy**

---

## License

MIT License

This project is intended for educational and personal use.
