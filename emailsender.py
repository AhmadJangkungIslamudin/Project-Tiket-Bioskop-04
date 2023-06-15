import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import re

# Konfigurasi
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'bioskopadudu@gmail.com' #Email Pengirim
SMTP_PASSWORD = 'bqeseknufgjpsxkr' #Password SMTP EMAIL
SENDER_EMAIL = 'bioskopadudu@gmail.com' # Email Pengirim

def validate_email(email):
    # Pola regular expression untuk validasi alamat email
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# Meminta input dari pengguna untuk alamat email penerima
while True:
    RECIPIENT_EMAIL = input("Masukkan Email Anda: ")
    if validate_email(RECIPIENT_EMAIL):
        break
    else:
        print("Alamat email tidak valid. Silakan coba lagi.")


# Membuat pesan email
msg = MIMEMultipart()
msg['From'] = SENDER_EMAIL
msg['To'] = RECIPIENT_EMAIL
msg['Subject'] = 'REKAP PEMESANAN'

body = 'Halo, ini adalah contoh email 2.'
msg.attach(MIMEText(body, 'plain'))
simple_email_contatcs = ssl.create_default_context()

# Mengirim email menggunakan SMTP
try:
    print("Connecting to server ... ")
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls(context=simple_email_contatcs)
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    text = msg.as_string()
    server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, text)
    server.quit()
    print('Email berhasil dikirim!')
except Exception as e:
    print('Email gagal dikirim:', str(e))
