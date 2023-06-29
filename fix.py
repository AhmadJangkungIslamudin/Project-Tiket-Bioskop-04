import csv
import pandas as pd
import datetime 
import random
import ast
import shortcut_pandas as ps

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
        print("                 Login berhasil")
        print("=" * 50)
        menu()
        
    else:
        print("=" * 50)
        print(" Username atau Password yang anda masukkan salah")
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
    print("\nKetik '1' Pemesanan tiket")
    print("Ketik '2' Pusat Bantuan")
    print("Ketik '3' Keluar")
    option = input("Pilih menu : ")
    if option == '1':
        with open('Daftar Film.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
        column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]
        for row in data:
            formatted_row = ' | '.join(f"{item:{width}}" for item, width in zip(row, column_widths))
            print(formatted_row)
        pilihfilm('1')
    elif option == '2':
        pusat_bantuan()
    elif option == '3':
        print('''
        
        Terimakasih telah menggunakan layanan kami!
        
        ''')

    else:
        print('\nTidak terdapat dalam menu!\n')
        menu()

def pusat_bantuan():
    global kode_pembayaran, kode_pembayaran_lama
    kode_pembayaran = (input("Masukan kode unik anda "))
    kode_pembayaran_lama = kode_pembayaran
    sukses = False
    with open('riwayat pembelian.csv', 'r') as file:
        next(file)  # Melewati baris header jika ada
        reader = csv.reader(file)
        for row in reader:
            if row[0] == kode_pembayaran_lama:
                sukses = True
                break
    if sukses == True:
        print("Ketik '1' Reschedule")
        print("Ketik '2' Cancel & Refund")
        option = (input("Pilih menu : "))
        if option == "1":
                print("Anda memilih RESCHEDULE")
                pilihfilm('2')
        elif option == "2":
                print("Anda memilih CANCEL & REFUND")
                pilihfilm('3')
        else:
                print("Menu tidak tersedia")
                pusat_bantuan()
    else:
        print('Kode unik tidak terdaftar')
        pusat_bantuan()        

