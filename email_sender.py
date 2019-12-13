import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
from config import login, password

# this gives us access to html
html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Oscar Sanchez Jr.'
email['to'] = 'ojsanch@gmail.com'
email['subject'] = 'Totally Not Fake Monthly Newsletter'

email.set_content(html.substitute({'name': 'John Smith'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(login, password)
    smtp.send_message(email)
    print('Email sent, all good!')
