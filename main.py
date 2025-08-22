from auth_gmail import authenticate_gmail
from googleapiclient.discovery import build
from read_emails import read_emails
from send_email import create_message, send_message

def main():
    creds = authenticate_gmail()
    service = build('gmail', 'v1', credentials=creds)

    emails = read_emails(service)
    print("Recent emails:")
    for email in emails:
        print(f"Subject: {email['subject']}")
        print(f"Snippet: {email['snippet']}")
        print("------")
    
    # Example of sending an email
    message = create_message("recipient@example.com", "Test Subject", "This is a test email.")
    result = send_message(service, message)
    print(f"Email sent with ID: {result['id']}")

if __name__ == '__main__':
    main()

