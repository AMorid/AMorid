import csv
import datetime
import random

stations = ["Station A", "Station B", "Station C"]
def enter_message():
    message = input("Enter your message (up to 140 characters): ")
    if len(message) > 140:
        print("The message is too long. Please try again.")
        return
    date_time = datetime.datetime.now()
    traveler_name = input("Enter your name (leave empty for 'anonymous'): ")
    if not traveler_name:
        traveler_name = "anonymous"
    station = random.choice(stations)
    return message, date_time, traveler_name, station

def save_message(message):
    with open('messages.csv', mode='a', newline='') as messages_file:
        messages_writer = csv.writer(messages_file)
        messages_writer.writerow(message)

