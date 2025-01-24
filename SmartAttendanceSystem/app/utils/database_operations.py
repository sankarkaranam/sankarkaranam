import csv
import os

LOG_FILE = 'data/attendance_logs.csv'

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Name'])

def log_attendance(name):
    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["2025-01-24", name])

def get_attendance_logs():
    with open(LOG_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)