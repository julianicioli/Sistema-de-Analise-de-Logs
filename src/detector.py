from collections import defaultdict
from datetime import datetime


def detect_hours(logs):
    failed_attempts = defaultdict(int)
    hours = []

    for log_entry in logs:
        log_entry = log_entry.strip()
        if not log_entry:
            continue

        timestamp, event, ip = log_entry.split(" | ")
        date = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

        if event == "LOGIN_FAIL":
            failed_attempts[ip] += 1
            attempts = failed_attempts[ip]

            if 0 <= date.hour <= 5 and 3 <= attempts <= 5:
                hours.append({
                    "ip": ip,
                    "hour": date.hour,
                    "timestamp": timestamp,
                    "attempts": attempts,
                })

    return hours
