# ==========================================
# JARVIS AI ASSISTANT - PART 7
# WhatsApp Automation
# ==========================================

import pywhatkit
import datetime
import json


CONTACTS_FILE = "contacts.json"


def load_contacts():

    try:

        with open(
            CONTACTS_FILE,
            "r"
        ) as file:

            return json.load(file)

    except:

        return {}


def get_contact_number(name):

    contacts = load_contacts()

    return contacts.get(
        name.lower()
    )


# ==========================================
# Send Instant WhatsApp
# ==========================================

def send_whatsapp(
        contact_name,
        message):

    number = get_contact_number(
        contact_name
    )

    if not number:

        print(
            "Contact not found."
        )

        return False

    try:

        pywhatkit.sendwhatmsg_instantly(
            number,
            message,
            wait_time=15,
            tab_close=True
        )

        print(
            "WhatsApp message sent."
        )

        return True

    except Exception as e:

        print(
            "WhatsApp Error:",
            e
        )

        return False


# ==========================================
# Schedule WhatsApp
# ==========================================

def schedule_whatsapp(
        contact_name,
        message,
        hour,
        minute):

    number = get_contact_number(
        contact_name
    )

    if not number:

        return False

    try:

        pywhatkit.sendwhatmsg(
            number,
            message,
            hour,
            minute
        )

        return True

    except Exception as e:

        print(e)

        return False
    # ==========================================
# Email Automation
# ==========================================

import yagmail

EMAIL_ADDRESS = "YOUR_EMAIL@gmail.com"

APP_PASSWORD = "YOUR_GMAIL_APP_PASSWORD"


def send_email(
        recipient,
        body,
        subject="Jarvis Message"):

    try:

        yag = yagmail.SMTP(
            EMAIL_ADDRESS,
            APP_PASSWORD
        )

        yag.send(
            to=recipient,
            subject=subject,
            contents=body
        )

        print(
            "Email sent."
        )

        return True

    except Exception as e:

        print(
            "Email Error:",
            e
        )

        return False
    def send_email_attachment(
        recipient,
        subject,
        body,
        attachment):

    try:

        yag = yagmail.SMTP(
            EMAIL_ADDRESS,
            APP_PASSWORD
        )

        yag.send(
            to=recipient,
            subject=subject,
            contents=body,
            attachments=attachment
        )

        return True

    except Exception as e:

        print(e)

        return False
    # ==========================================
# Message Scheduler
# ==========================================

import schedule
import time

scheduled_jobs = []


def add_job(
        func,
        interval_minutes=1):

    schedule.every(
        interval_minutes
    ).minutes.do(func)


def run_scheduler():

    while True:

        schedule.run_pending()

        time.sleep(1)
        from whatsapp import (
    send_whatsapp,
    schedule_whatsapp
)

from email_sender import (
    send_email,
    send_email_attachment
)
elif "send whatsapp" in command:

    speak(
        "Who should receive the message?"
    )

    contact = listen()

    speak(
        "What is the message?"
    )

    message = listen()

    success = send_whatsapp(
        contact,
        message
    )

    if success:

        speak(
            "Message sent successfully."
        )

    else:

        speak(
            "Unable to send message."
        )
        elif "send email" in command:

    recipient = input(
        "Recipient Email: "
    )

    speak(
        "What should I send?"
    )

    body = listen()

    success = send_email(
        recipient,
        body
    )

    if success:

        speak(
            "Email sent."
        )

    else:

        speak(
            "Email failed."
        )
        elif "send file email" in command:

    recipient = input(
        "Recipient Email: "
    )

    attachment = input(
        "File Path: "
    )

    send_email_attachment(
        recipient,
        "Jarvis File",
        "Attachment included.",
        attachment
    )

    speak(
        "File sent."
    )