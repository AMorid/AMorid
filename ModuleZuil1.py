import csv
import datetime
import random
stations = ["Amsterdam CS", "Utrecht CS", "Leiden CS"]
def type_your_message_():
    message = input("Write a message of maximum 140 characters in: ")
    if len(message) > 140:
        print("Your message is too long. Try again.")
        return
    date_time = datetime.datetime.now()
    name = input("Type your name (Or leave it 'anonymous'): ")
    if not name:
        name = "anonymous"
    station = random.choice(stations)
    return message, date_time, name, station
def save_messages(message):
    with open('messages.csv', mode='a', newline='') as message_file:
        message_Writer = csv.writer(message_file)
        message_Writer.writerow(message)