def pilihfilm(opsimenu):
    global film_dipilih, list_kursi_pilihan, df,list_kursi,index_pembelian,dfPembelian,list_kursi_pilihan
    list_kursi = ["A1","A2","A3","A4","A5","A6","A7","A8","B1","B2","B3","B4","B5","B6","B7","B8","C1","C2","C3","C4","C5","C6","C7","C8","D1","D2","D3","D4","D5","D6","D7","D8","E1","E2","E3","E4","E5","E6","E7","E8"]
    list_kursi_pilihan =[]

    def reset_kursi():
        global df, film_dipilih,dfPembelian,index_pembelian, list_kursi_pilihan
        dfPembelian = ps.read('riwayat pembelian.csv')
        index_pembelian=dfPembelian.index[(dfPembelian['kode'] == kode_pembayaran)].tolist()                    
        index_pembelian=dfPembelian.index[(dfPembelian['kode'] == kode_pembayaran)&(dfPembelian['user'] == name)].tolist()
        ps.konf(name,
                dfPembelian.iloc[index_pembelian[0],3],
                "-",
                dfPembelian.iloc[index_pembelian[0],2],
                str(dfPembelian.iloc[index_pembelian[0],5])+"-"+str(datetime.datetime.now().month)+"-"+"2023",
                dfPembelian.iloc[index_pembelian[0],8],
                "-",
                kode_pembayaran
                )

        df = ps.read('Data Jadwal.csv')
        index_data=df.index[(df['jam'] == dfPembelian.iloc[index_pembelian[0],4]) & 
                            (df['tanggal'] == dfPembelian.iloc[index_pembelian[0],5])& 
                            (df['judul'] == dfPembelian.iloc[index_pembelian[0],3])].tolist()

        list_kursi_pilihan = ast.literal_eval(dfPembelian.values[index_pembelian[0],8])
        film_dipilih = dfPembelian.iloc[index_pembelian[0],3]
        

    def print_layout(checklist):
        global index_data
        index_data=df.index[(df['jam'] == input_jam_pilihan) & (df['tanggal'] == tanggal_pilihan)& (df['judul'] == film_dipilih)].tolist()
        print(index_data)
        nama_kolom = ["A","B","C","D","E"]
        nama_baris = [1,2,3,4,5,6,7,8]
        print('=========  LAYAR  =========')
        x=0
        if opsimenu == '1':
            for i in nama_kolom:
                for j in nama_baris:
                    if df.iloc[index_data[0],5:45].values[x] == 1:
                        print(i,end="")
                        print(j,end="  ")
                    elif df.iloc[index_data[0],5:45].values[x] == 0:
                        print("|x|",end=' ')
                    x=x+1
                print()

    def pilih_tanggal():
        global tanggal_pilihan, df, dataKursi
        #=== BACA DATA TANGGAL
        df = ps.read('Data Jadwal.csv')
        #=== PILIH TANGGAL
        tanggal_tersedia=list(set(df.loc[(df['judul'] == film_dipilih)].tanggal))
        print(tanggal_tersedia)                                                                                 # PRINT TANGGAL TERSEDIA
        tanggal_pilihan = int(input("Masukan Tanggal pilihan "))
        if tanggal_pilihan in tanggal_tersedia and tanggal_pilihan>=datetime.datetime.now().day:
            if tanggal_pilihan==datetime.datetime.now().day and datetime.datetime.now().time() >= datetime.time(16, 0):
                print('Tidak ada jam tayang')
                pilih_tanggal()
            else:
                print("SUCCESS")
                pilih_jam()
        #misal selain integer eror        
        else:
            print("Tanggal tidak sesuai")
            pilih_tanggal()

    def pilih_jam():
        global input_jam_pilihan
        #=== BACA DATA TANGGAL
        df = ps.read('Data Jadwal.csv')
        #=== PILIH JAM
        jam_tersedia=list(set(df.loc[(df['judul'] == film_dipilih)&(df['tanggal'] == tanggal_pilihan)].jam))
        print(jam_tersedia)                                                                                     # PRINT JAM TERSEDIA
        try:
            input_jam_pilihan = input("Masukan jam pilihan anda ")
            jam_pilihan = datetime.datetime.strptime(input_jam_pilihan, "%H:%M").time()
        except:
            print("Input tidak sesuai")
            pilih_jam()

        if input_jam_pilihan in jam_tersedia and (jam_pilihan>=datetime.datetime.now().time() or tanggal_pilihan>datetime.datetime.now().day):
            print("SUCCESS")
            print_layout('')
            pilih_kursi()
        elif input_jam_pilihan in jam_tersedia and (jam_pilihan<=datetime.datetime.now().time()):
            print("Jam sudah terlewat")
            pilih_tanggal()
        else:
            print("Jam tidak tersedia")
            pilih_jam()
    
    #=== PILIH KURSI
    
    def pilih_kursi():
        if opsimenu == '1':
            df = ps.read('Data Jadwal.csv')
            while True:
                try: 
                    kursi_pilihan = input("\nPilih kursi anda. Ketik Confirm jika sudah selesai ")
                    kursi_pilihan == kursi_pilihan.lower()
                    if kursi_pilihan == "Confirm" and len(list_kursi_pilihan)==0:
                        print("Pilih minimal satu kursi")
                    elif kursi_pilihan == "Confirm":
                        print(list_kursi_pilihan)
                        ringkasan_beli()
                        break
                    elif kursi_pilihan in list_kursi_pilihan or df.iloc[index_data[0],5:45].values[list_kursi.index(kursi_pilihan)]==0:
                        print("Kursi tidak tersedia / sudah dipilih")
                    elif kursi_pilihan in list_kursi and df.iloc[index_data[0],5:45].values[list_kursi.index(kursi_pilihan)]==1:
                        list_kursi_pilihan.append(kursi_pilihan)
                        print(list_kursi_pilihan)
                except:
                    print("Input salah")
        elif opsimenu == '2':
            ringkasan_beli()
    
