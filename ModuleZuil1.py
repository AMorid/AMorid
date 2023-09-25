import csv
# https://docs.python.org/3.10/library/csv.html
import datetime
# https://www.w3schools.com/python/python_datetime.asp
import random

# https://docs.python.org/3/library/random.html
# stations = ["Amsterdam", "Utrecht", "Leiden", "Groningen"]


# def enter_message():
    # message = input("Write your message (no more than 140 characters): ")
    # if len(message) > 140:
        # print("Your message is too long. Try again.")
       # return
    # import datetime
    # x = datetime.datetime.now()
    # https: // www.w3schools.com / python / python_datetime.asp
    # date_time = datetime.datetime.now()
    # passenger_name = input("Write your name (or leave it empty for 'anonymous'): ")
    # if not passenger_name:
      #  passenger_name = "anonymous"
    # station = random.choice(stations)
    #return message, date_time, passenger_name, station

import csv
import datetime
import random

stations = ["Amsterdam", "Utrecht", "Leiden", "Groningen"]
def enter_message():
    message = input("Write your message (no more than 140 characters): ")
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

save_message(enter_message())
def save_message_cvs():
    with open('messages.csv', mode='a', newline='') as messages_file:
        messages_writer = csv.writer(messages_file)
        messages_writer.writerow(messages_writer)

