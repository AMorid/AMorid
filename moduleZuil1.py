import csv
import datetime
import random
stations = ["Amsterdam", "Utrecht", "Leiden", "Groningen"]
def enter_message():
    message = input("Write your message(no more than 140 characters): ")
    if len(message) > 140:
        print("Your message is too long. Try again.")
        return
    date_time = datetime.datetime.now()
    passenger_name = input("Write your name (or leave it empty for 'anonymous'): ")
    if not passenger_name:
        passenger_name = "anonymous"
    station = random.choice(stations)
    return message, date_time, passenger_name, station
def save_message(message):
    with open('messages.csv', mode='a', newline='') as messages_file:
        messages_writer = csv.writer(messages_file)
        messages_writer.writerow(message)
    print(message)
# Kleine deel van de line 43 geïnspireerd door ChatGpT.
save_message(enter_message())
def save_message_cvs():
    with open('messages.csv', mode='a', newline='') as messages_file:
        messages_writer = csv.writer(messages_file)
        messages_writer.writerow(messages_writer)
        # Bronen die gebruikte
        # ChatGPT
        # https://docs.python.org/3.10/library/csv.html
        # https://www.w3schools.com/python/python_datetime.asp