import json
import psutil
import smtplib
from email.mime.text import MIMEText


def send_alert(sender_email, receiver_email, smtp_server, smtp_port, smtp_username, smtp_password, message):
    # Creating an email message
    msg = MIMEText(message)
    msg['Subject'] = 'Server Resource Alert'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Sending an email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

def monitor_resources(config):
    # Monitor CPU usage
    cpu_percent = psutil.cpu_percent()

    # Monitor memory usage
    memory_percent = psutil.virtual_memory().percent

    # Monitor disk usage
    disk_percent = psutil.disk_usage('/').percent

    # Compare threshold values from the config file and send alerts if usgae exceeds
    if cpu_percent > config['Thresholds']['cpu_threshold']:
        send_alert(config['Email']['sender_email'], config['Email']['receiver_email'], config['Email']['smtp_server'], config['Email']['smtp_port'], config['Email']['smtp_username'], config['Email']['smtp_password'], f'CPU usage exceeded threshold: {cpu_percent}%')

    if memory_percent > config['Thresholds']['memory_threshold']:
        send_alert(config['Email']['sender_email'], config['Email']['receiver_email'], config['Email']['smtp_server'], config['Email']['smtp_port'], config['Email']['smtp_username'], config['Email']['smtp_password'], f'Memory usage exceeded threshold: {memory_percent}%')

    if disk_percent > config['Thresholds']['disk_threshold']:
        send_alert(config['Email']['sender_email'], config['Email']['receiver_email'], config['Email']['smtp_server'], config['Email']['smtp_port'], config['Email']['smtp_username'], config['Email']['smtp_password'], f'Disk usage exceeded threshold: {disk_percent}%')

if __name__ == "__main__":
    # Parsing configurations from config.json
    with open('config.json') as f:
        config = json.load(f)

    # Monitor server resources and send alerts if these resources exceed the predefined threshold
    monitor_resources(config)
