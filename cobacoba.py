def sungregis():
    sungregis2 = input("Silahkan Registrasi (ya/tidak) : ")
    if (sungregis2 != "ya" and sungregis != "tidak"):
        sungregis()
        if sungregis2.lower == "ya":
            name = input("Masukkan Username Baru : ")
            password = input("Masukkan Password Baru : ")
            register(name,password)
            print("Register berhasil, silahkan login")
sungregis()