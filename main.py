import re
import smtplib
import random
import re
from email.mime.text import MIMEText

filename = "quotes.txt"

def get_random_quote(filename):
    with open(filename, 'r', encoding="utf8") as f:
        #reads lines in file
        lines = f.readlines()
        # Use a list comprehension to extract the lines that are in quotation marks
        quotes = [line for line in lines if re.search('"(.+)"', line)]

        # Select a random line
        line = random.choice(quotes)

        # return the line
        return (line)


# Set the email parameters
to_email = 'antqdasilva@gmail.com'
from_email = 'qdee508@gmail.com'
subject = 'Daily Motivation'
message = get_random_quote("quotes.txt")

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
