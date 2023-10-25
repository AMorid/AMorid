import csv
import psycopg2
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
    try:
        connection = psycopg2.connect(
            user="MoridA",
            password="********",
            host="localhost",
            port="5432",
            database="Moderatie"
        )
