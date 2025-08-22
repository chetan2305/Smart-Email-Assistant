# Module to read emails using Gmail API
from googleapiclient.discovery import build
import base64
from email.mime.text import MIMEText

def read_emails(service):
    results = service.users().messages().list(userId='me', maxResults=10).execute()
    messages = results.get('messages', [])
    email_list = []
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        payload = msg_data['payload']
        headers = payload.get('headers', [])
        subject = None
        for header in headers:
            if header['name'] == 'Subject':
                subject = header['value']
        snippet = msg_data.get('snippet')
        email_list.append({'subject': subject, 'snippet': snippet})
    return email_list

