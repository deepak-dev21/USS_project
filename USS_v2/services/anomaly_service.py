def detect_anomaly(data):
    suspicious = ["DROP", "DELETE", "INSERT", "--"]

    for word in suspicious:
        if word in data.upper():
            return True
    return False