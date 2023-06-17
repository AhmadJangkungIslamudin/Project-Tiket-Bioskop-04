import csv
import pandas as pd
import datetime 
import random
import ast
import shortcut_pandas as ps
import re

def begin():
    print("=" * 50)
    print("\n          SELAMAT DATANG DI ADUDU CINEMAX\n")
    print("=" * 50)
    print("Ketik '1' jika anda sudah ingin Login")
    print("Ketik '2' untuk mendaftar")
    print("=" * 50)
    while True:
        option = (input("Silahkan masukkan : "))
        if option == '1':
            login()
            break
        elif option == '2':
            signup()
            break
        else:
            print('Input tidak valid')
            

def login():
    global name
    global email_user
    name = input("Masukkan Username : ")
    password = input("Masukkan Password : ")
    sukses = False
    with open('login.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            a, b, c = row
            if a == name and b == password:
                sukses = True
                break

    if sukses == True:
        print("=" * 50)
        print("                 LOGIN BERHASIL")
        print("=" * 50)
        email_user = ps.get_email_by_username(name)
        menu()
        
    else:
        print("=" * 50)
        print(" Username atau Password yang anda masukkan salah")
        print("=" * 50)
        login()



def signup():
    print("\nMasukkan data diri anda!")
    name = input("Masukkan Username Baru : ")
    password = input("Masukkan Password Baru : ")
    email = input("Masukkan Email Baru    : ")
    if ps.email_form(email):
        pass
    else:
        print("\nAlamat email tidak valid. Silakan coba lagi.")
        signup()
    
    kode_otp = str(random.randint(10000000, 99999999))    
    kodeotp = ps.kodeUnikDikirim(kode_otp)
    ps.ngirim_email(kodeotp,email,jenis=4)
    while True:
        verif = input('Masukkan kode OTP Registrasi yang dikirim ke email anda : ')
        if verif == kodeotp:
            print("=" * 50)
            print("        Register berhasil, silahkan login")
            print("=" * 50)
            print()
            with open("login.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([name, password,email])
            begin() 
        else:
            print("Kode OTP tidak valid, silahkan input dengan benar!\n")

def menu():
    global opsi_transaksi
    print('\nMENU')
    print("Ketik '1' Pemesanan tiket")
    print("Ketik '2' Pusat Bantuan")
    print("Ketik '3' Keluar")
<<<<<<< HEAD
    option = input("\nPilih menu : ")
    if option == '1':
        opsi_transaksi = 1
        with open('Daftar Film.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
        column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]
        for row in data:
            formatted_row = ' | '.join(f"{item:{width}}" for item, width in zip(row, column_widths))
            print('='*83)
            print(formatted_row)
        print('='*83)
        pilihfilm('1')
    elif option == '2':
        pusat_bantuan()
    elif option == '3':
        print('''\n====================================================    
TERIMA KASIH TELAH MENGGUNAKAN LAYANAN ADUDU CINEMAX!
====================================================\n''')
    else:
        print('\nTidak terdapat dalam menu!')
        menu()
=======
    while True:
        option = input("\nPilih menu : ")
        if option == '1':
            opsi_transaksi = 1
            with open('Daftar Film.csv', 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                data = list(reader)
            column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]
            for row in data:
                formatted_row = ' | '.join(f"{item:{width}}" for item, width in zip(row, column_widths))
                print('='*83)
                print(formatted_row)
            print('='*83)
            pilihfilm('1')
            break
        elif option == '2':
            pusat_bantuan()
            break
        elif option == '3':
            print('''\n====================================================    
TERIMA KASIH TELAH MENGGUNAKAN LAYANAN ADUDU CINEMAX!
====================================================\n''')
            break
        else:
            print('\nTidak terdapat dalam menu!')
            
>>>>>>> bd9312296a8bb79cd7d90788c64fe4cb2f8b5926

def pusat_bantuan():
    global kode_pembayaran, kode_pembayaran_lama
    global opsi_transaksi
    kode_pembayaran = (input("\nMasukan kode unik anda : "))
    kode_pembayaran_lama = kode_pembayaran
    sukses = False
    with open('riwayat pembelian.csv', 'r') as file:
        next(file)
        reader = csv.reader(file)
        for row in reader:
            if row[0] == kode_pembayaran_lama:
                sukses = True
                break
    if sukses == True:
        print("\nKetik '1' Reschedule")
        print("Ketik '2' Cancel & Refund")
        option = (input("\nPilih menu : "))
<<<<<<< HEAD
        #while True:
        if option == "1":
            print("Anda memilih RESCHEDULE")
            pilihfilm('2')
        elif option == "2":
            print("Anda memilih CANCEL & REFUND")
            pilihfilm('3')
        else:
            print("Menu tidak tersedia")
            pusat_bantuan()
=======
        while True:
            if option == "1":
                print("Anda memilih RESCHEDULE")
                pilihfilm('2')
                break
            elif option == "2":
                print("Anda memilih CANCEL & REFUND")
                pilihfilm('3')
                break
            else:
                print("Menu tidak tersedia")
                pusat_bantuan()
                break
>>>>>>> bd9312296a8bb79cd7d90788c64fe4cb2f8b5926
    else:
        print('gagal')
        pusat_bantuan()        

def pilihfilm(opsimenu):
    global film_dipilih, list_kursi_pilihan, df,list_kursi,index_pembelian,dfPembelian,list_kursi_pilihan
    list_kursi = ["A1","A2","A3","A4","A5","A6","A7","A8","B1","B2","B3","B4","B5","B6","B7","B8","C1","C2","C3","C4","C5","C6","C7","C8","D1","D2","D3","D4","D5","D6","D7","D8","E1","E2","E3","E4","E5","E6","E7","E8"]
    list_kursi_pilihan =[]

    def reset_kursi():
        global df, film_dipilih,dfPembelian,index_pembelian, list_kursi_pilihan
        dfPembelian = ps.read('riwayat pembelian.csv')
        index_pembelian=dfPembelian.index[(dfPembelian['kode'] == kode_pembayaran)].tolist()                    
        ps.konf(name,
                dfPembelian.iloc[index_pembelian[0],3],
                dfPembelian.iloc[index_pembelian[0],4],
                str(dfPembelian.iloc[index_pembelian[0],5])+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().year),
                '-',
                dfPembelian.iloc[index_pembelian[0],2],
                dfPembelian.iloc[index_pembelian[0],8],
                '-',
                kode_pembayaran)

        df = ps.read('Data Jadwal.csv')
        index_data=df.index[(df['jam'] == dfPembelian.iloc[index_pembelian[0],4]) & 
                            (df['tanggal'] == dfPembelian.iloc[index_pembelian[0],5])& 
                            (df['judul'] == dfPembelian.iloc[index_pembelian[0],3])].tolist()

        list_kursi_pilihan = ast.literal_eval(dfPembelian.values[index_pembelian[0],8])
        film_dipilih = dfPembelian.iloc[index_pembelian[0],3]

    def print_layout(checklist):
        global index_data
        index_data=df.index[(df['jam'] == input_jam_pilihan) & (df['tanggal'] == tanggal_pilihan)& (df['judul'] == film_dipilih)].tolist()
        #print(index_data)
        nama_kolom = ["A","B","C","D","E"]
        nama_baris = [1,2,3,4,5,6,7,8]
<<<<<<< HEAD
=======
        print('''\n=====================================
============    LAYAR    ============\n''')
        x=0
>>>>>>> bd9312296a8bb79cd7d90788c64fe4cb2f8b5926
        if opsimenu == '1':
            print('''\n=====================================
============    LAYAR    ============\n''')
            x=0
            for i in nama_kolom:
                for j in nama_baris:
                    if df.iloc[index_data[0],5:45].values[x] == 1:
                        print(i,end="")
                        print(j,end="   ")
                    elif df.iloc[index_data[0],5:45].values[x] == 0:
                        print("|x|",end=' ')
                    x=x+1
                print()

    def pilih_tanggal():
        global tanggal_pilihan, df
        #=== BACA DATA TANGGAL
        df = ps.read('Data Jadwal.csv')
        #=== PILIH TANGGAL
        tanggal_tersedia=list(set(df.loc[(df['judul'] == film_dipilih)].tanggal))
        print('\nTanggal')
        print(tanggal_tersedia)
<<<<<<< HEAD
        try:
            tanggal_pilihan = int(input("\nMasukan Tanggal pilihan : "))
            if tanggal_pilihan in tanggal_tersedia and tanggal_pilihan>=datetime.datetime.now().day:
                if tanggal_pilihan==datetime.datetime.now().day and datetime.datetime.now().time() >= datetime.time(16, 0):
                    print('Tidak ada jam tayang')
                    pilih_tanggal()
                else:
                    print("success")
                    pilih_jam()        
            else:
                print("Tanggal tidak tersedia")
                pilih_tanggal()
        except ValueError:
            print('Input tidak valid')
=======
        tanggal_pilihan = int(input("\nMasukan Tanggal pilihan : "))
        if tanggal_pilihan in tanggal_tersedia and tanggal_pilihan>=datetime.datetime.now().day:
            if tanggal_pilihan==datetime.datetime.now().day and datetime.datetime.now().time() >= datetime.time(16, 0):
                print('Tidak ada jam tayang')
                pilih_tanggal()
            else:
                print("success")
                pilih_jam()
        #misal selain integer eror        
        else:
            print("Tanggal tidak tersedia")
>>>>>>> bd9312296a8bb79cd7d90788c64fe4cb2f8b5926
            pilih_tanggal()

    def pilih_jam():
        global input_jam_pilihan
        #=== BACA DATA TANGGAL
        df = ps.read('Data Jadwal.csv')
        #=== PILIH JAM
        jam_tersedia=list(set(df.loc[(df['judul'] == film_dipilih)&(df['tanggal'] == tanggal_pilihan)].jam))
        print('\nWaktu')
        print(jam_tersedia)
        try:
            input_jam_pilihan = input("\nMasukan jam pilihan anda : ")
            jam_pilihan = datetime.datetime.strptime(input_jam_pilihan, "%H:%M").time()
        except:
            print("Input tidak sesuai")
            pilih_jam()

        if input_jam_pilihan in jam_tersedia and (jam_pilihan>=datetime.datetime.now().time() or tanggal_pilihan>datetime.datetime.now().day):
            print("success")
            print_layout('')
            pilih_kursi()
        else:
            print("Jam tidak tersedia")
            pilih_jam()
    
    #=== PILIH KURSI
    
    def pilih_kursi():
        if opsimenu == '1':
            df = ps.read('Data Jadwal.csv')
            while True:
                try:
                    kursi_pilihan = input("\nPilih kursi anda. Ketik 'confirm' jika sudah selesai : ")
                    if kursi_pilihan == "confirm" and len(list_kursi_pilihan) == 0:
                        print("Pilih minimal satu kursi")
                    elif kursi_pilihan == "confirm":
                        print(list_kursi_pilihan)
                        ringkasan_beli()
                        break
                    elif kursi_pilihan in list_kursi_pilihan or df.iloc[index_data[0],5:45].values[list_kursi.index(kursi_pilihan)]==0:
                        print("Kursi tidak tersedia / sudah dipilih")
                    elif kursi_pilihan in list_kursi and df.iloc[index_data[0],5:45].values[list_kursi.index(kursi_pilihan)]==1:
                        list_kursi_pilihan.append(kursi_pilihan)
                        print(list_kursi_pilihan)
                except ValueError:
                    print('Input tidak valid')
                    pilih_kursi()
        elif opsimenu == '2':
            ringkasan_beli()
    
#==== Ringkasan beli
    def ringkasan_beli():
        print('''
====================================
           Ringkasan Order
====================================

  Judul   : {judul}
  Jam     : {jam}
  Tanggal : {tanggal}
  Bulan   : {bulan}
  Tahun   : {tahun}
  Kursi   : {kursi}

====================================
        '''.format(judul=film_dipilih,
                jam=input_jam_pilihan,
                tanggal=tanggal_pilihan,
                bulan=datetime.datetime.now().month,
                tahun=datetime.datetime.now().year,
                kursi=list_kursi_pilihan))
        while True:
            konfirmasi_bayar = input("Apakah anda ingin melanjutkan pembayaran? (y/n) : ")
            if konfirmasi_bayar == 'y':
                print("TRANSAKSI")
                transaksi(opsimenu)
<<<<<<< HEAD
                break
            elif konfirmasi_bayar == 'n':
                menu()
                break
=======
                return
            elif konfirmasi_bayar == 'n':
                menu()
>>>>>>> bd9312296a8bb79cd7d90788c64fe4cb2f8b5926
            else:
                print('Input tidak valid')
    #=======================================================
    # BACA DAFTAR FILM
    if opsimenu == "1":
        df = ps.read('Daftar Film.csv')
        # INPUT FILM
<<<<<<< HEAD
        try:
            inputan=int(input("\nMasukkan no Film (1-6) : "))-1
            if inputan in range (6):
                film_dipilih = df.iloc[inputan,1]
                print(film_dipilih)
                pilih_tanggal()
            else:
                print('Input tidak valid')
                pilihfilm(opsimenu)
        except ValueError:
            print('Input tidak valid')
            pilihfilm(opsimenu)
=======
        inputan=int(input("\nMasukkan no Film (1-6) : "))-1
        if inputan in range (6):
            film_dipilih = df.iloc[inputan,1]
            print(film_dipilih)
            pilih_tanggal()
        else:
            print('Input tidak valid')
>>>>>>> bd9312296a8bb79cd7d90788c64fe4cb2f8b5926
    elif opsimenu == '2':
        reset_kursi()
        pilih_tanggal()
    elif opsimenu == '3':
        reset_kursi()
        transaksi(opsimenu)
        return

def transaksi(jenis_transaksi):
    jambeli = datetime.datetime.now().strftime('%H:%M') #jambeli
    tanggalbeli = datetime.datetime.now().strftime('%d-%m-%Y') #tanggalbeli
    totalbeli = (int(len(list_kursi_pilihan))*25000)
    kode_unik = str(random.randint(10000000, 99999999))

    if jenis_transaksi =='1':
        kode_pembayaran = "TK"+ kode_unik       
        ps.konf(name,
                film_dipilih,
                str(input_jam_pilihan),
                str(tanggal_pilihan)+datetime.datetime.now().strftime('-%m-%Y'),
                jambeli,
                tanggalbeli,
                list_kursi_pilihan,
                totalbeli,
                kode_pembayaran)
        
        while True:
            konfirmasi_bayar = input("Bayar? (y/n) : ")
            if konfirmasi_bayar == 'y':
                codeSended = ps.kodeUnikDikirim(kode_unik)
                ps.ngirim_email(codeSended,email_user,jenis=1)
                break
            elif konfirmasi_bayar == 'n':
                konfirmasi_bayar2 = input('Yakin ingin membatalkan pesanan? (y/n) : ')
                if konfirmasi_bayar2 == 'y':
                    menu()
<<<<<<< HEAD
                    break
=======
>>>>>>> bd9312296a8bb79cd7d90788c64fe4cb2f8b5926
                elif konfirmasi_bayar2 != 'n':
                    print('Input tidak valid')
            else:
                print('Input tidak valid')
        
        while True:
            kode_bayar = str(input("\nMasukan Kode Konfirmasi Pembayaran (5 Digit) : "))
            if len(str(kode_bayar))==5:
                if kode_bayar == codeSended:
                    print("Kode Pembayaran Terkonfirmasi")
                    ps.kirim_email_struk(
                        name,
                        film_dipilih,
                        str(input_jam_pilihan),
                        str(tanggal_pilihan)+datetime.datetime.now().strftime('-%m-%Y'),
                        jambeli,
                        tanggalbeli,
                        list_kursi_pilihan,
                        totalbeli,
                        kode_pembayaran,
                        email_user)
                break
            else:
                print("Kode pembayaran salah!")      
        print('''\n===============================================================    
Pembayaran Berhasil. Terimakasih telah memesan di ADUDU CINEMAX!
===============================================================''')

        df = ps.read('Data Jadwal.csv')
        for i in list_kursi_pilihan:
            listdf = df.iloc[index_data[0],5:45]
            listdf.values[list_kursi.index(i)]=0
            df.iloc[index_data[0],5:45] = listdf    
        updateKursi = pd.DataFrame(df)
        updateKursi.to_csv('Data Jadwal.csv',index=False)
        
        summary = {
                            'kode' : [kode_pembayaran],
                            'user' : [name],
                            'waktupembelian' : [datetime.datetime.now().strftime('%d-%m-%Y')],
                            'judul' : [film_dipilih],
                            'jam' : [input_jam_pilihan],
                            'tanggal' : [tanggal_pilihan],
                            'bulan' : [str(datetime.datetime.now().month)],
                            'tahun' : [str(datetime.datetime.now().year)],
                            'kursi' : ["" + str(list_kursi_pilihan)+"" ],
                            'pembayaran' : ["CASHLESS"]}
        
        inputdatapembelian = pd.DataFrame(summary)
        inputdatapembelian.to_csv('riwayat pembelian.csv', mode='a', index=False, header=False)
        
    elif jenis_transaksi =='2':
        kode_pembayaran = kode_pembayaran_lama
        ps.konf(name,
                film_dipilih,
<<<<<<< HEAD
                str(input_jam_pilihan),
                str(tanggal_pilihan)+datetime.datetime.now().strftime('-%m-%Y'),
                jambeli,
                tanggalbeli,
=======
                jambeli,
                tanggalbeli,
                str(tanggal_pilihan)+datetime.datetime.now().strftime('-%m-%Y'),
>>>>>>> bd9312296a8bb79cd7d90788c64fe4cb2f8b5926
                list_kursi_pilihan,
                totalbeli + (0.1 * totalbeli),
                kode_pembayaran)
        
        while True:
            konfirmasi_bayar = input("Pesanan sudah benar? (y/n) : ")
            if konfirmasi_bayar == 'y':
                print("Reschedule terkonfirmasi")
                ps.kirim_email_struk(
                    name,
                    film_dipilih,
<<<<<<< HEAD
                    str(input_jam_pilihan),
                    str(tanggal_pilihan)+datetime.datetime.now().strftime('-%m-%Y'),
                    jambeli,
                    tanggalbeli,
                    list_kursi_pilihan,
                    totalbeli+(0.1 * totalbeli),
                    kode_pembayaran,
                    email_user)
=======
                    jambeli,
                    tanggalbeli,
                    str(tanggal_pilihan)+datetime.datetime.now().strftime('-%m-%Y'),
                    list_kursi_pilihan,
                    totalbeli + (0.1 * totalbeli),
                    kode_pembayaran,
                    email_user
                )
