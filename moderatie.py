import csv
import argparse
from datetime import datetime

def read_messages(csv_file):
    messages = []
    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            message, date_time, name, station = row
            messages.append((message, date_time, name, station))
    return messages
def write_to_database(messages, approval, review_date_time, moderator_name, moderator_email):
        connection = psycopg2.connect(
            user="postgres",
            password="xxxxxxx",
            host="localhost",
            port_id="5432",
            database="Moderatie"
        )
cursor = connection.cursor()
# kreeg een fout melding hier.
for message, date_time, name, station in messages:
            cursor.execute(
                "INSERT INTO messages (message, date_time, name, station, approval, review_date_time, moderator_name, moderator_email) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (message, date_time, name, station, approval, review_date_time, moderator_name, moderator_email)
            )
        # Bronen die ik gebruikte
        # ChatGPT
        # http://www.spronck.net/pythonbook/pythonboek.pdf
        # https://docs.python.org/3.10/library/csv.html
        # https://www.w3schools.com/python/python_datetime.asp

