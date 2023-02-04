from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import pandas
from pandas import Series
import yagmail
import time
from datetime import datetime

# Gmail part
sender = "GOOGLE_SENDER_EMAIL"
# generate app in gmail secure apps
my_password = "SENDER_PATH"
# Disposable email
# receiver = "cocijam768@ezgiant.com"
receiver = "RECEIVER_EMAIL"


def generate_file(filename, content):
    with open(filename, mode="w") as file:
        file.write(str(content))


yag = yagmail.SMTP(user=sender, password=my_password)


def parse_contacts(row: Series):
    return row["name"], row["email"], row["amount"]


def send_email(email_client, rec_email, content, subject="This is a subject"):
    email_client.send(to=rec_email, subject=subject, contents=content)
    print("Email send")


def generate_content(name, filename, amount):
    return [
        f"""
    Here is a content of email
    Hi {name}! You need to pay for the service {amount}$
    Have a good day
    """,
        filename,
    ]


rows = pandas.read_csv("contacts.csv")


def main():
    for index, row in rows.iterrows():
        name, rec_email, amount = parse_contacts(row)
        filename = f"{name}.txt"
        generate_file(filename, amount)

        content = generate_content(name, filename, amount)
        while True:
            current_time = datetime.now()
            if current_time.hour == 13 and current_time.minute == 43:
                send_email(yag, rec_email, content)
                time.sleep(60)


# Outlook part
sender = "OUTLOOK_EMAIL"
my_password = "PASSWORD"

message = MIMEMultipart()
message["From"] = sender
message["To"] = receiver
message["Subject"] = "Hello from Outlook"

body = """
<h1>Some Beautiful text is going here</h1>
There are only 1 air alarm today.
Let's hope for it stays the same.
"""

minetext = MIMEText(body, "html")
message.attach(minetext)

attachment_path = "dog.jpeg"
attachment_file = open(attachment_path, "rb")
payload = MIMEBase("application", "octate-stream")
payload.set_payload(attachment_file.read())
encoders.encode_base64(payload)
payload.add_header("Content-Disposition", "attachment", filename=attachment_path)
message.attach(payload)

with smtplib.SMTP("smtp.office365.com", 587) as server:
    server.starttls()
    server.login(sender, my_password)
    message_text = message.as_string()
    server.sendmail(sender, receiver, message_text)
