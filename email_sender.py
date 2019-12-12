import smtplib
from email.message import EmailMessage
# using a dollar sign you can substitute variables inside of texts - Template
from string import Template
from pathlib import Path
from config import login, password
# similar to os.path, it allows us to access the HTML document

# create a dictionary for fake users, and implement them in the html.substitue
# also create a timer function to automate this to a certain time

# this gives us access to html
html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Oscar Sanchez Jr.'
# email['to'] = 'lexi.m.smith94@gmail.com'
email['to'] = 'ojsanch@gmail.com'
email['subject'] = 'Totally Not Fake Monthly Newsletter'

email.set_content(html.substitute({'name': 'Lexi Smith'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # lets the server know you up and running
    smtp.starttls()  # encription mechanism
    smtp.login(login, password)
    # smtp.login('osj.dev.tests@gmail.com', 'ovlhcyvbsrftxids')
    smtp.send_message(email)
    print('Email sent, all good!')
