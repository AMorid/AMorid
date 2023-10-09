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
            user="your_username",
            password="your_password",
            host="localhost",
            port="5432",
            database="your_database"
        )
        cursor = connection.cursor()
        for message, date_time, name, station in messages:
            cursor.execute(
                "INSERT INTO messages (message, date_time, name, station, approval, review_date_time, moderator_name, moderator_email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (message, date_time, name, station, approval, review_date_time, moderator_name, moderator_email)
            )
        connection.commit()
        cursor.close()
        connection.close()
    except (Exception, psycopg2.Error) as error:
        print("Error while working with the database:", error)
    # url = http: // www.omdbapi.com /?apikey = [yourkey] &= {apikey} & t = {search_term}


