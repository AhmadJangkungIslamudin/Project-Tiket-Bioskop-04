import csv

def MENU():
    with open('nama_file.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
    column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]
    for row in data:
        formatted_row = ' | '.join(f"{item:{width}}" for item, width in zip(row, column_widths))
        print(formatted_row)
    
    with open('file_rapi.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def login(name, password):
    sukses = False
    with open('loginscv.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            a, b = row
            if a == name and b == password:
                sukses = True
                break
    
    if(sukses):
        print("="*50)
        print("Login berhasil")
        print("="*50)
        menu()
    else:
        print("="*50)
        print("Anda belum terdaftar, silahkan registrasi")
        print("="*50)
        #langsung regis
        sungregis2 = input("Silahkan Registrasi (ya/tidak) : ")
        sungregis2 = sungregis2.lower()
        if (sungregis2 != "ya" and sungregis2 != "tidak"):
            return sungregis2

        if (sungregis2 == "ya"):
            name = input("Masukkan Username Baru : ")
            password = input("Masukkan Password Baru : ")
            register(name,password) #3
            print("="*50)
            print("Register berhasil, silahkan login")
            print("="*50)
            access(option)

        else:
            print("="*50)
            print("Terima kasih telah menggunakan layanan kami")
            print("="*50)

def register(name, password):
    with open("loginscv.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, password])

def access(option):
    global name
    if option == "login":
        name = input("Masukkan Username : ")
        password = input("Masukkan Password : ")
        login(name, password)
    else:
        print("Masukkan Username dan Password anda yang baru")
        name = input("Masukkan Username Baru : ")
        password = input("Masukkan Password Baru : ")
        register(name, password)
        print("=" * 50)
        print("Register berhasil, silahkan login")
        print("=" * 50)

def begin():
    global option
    print("=" * 50)
    print("Selamat Datang di Adudu Cinemax")
    print("=" * 50)
    print("Ketik 'login' jika anda sudah punya akun")
    print("Ketik 'registrasi' jika anda belum punya akun")
    print("=" * 50)
    option = input("Silahkan masukkan (login/registrasi) : ")
    option = option.lower()
    if option != "login" and option != "registrasi":
        return begin()

begin()
access(option)

#=============================================================
def mENU():
    with open('nama_file.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
    column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]
    for row in data:
        formatted_row = ' | '.join(f"{item:{width}}" for item, width in zip(row, column_widths))
        print(formatted_row)
    
    with open('file_rapi.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)