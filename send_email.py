# Module to send email using Gmail API
from googleapiclient.discovery import build
import base64
from email.mime.text import MIMEText

def create_message(to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw}

def send_message(service, message):
    sent_message = service.users().messages().send(userId='me', body=message).execute()
    return sent_message

