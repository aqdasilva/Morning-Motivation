import re
import smtplib
import random
from datetime import datetime
from email.mime.text import MIMEText
import requests
import json
import secrets


# searches giphy based upon what you put here
search_term = ["motivation", "gym", "pump", "fuck", "hype", "no fucks given", "monday motivation"]

filename = "quotes.txt"
subjectFile = "subjects.txt"


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


##Need 52 words for each day of the week
def subjectOfTheDay():
    from datetime import datetime
    current_day = datetime.today().weekday()
    if current_day == 0:
        return subject_for_monday(subjectFile)
    elif current_day == 1:
        return subject_for_tuesday(subjectFile)
    elif current_day == 2:
        return subject_for_wednesday(subjectFile)
    elif current_day == 3:
        return subject_for_thursday(subjectFile)
    elif current_day == 4:
        return subject_for_friday(subjectFile)
    elif current_day == 5:
        return subject_for_saturday(subjectFile)
    elif current_day == 6:
        return subject_for_sunday(subjectFile)
    else:
        return "you stoopid fix this"

def subject_for_monday(filename):
    with open(filename, 'r', encoding="utf8") as f:
        lines = f.readlines()
        return random.choice(lines[:52])


def subject_for_tuesday(filename):
    with open(filename, 'r', encoding="utf8") as f:
        lines = f.readlines()
        return random.choice(lines[53:104])


def subject_for_wednesday(filename):
    with open(filename, 'r', encoding="utf8") as f:
        lines = f.readlines()
        return random.choice(lines[105:156])


def subject_for_thursday(filename):
    with open(filename, 'r', encoding="utf8") as f:
        lines = f.readlines()
        return random.choice(lines[157:208])


def subject_for_friday(filename):
    with open(filename, 'r', encoding="utf8") as f:
        lines = f.readlines()
        return random.choice(lines[209:260])


def subject_for_saturday(filename):
    with open(filename, 'r', encoding="utf8") as f:
        lines = f.readlines()
        return random.choice(lines[260:312]) + "Saturday"


def subject_for_sunday(filename):
    with open(filename, 'r', encoding="utf8") as f:
        lines = f.readlines()
        return random.choice(lines[313:365]) + "Sunday"
def generate_meme(search_term):
    # makes a request to giphy api
    response = requests.get(
        f"https://api.giphy.com/v1/gifs/search?api_key={secrets.GIPHY_KEY}&q={search_term}&limit=1&offset=0&rating=G&lang=en")

    # Load the response data into a Python dictionary
    response_data = json.loads(response.text)

    # Get the URL of the first GIF in the search results
    gif_url = response_data['data'][0]['images']['original']['url']

    return gif_url

# searches giphy based upon what you put here
search_term = 'motivation'

# generate a random a meme from giphy
gif_url = generate_meme(search_term)

print(gif_url)


# Set the email parameters
to_email = 'antqdasilva@gmail.com'
from_email = 'qdee508@gmail.com'
subject = subjectOfTheDay()
message = get_random_quote("quotes.txt") + generate_meme(search_term)
body = gif_url

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
server.sendmail(from_email, to_email, msg.as_string(body))

# Disconnect from the server
server.quit()

print('Email sent!')