#==== Ringkasan beli
    def ringkasan_beli():
        print('''
        ===================================
                  Ringkasan Order
        ===================================

        Judul   : {judul}
        Jam     : {jam}
        Tanggal : {tanggal}
        Bulan   : {bulan}
        Tahun   : {tahun}
        Kursi   : {kursi}

        ===================================
        '''.format(judul=film_dipilih,
                jam=input_jam_pilihan,
                tanggal=tanggal_pilihan,
                bulan=datetime.datetime.now().month,
                tahun=datetime.datetime.now().year,
                kursi=list_kursi_pilihan))
        
        konfirmasi_bayar = input("Apakah anda ingin melanjutkan pembayaran? (y/n) : ")
        if konfirmasi_bayar == 'y':
            transaksi(opsimenu)
            return
        elif konfirmasi_bayar != 'y':
            menu()
    #=======================================================
    #=== BACA DAFTAR FILM
    if opsimenu == "1":
        df = ps.read('Daftar Film.csv')
        #=== INPUT FILM
        inputan=int(input("Masukkan no Film "))-1
        try:
            film_dipilih = df.iloc[inputan,1]
            print(film_dipilih)
            pilih_tanggal()
        except:
            print("Kesalahan sistem, mohon coba lagi")
            menu()
    elif opsimenu == '2':
        reset_kursi()
        pilih_tanggal()
    elif opsimenu == '3':
        reset_kursi()
        transaksi(opsimenu)
        return

def transaksi(jenis_transaksi):
    if jenis_transaksi =='1':
        kode_pembayaran = "TK"+str(random.randint(10000000, 99999999))
        ps.konf(name,
                film_dipilih,
                datetime.datetime.now().strftime('%H:%M'), #jambeli
                datetime.datetime.now().strftime('%d-%m-%Y'), #tanggalbeli
                str(tanggal_pilihan)+datetime.datetime.now().strftime('-%m-%Y'),
                list_kursi_pilihan,
                (int(len(list_kursi_pilihan))*25000),
                kode_pembayaran)
        
        while True:
            konfirmasi_bayar = input("Bayar? (y/n) : ")
            if konfirmasi_bayar == 'y':
                break
            elif konfirmasi_bayar == 'n':
                konfirmasi_bayar2 = input('Yakin ingin membatalkan pesanan? (y/n) : ')
                if konfirmasi_bayar2 == 'y':
                    menu()
            else:
                print('Input tidak valid')
        
        while True:
            kode_bayar = str(input("Masukan Kode Konfirmasi Pembayaran (5 Digit) : "))
            if len(str(kode_bayar))==5:
                print("Kode Pembayaran Terkonfirmasi")
                break
            else:
                print("Kode pembayaran salah!")
        print('''
        
        Pembayaran Berhasil. Terimakasih telah memesan melalui aplikasi kami!
        
        ''')

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
                datetime.datetime.now().strftime('%H:%M'),
                datetime.datetime.now().strftime('%d-%m-%Y'),
                str(tanggal_pilihan)+"-"+str(datetime.datetime.now().month)+"-"+"2023",
                list_kursi_pilihan,
                (int(len(list_kursi_pilihan))*25000),
                kode_pembayaran)
        
        while True:
            konfirmasi_bayar = input("Pesanan sudah benar? (y/n) : ")
            if konfirmasi_bayar == 'y':
                break
            elif konfirmasi_bayar == 'n':
                konfirmasi_bayar2 = input('Yakin ingin membatalkan pesanan? (y/n) : ')
                if konfirmasi_bayar2 == 'y':
                    menu()
            else:
                print('Input tidak valid')
        print('''
        
        Reschedule Berhasil. Terimakasih telah memesan melalui aplikasi kami!
        
        ''')

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
        print(kode_pembayaran)
        dfPembelian = ps.read('riwayat pembelian.csv')
        dfPembelian.iloc[index_pembelian] = pd.Series(summary)
        dfPembelian.to_csv('riwayat pembelian.csv', index=False )

    elif jenis_transaksi =='3':
        while True:
            konfirmasi_bayar = input("Yakin melakukan cancel & refund? (y/n) ")
            if konfirmasi_bayar == 'y':
                break
            elif konfirmasi_bayar == 'n':
                menu()
            else:
                print('Input tidak valid')
        dataPembelian = pd.read_csv('riwayat pembelian.csv')
        dataPembelian = dataPembelian.drop(index_pembelian)
        dataPembelian.to_csv('riwayat pembelian.csv', index=False)
        print('''
        
        Cancel & Refund Berhasil. Terimakasih telah menggunakan aplikasi kami!
        
        ''')
    
    print("=" * 50)
    print("         Adudu Cinemax         ")
    print("=" * 50)
    menu()

begin()