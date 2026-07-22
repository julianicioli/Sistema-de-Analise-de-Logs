def detect_sucess_after_failures(logs):
    failed_attempts = {}
    alerts = []

    for log in logs:
        log = log.strip()

        if not log: 
            continue
        timestamp, event, ip = log.split(" | ")

        if event == "LOGIN_FAIL":
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1
        elif event == "LOGIN_SUCESS":
            if failed_attempts.get(ip, 0) >= 3:
                alerts.append({
                    "ip": ip,
                    "attempts": failed_attempts[ip],
                    "timestamp": timestamp
                })
    return alerts    