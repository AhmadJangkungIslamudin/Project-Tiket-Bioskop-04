import csv

def begin():
    print("=" * 50)
    print("Selamat Datang di Adudu Cinemax")
    print("=" * 50)
    print("Ketik '1' jika anda sudah ingin Login")
    print("Ketik '2' untuk mendaftar")
    print("=" * 50)
    option = str(input("Silahkan masukkan\t:"))
    option = option.lower()
    if option == '1':
        login()
    elif option == '2':
        signup()
    else:
        print('Silahkan Masukkan salah satunya!')
        begin()

def login():
    name = input("Masukkan Username : ")
    password = input("Masukkan Password : ")
    sukses = False
    with open('loginscv.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            a, b = row
            if a == name and b == password:
                sukses = True
                break

    if sukses == True:
        print("=" * 50)
        print("Login berhasil")
        print("=" * 50)
        menu()
        
    else:
        print("=" * 50)
        print("Username atau Password yang anda masukkan salah")
        print("=" * 50)
        login()
    
def signup():
    print("Masukkan Username dan Password anda yang baru")
    name = input("Masukkan Username Baru : ")
    password = input("Masukkan Password Baru : ")
    with open("loginscv.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, password])
    print("=" * 50)
    print("Register berhasil, silahkan login")
    print("=" * 50)
    begin() 

def menu():
    print("Ketik '1' Pemesanan tiket")
    print("Ketik '2' Pusat Bantuan")
    option = input("Pilih menu : ")
    if option == '1':
        with open('Daftar Film.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
        column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]
        for row in data:
            formatted_row = ' | '.join(f"{item:{width}}" for item, width in zip(row, column_widths))
            print(formatted_row)
    elif option == '2':
        print("=")
    else:
        print('\nTidak terdapat dalam menu!\n')
        menu()

begin()