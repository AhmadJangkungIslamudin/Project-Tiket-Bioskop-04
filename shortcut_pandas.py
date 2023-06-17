import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import csv
import re


def read(nama_file):
    data = pd.read_csv(nama_file)
    df = pd.DataFrame(data)
    return df

def konf(a,b,c,d,e,f,g,h,i):
    print(
    '''
    ==================================================
                  KONFIRMASI PEMBAYARAN
    ==================================================

      Nama                    : {nama}
      Judul                   : {judul}
      Jam Tayang              : {jamtayang}
      Tanggal Tayang          : {tanggaltayang}
      Jam Pembelian           : {jambeli}
      Tanggal Pembelian       : {tanggalbeli}
      Kursi                   : {kursi}
      Total                   : {total}
      Kode Unik               : {kode}

    ==================================================
    '''.format(nama=a,
            judul=b,
            jamtayang=c,
            tanggaltayang=d,
            jambeli=e,
            tanggalbeli=f,
            kursi=g,
            total=h,
            kode=i
        ))

def kirim_email_struk(a,b,c,d,e,f,g,h,i,email_user):
    isi_email = (
    '''
==================================================
                STRUK PEMBAYARAN
==================================================

  Nama                    : {nama}
  Judul                   : {judul}
  Jam Tayang              : {jamtayang}
  Tanggal Tayang          : {tanggaltayang}
  Jam Pembelian           : {jambeli}
  Tanggal Pembelian       : {tanggalbeli}
  Kursi                   : {kursi}
  Total                   : {total}
  Kode Unik               : {kode}

==================================================
TERIMA KASIH {nama} TELAH MEMESAN DI ADUDU CINEMAX
==================================================
    '''.format(nama=a,
            judul=b,
            jamtayang=c,
            tanggaltayang=d,
            jambeli=e,
            tanggalbeli=f,
            kursi=g,
            total=h,
            kode=i))
     
    ngirim_email(isi_email,email_user, jenis=2) 

def ngirim_email(body_email,email_user,jenis):
    # Konfigurasi
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    SMTP_USERNAME = 'bioskopadudu@gmail.com' #Email Pengirim
    SMTP_PASSWORD = 'bqeseknufgjpsxkr' #Password SMTP EMAIL
    SENDER_EMAIL = 'bioskopadudu@gmail.com' # Email Pengirim

    # Membuat pesan email
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = email_user
    msg['Subject'] = 'ADUDU CINEMAX'

    if jenis == 1:
        body = '''
==================================================

      TERIMA KASIH TELAH MELAKUKAN PEMESANAN 
BERIKUT MERUPAKAN KODE KONFIRMASI PEMBAYARAN ANDA
                    {HASIL}

==================================================
        '''.format(HASIL = body_email )

    elif jenis == 2:
        body = body_email
    elif jenis == 3:
        body = '''
==================================================

          PESANAN ANDA BERHASIL DIBATALKAN
TERIMA KASIH {Username} TELAH MEMESAN DI ADUDU CINEMAX

==================================================
        '''.format(Username = body_email)

    elif jenis == 4:
        body = '''
==================================================

     TERIMA KASIH TELAH MELAKUKAN PENDAFTARAN 
BERIKUT MERUPAKAN KODE KONFIRMASI OTP REGISTRASI ANDA
                    {HASIL}

     JANGAN BERIKAN KODE INI PADA ORANG LAIN!

==================================================
        '''.format(HASIL = body_email )

    msg.attach(MIMEText(body, 'plain'))
    simple_email_contatcs = ssl.create_default_context()
    try:
        print("\nConnecting to server ... ")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls(context=simple_email_contatcs)
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, email_user, text)
        server.quit()
        print('Kode terkirim di email. Silahkan periksa email anda')
    except Exception as e:
        print('Email gagal dikirim:', str(e))

    
def get_email_by_username(username):
    with open('login.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                return row[2]  # Mengembalikan email dari baris yang sesuai dengan username
    return None  # Jika username tidak ditemukan


def kodeUnikDikirim(kodeUnik):
    kode_unik = kodeUnik
    list_kode = list(kode_unik)
    list_kode.reverse()
    hasil = ''.join(list_kode[:5])
    return hasil

def email_form(email):
    # Pola regular expression untuk validasi alamat email
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False

