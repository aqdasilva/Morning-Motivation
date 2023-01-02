import smtplib
from email.mime.text import MIMEText

# Set the email parameters
to_email = 'antqdasilva@gmail.com'
from_email = 'qdee508@gmail.com'
subject = 'Daily Motivation'
message = 'Your motivational message here'

# Create the email message
msg = MIMEText(message)
msg['To'] = to_email
msg['Subject'] = subject

# Connect to the Gmail SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Login to your Gmail account
server.login(from_email, 'lkiu uxzy xxea gcwr')

# Send the email
server.sendmail(from_email, to_email, msg.as_string())

# Disconnect from the server
server.quit()

print('Email sent!')
