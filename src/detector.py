from datetime import datetime

def detect_suspicious_hours(logs):
    suspicious_hours = []

    for log in logs:
        log = log.strip()
        if not log:
            continue

        timestamp, event, ip = log.split(" | ")
        date = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

        if event == "LOGIN_FAIL" and 0 <= date.hour <= 5:
            suspicious_hours.append({
                "ip": ip,
                "hour": date.hour,
                "timestamp": timestamp
            })

    return suspicious_hours
