import pandas as pd

data = []

def log_honeypot_activity(ip, port, timestamp):
    data.append({"IP": ip, "Port": port, "Timestamp": timestamp})
    df = pd.DataFrame(data)
    df.to_csv("honeypot_logs.csv", index=False)

# Məlumatları nümunə üçün əlavə edin:
log_honeypot_activity("192.168.1.1", 8080, "2024-12-25 10:00:00")
log_honeypot_activity("10.0.0.2", 22, "2024-12-25 10:10:00")
