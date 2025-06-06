import json
import csv
import os

CSV_PATH = 'dataset/attack_logs.csv'
JSON_PATH = 'logs/attacker.json'

def log_event(event):
    # Append to JSON
    with open(JSON_PATH, 'a') as jf:
        jf.write(json.dumps(event) + "\n")

    # Append to CSV
    write_header = not os.path.exists(CSV_PATH)
    with open(CSV_PATH, 'a', newline='') as cf:
        writer = csv.DictWriter(cf, fieldnames=event.keys())
        if write_header:
            writer.writeheader()
        writer.writerow(event)
