import csv

def menu():
    list_Menu = ["Pemesanan tiket", "Pusat Bantuan"]
    print("1. ", list_Menu[0])
    print("2. ", list_Menu[1])
    print("="*50)
    while (True):
        menu=input("Pilih menu: ")
        if menu == "1":
            file_film = open('Daftar Film.csv','r')
            next(file_film)
            x=1
            film_list =[]
            for i in file_film:
                film = i.split(",")
                film.insert(0,x)
                print(film)
                film_list.append(film)
                x=x+1

            print(film_list)
            film_pilihan = int(input("Masukan kode film"))
            x=0
            for i in range (len(film_list)):
                if film_pilihan == int(film_list[i][0]):
                    film_pilihan = film_list[i]

            print(film_pilihan)


def login(name, password):
    sukses = False
    with open('loginscv.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            a, b = row
            if a == name and b == password:
                sukses = True
                break
    
    if sukses:
        print("=" * 50)
        print("Login berhasil")
        print("=" * 50)
        menu()
            
    else:
        print("=" * 50)
        print("Username atau Password yang anda masukkan salah")
        print("=" * 50)
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