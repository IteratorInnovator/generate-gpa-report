from smtplib import SMTP
import ssl
from email.message import EmailMessage
from dotenv import load_dotenv
import os
from process_data import load_json

def draft_email_message(pdf_file,sender_email, recipient_email):
    student_info = load_json("student_info.json")
    body_content = f"""
Hi {student_info['name']},
This email contains a copy of your GPA report for your reference.

Key details:

Name: {student_info['name']}
Course of Study: {student_info['course_of_study']}

The full report is attached to this email for safekeeping.

Best regards,
Ng Kok Jing
    """
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = f"{student_info['name']} GPA Report"
    msg.set_content(body_content)
    with open(pdf_file, 'rb') as f:
        msg.add_attachment(f.read(), maintype="application", subtype='pdf', filename="GPA_report.pdf")
    return msg

def email_gpa_pdf_report(pdf_file):
    load_dotenv()
    sender_email = os.getenv('SENDER_EMAIL')
    app_password = os.getenv('APP_PASSWORD')
    recipient_email = os.getenv('RECIPIENT_EMAIL')
    email_msg = draft_email_message(pdf_file, sender_email, recipient_email)
    with SMTP(host='smtp.gmail.com', port=587) as server:
        server.starttls(context=ssl.create_default_context())
        server.login(sender_email, app_password)
        server.send_message(email_msg)
    
if __name__ == "__main__":
    pass