>>>>>>> bd9312296a8bb79cd7d90788c64fe4cb2f8b5926
                break
            elif konfirmasi_bayar == 'n':
                konfirmasi_bayar2 = input('Yakin ingin membatalkan reschedule? (y/n) : ')
                if konfirmasi_bayar2 == 'y':
                    menu()
            else:
                print('Input tidak valid')
        print('''\n===============================================================
Reschedule Berhasil. Terimakasih telah memesan di ADUDU CINEMAX!
===============================================================''')

        df = ps.read('Data Jadwal.csv')
        for i in list_kursi_pilihan:
            listdf = df.iloc[index_data[0],5:45]
            listdf.values[list_kursi.index(i)]=0
            df.iloc[index_data[0],5:45] = listdf   
        
        updateKursi = pd.DataFrame(df)
        updateKursi.to_csv('Data Jadwal.csv',index=False)
        summary = {
                            'kode' : [kode_pembayaran],
                            'user' : [name],
                            'waktupembelian' : [datetime.datetime.now().strftime('%d-%m-%Y')],
                            'judul' : [film_dipilih],
                            'jam' : [input_jam_pilihan],
                            'tanggal' : [tanggal_pilihan],
                            'bulan' : [str(datetime.datetime.now().month)],
                            'tahun' : [str(datetime.datetime.now().year)],
                            'kursi' : ["" + str(list_kursi_pilihan)+"" ],
                            'pembayaran' : ["CASHLESS"]}
        
        dfPembelian = ps.read('riwayat pembelian.csv')
        dfPembelian.iloc[index_pembelian] = pd.Series(summary)
        dfPembelian.to_csv('riwayat pembelian.csv', index=False )

    elif jenis_transaksi =='3':
        while True:
            konfirmasi_bayar = input("\nYakin melakukan refund? (y/n) : ")
            if konfirmasi_bayar == 'y':
                print("Refund Terkonfirmasi")
                ps.ngirim_email(name,email_user,jenis=3)
                break
            elif konfirmasi_bayar == 'n':
                menu()
                break
            else:
                print('Input tidak valid')
        dataPembelian = pd.read_csv('riwayat pembelian.csv')
        dataPembelian = dataPembelian.drop(index_pembelian)
        dataPembelian.to_csv('riwayat pembelian.csv', index=False)
        print('''\n===========================================================
Refund Berhasil. Terimakasih telah memesan di ADUDU CINEMAX!
===========================================================''')
    
    menu()
begin()