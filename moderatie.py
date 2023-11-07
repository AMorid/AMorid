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
# Helaas mij is het niet geukt(niet geleerd) om een verbiding te maken met postgresSQL.


