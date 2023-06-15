import csv
import pandas as pd
import datetime 
import random
import ast
import shortcut_pandas as ps

def begin():
    print("=" * 50)
    print("Selamat Datang di Adudu Cinemax")
    print("=" * 50)
    print("Ketik '1' jika anda sudah ingin Login")
    print("Ketik '2' untuk mendaftar")
    print("=" * 50)
    option = (input("Silahkan masukkan\t:"))
    option = option.lower()
    if option == '1':
        login()
    elif option == '2':
        signup()
    else:
        print('Silahkan Masukkan salah satunya!')
        begin()

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
    global opsi_transaksi
    print("Ketik '1' Pemesanan tiket")
    print("Ketik '2' Pusat Bantuan")
    print("Ketik '3' Keluar")
    option = input("Pilih menu : ")
    if option == '1':
        opsi_transaksi = 1
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
        print()
    else:
        print('\nTidak terdapat dalam menu!\n')
        menu()

def pusat_bantuan():
    global kode_pembayaran, kode_pembayaran_lama
    global opsi_transaksi
    kode_pembayaran = (input("Masukan kode unik anda "))
    kode_pembayaran_lama = kode_pembayaran
    print("Ketik '1' Reschedule")
    print("Ketik '2' Cancel & Refund")
    option = (input("Pilih menu : "))
    if option == "1":
        print("Anda memilih RESCHEDULE")
        pilihfilm('2')
    elif option == "2":
        print("Anda memilih CANCEL & REFUND")
        pilihfilm('3')

def pilihfilm(opsimenu):
    global film_dipilih, list_kursi_pilihan, df,list_kursi
    list_kursi = ["A1","A2","A3","A4","A5","A6","A7","A8","B1","B2","B3","B4","B5","B6","B7","B8","C1","C2","C3","C4","C5","C6","C7","C8","D1","D2","D3","D4","D5","D6","D7","D8","E1","E2","E3","E4","E5","E6","E7","E8"]
    list_kursi_pilihan =[]

    def print_layout(checklist):
        global index_data
        
        index_data=df.index[(df['jam'] == input_jam_pilihan) & (df['tanggal'] == tanggal_pilihan)& (df['judul'] == film_dipilih)].tolist()
        print(index_data)
        nama_kolom = ["A","B","C","D","E"]
        nama_baris = [1,2,3,4,5,6,7,8]
        print('''
        ========LAYAR========
                ''')
    
        x=0
    
        for i in nama_kolom:
            for j in nama_baris:
                if df.iloc[index_data[0],5:45].values[x] == 1:
                    print(i,end="")
                    print(j,end="  ")
                elif df.iloc[index_data[0],5:45].values[x] == 0:
                    print("|x|",end=' ')
                elif checklist == 'v':
                    print("|v|",end=' ')
                x=x+1
            print()

    def pilih_tanggal():
        global tanggal_pilihan, df, dataKursi
        #=== BACA DATA TANGGAL
        dataKursi = pd.read_csv('Data Jadwal.csv')
        df = pd.DataFrame(dataKursi)
        #=== PILIH TANGGAL
        tanggal_tersedia=list(set(df.loc[(df['judul'] == film_dipilih)].tanggal))
        print(tanggal_tersedia)                                                                                 # PRINT TANGGAL TERSEDIA
        tanggal_pilihan = int(input("Masukan Tanggal pilihan "))
        if tanggal_pilihan in tanggal_tersedia and tanggal_pilihan>=datetime.datetime.now().day:
            print("success")
            pilih_jam()
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
            pilih_jam()
        if input_jam_pilihan in jam_tersedia and (jam_pilihan>=datetime.datetime.now().time() or tanggal_pilihan>=datetime.datetime.now().day):
                print("success")
                print_layout('')
                pilih_kursi()
        else:
            print("Jam tidak sesuai atau sudah terlewat")
            pilih_jam()
    
    #=== PILIH KURSI
    
    def pilih_kursi():
        df = ps.read('Data Jadwal.csv')
        while True:
            try: 
                kursi_pilihan = input("Pilih kursi anda. Ketik Confirm jika sudah selesai ")
                if kursi_pilihan == "Confirm".lower() and len(list_kursi_pilihan)==0:
                    print("Pilih minimal satu kursi")
                elif kursi_pilihan == "Confirm".lower():
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
    
#==== Ringkasan beli
    def ringkasan_beli():
        print('''
        ===========
        Ringkasan Order
        ===========

        Judul   : {judul}
        Jam     : {jam}
        Tanggal : {tanggal}
        Bulan   : {bulan}
        Tahun   : 2023
        Kursi   : {kursi}


        '''.format(judul=film_dipilih,
                jam=input_jam_pilihan,
                tanggal=tanggal_pilihan,
                bulan=datetime.datetime.now().month,
                kursi=list_kursi_pilihan))
        
        konfirmasi_bayar = input("Apakah anda ingin melanjutkan pembayaran? (y/n) ")
        if konfirmasi_bayar == 'y':
            transaksi(opsimenu)
            return
        else:
            pilih_kursi()

    
    dataFilm = pd.read_csv('Daftar Film.csv')
    df = pd.DataFrame(dataFilm)
    #inputfillm
    inputan=int(input("Masukkan no Film "))-1
    try:
        film_dipilih = df.iloc[inputan,1]
        print(film_dipilih)
        pilih_tanggal()
    except:
        print("error")
        menu()

def transaksi(jenis_transaksi):

    if jenis_transaksi =='1':
        
        kode_pembayaran = "TK"+str(random.randint(10000000, 99999999))
        
        ps.konf(name,
                film_dipilih,
                datetime.datetime.now().strftime('%H:%M'),
                datetime.datetime.now().strftime('%d-%m-%Y'),
                str(tanggal_pilihan)+"-"+str(datetime.datetime.now().month)+"-"+"2023",
                list_kursi_pilihan,
                (int(len(list_kursi_pilihan))*25000),
                kode_pembayaran)
        
        konfirmasi_bayar = input("Bayar? (y/n) ")
        if konfirmasi_bayar == 'y':
            print("Lanjutt")
        elif konfirmasi_bayar != 'y':
            pilihfilm()
       
        while True:
            kode_bayar = str(input("Masukan Kode Konfirmasi Pembayaran kamu (5 Digit) "))
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
                            'tahun' : [2023],
                            'kursi' : ["" + str(list_kursi_pilihan)+"" ],
                            'pembayaran' : ["CASHLESS"]}

        inputdatapembelian = pd.DataFrame(summary)
        
        inputdatapembelian.to_csv('riwayat pembelian.csv', mode='a', index=False, header=False)
    menu()

begin()