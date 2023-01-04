import re
import smtplib
import random
import re
from datetime import datetime
from email.mime.text import MIMEText

filename = "quotes.txt"


def function_for_monday(filename):
    with open(filename, 'r', encoding="utf8") as f:
        lines = f.readlines()
        return random.choice(lines[:20])


def function_for_tuesday(filename):
    with open(filename, 'r', encoding="utf8") as f:
        lines = f.readlines()
        return random.choice(lines[20:41])

def function_for_wednesday(filename):
    with open(filename, 'r', encoding="utf8") as f:
        lines = f.readlines()
        return random.choice(lines[42:53])

def function_for_thursday(filename):
    with open(filename, 'r', encoding="utf8") as f:
        lines = f.readlines()
        return random.choice(lines[54:65])

def function_for_friday(filename):
    with open(filename, 'r', encoding="utf8") as f:
        lines = f.readlines()
        return random.choice(lines[66:77])

def function_for_saturday(filename):
    with open(filename, 'r', encoding="utf8") as f:
        lines = f.readlines()
        return random.choice(lines[78:89])

def function_for_sunday(filename):
    with open(filename, 'r', encoding="utf8") as f:
        lines = f.readlines()
        return random.choice(lines[90:100])


def get_random_quote(filename):
    # with open(filename, 'r', encoding="utf8") as f:
    #     # reads lines in file
    #     lines = f.readlines()
    #     # Use a list comprehension to extract the lines that are in quotation marks
    #     quotes = [line for line in lines if re.search('"(.+)"', line)]
    #
    #     # Select a random line
    #     line = random.choice(quotes)
    #
    #     # return the line
    #     return (line)
    from datetime import datetime
    current_day = datetime.today().weekday()
    if current_day == 0:
        return function_for_monday(filename)
    elif current_day == 1:
        return function_for_tuesday(filename)
    elif current_day == 2:
        return function_for_wednesday(filename)
    elif current_day == 3:
        return function_for_thursday(filename)
    elif current_day == 4:
        return function_for_friday(filename)
    elif current_day == 5:
        return function_for_saturday(filename)
    elif current_day == 6:
        return function_for_sunday(filename)
    else:
        return "you stoopid fix this"


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
