import time
import os
import psutil
import sqlite3
import uuid
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

cpu_usage = ram_usage = free_disk_space = number_processes = number_active_users = 0
max_cpu_usage = max_ram_usage = min_free_disk_space = max_number_processes = max_number_active_users = 0
epoch = int(time.time())
mac_address = hex(uuid.getnode())[2:]
table_name = "Sondes"

sender = "nbenmiri@gmail.com"
password = os.getenv("PASSWORD")
receiver = "nbenmiri@gmail.com"
alert_message = {
    "object": "",
    "body": "",
}

# Définir le chemin du répertoire courant
db_path = os.path.join(os.path.dirname(__file__), 'data.db')

con = sqlite3.connect(db_path)
cursor = con.cursor()

cursor.execute('SELECT History_Limit FROM Config;')
history_limit = cursor.fetchone()[0]

def create_table():
    query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
    Timestamp INTEGER,
    MAC_Address TEXT,
    Public_IP_Address TEXT,
    CPU_Usage REAL,
    RAM_Usage REAL,
    Free_Disk_Space REAL,
    Number_Processes INTEGER,
    Number_Active_Users INTEGER,
    PRIMARY KEY (Timestamp, MAC_Address)
);
"""
    cursor.execute(query)

def collect_data():
    global cpu_usage, ram_usage, free_disk_space, number_processes, number_active_users
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    free_disk_space = round(psutil.disk_usage('/').free / 2**30, 2)
    number_processes = len(psutil.pids())
    number_active_users = len(os.popen("who").readlines())

def limit_history():
    query = f"SELECT COUNT(*) FROM {table_name}"
    cursor.execute(query)
    count = cursor.fetchone()[0]
    if count > history_limit:
        query = f"DELETE FROM {table_name} WHERE Timestamp <= (SELECT MIN(Timestamp) FROM {table_name})"
        for _ in range(count - history_limit):
            cursor.execute(query)

def retrieve_config():
    global max_cpu_usage, max_ram_usage, min_free_disk_space, max_number_processes, max_number_active_users
    
    query = f"SELECT CPU_Usage FROM Config"
    cursor.execute(query)
    max_cpu_usage = cursor.fetchone()[0]

    query = f"SELECT RAM_Usage FROM Config"
    cursor.execute(query)
    max_ram_usage = cursor.fetchone()[0]

    query = f"SELECT Free_Disk_Space FROM Config"
    cursor.execute(query)
    min_free_disk_space = cursor.fetchone()[0]

    query = f"SELECT Number_Processes FROM Config"
    cursor.execute(query)
    max_number_processes = cursor.fetchone()[0]

    query = f"SELECT Number_Active_Users FROM Config"
    cursor.execute(query)
    max_number_active_users = cursor.fetchone()[0]

def send_alert():
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = alert_message["object"]

    body = alert_message["body"]
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls() 
        server.login(sender, password)
        text = message.as_string()
        server.sendmail(sender, receiver, text)

def set_alert():
    if cpu_usage > max_cpu_usage:
        alert = True
        alert_message["object"] = "[ALERT]: CPU Overuse"
        alert_message["body"] = f"""Hello admin, we would like to inform you that the machine with the mac address: {mac_address} is overusing its CPU power.

        Maximum Allowed CPU Usage: {max_cpu_usage}
        Current CPU Usage: {cpu_usage}
        """
        send_alert()

    if ram_usage > max_ram_usage:
        alert = True
        alert_message["object"] = "[ALERT]: RAM Overuse"
        alert_message["body"] = f"""Hello admin, we would like to inform you that the machine with the mac address: {mac_address} is overusing its RAM capacity.

        Maximum Allowed RAM Usage: {max_ram_usage}
        Current RAM Usage: {ram_usage}
        """
        send_alert()

    if free_disk_space < min_free_disk_space:
        alert = True
        alert_message["
