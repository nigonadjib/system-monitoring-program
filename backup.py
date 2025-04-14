import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import datetime
import time
import sqlite3

# Définir le chemin du répertoire courant
path = os.path.dirname(__file__)
file_path = os.path.join(path, 'data.db')

con = sqlite3.connect(file_path)
cursor = con.cursor()

ts = int(time.time())
date = datetime.fromtimestamp(ts).strftime("%d-%m")

print(date)

# Email details
sender_email = "nbenmiri@gmail.com"
receiver_email = "nbenmiri@gmail.com"
password = os.getenv("PASSWORD")

# Create message container
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = f"[ARCHIVE]: Database Backup From {date}"

# Attach file
filename = "data.db"  # Change this to your file name
attachment = open(file_path, "rb")  # Use the full path to the file
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f"attachment; filename={filename}")
msg.attach(part)

# Connect to SMTP server and send email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
text = msg.as_string()
server.sendmail(sender_email, receiver_email, text)
server.quit()

cursor.execute('DELETE FROM Sondes;')

con.commit()
cursor.close()
con.close()
