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
conn.commit()
def main():
    # Helaas mij is het niet geukt om een verbiding te maken met postgresSQL.
    parser = argparse.ArgumentParser(description='Moderate passenger messages and store them in the database.')
    parser.add_argument('--moderator_name', type=str, required=True, help='Moderator\'s name')
    parser.add_argument('--moderator_email', type=str, required=True, help='Moderator\'s email')
    parser.add_argument('--approval_status', type=str, choices=['Approved', 'Rejected'], required=True, help='Approval status')

    args = parser.parse_args()

    # Bericheten worden gelezen van mijn text bestanden.
    with open('messages.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            moderate_message(row, args.moderator_name, args.moderator_email, args.approval_status)

if __name__ == "__main__":
    main()
cursor.close()
conn.close()
