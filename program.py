#LOGIN
def login(name,password):
    sukses = False
    file = open('logindatabase.txt','r')
    for i in file:
        a,b = i.split(",") #split utk ambil id dan passwrd. (,) untuk pemisah antara id dan paswd
        b = b.strip()
        if (a == name and b == password):
            sukses = True
            break
    file.close()

    if(sukses):
        print("="*50)
        print("Login berhasil")
        print("="*50)
    else:
        print("="*50)
        print("Anda belum terdaftar, silahkan registrasi")
        print("="*50)
        #langsung regis
        sungregis2 = input("Silahkan Registrasi (ya/tidak) : ")
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
         

def register(name,password): #3
    file = open("logindatabase.txt","a")
    file.write("\n"+name+","+password)

def access(option): #2
    global name 
    if (option == "login"):
        name = input("Masukkan Username : ")
        password = input("Masukkan Password : ")
        login(name,password)
    else:
        print("Masukkan Username dan Password anda yang baru")
        name = input("Masukkan Username Baru : ")
        password = input("Masukkan Password Baru : ")
        register(name,password) #3
        print("Register berhasil, silahkan login")      

def begin(): #1
    global option
    print()
    print("="*50)
    print("Selamat Datang di Adudu Cinemax")
    print("="*50)
    print("Ketik 'login' jika anda sudah punya akun")
    print("Ketik 'registrasi' jika anda belum punya akun")
    print("="*50)
    option = input("Silahkan masukkan (login/registrasi) : ")
    if (option != "login" and option != "registrasi"):
        begin()

begin() #1
access(option) #2