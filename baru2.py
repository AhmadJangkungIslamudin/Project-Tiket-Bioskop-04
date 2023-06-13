import csv
import pandas as pd
import datetime 
import random
import ast

def begin():
    print("=" * 50)
    print("\tSelamat Datang di Adudu Cinemax")
    print("=" * 50)
    print("\nKetik '1' jika anda sudah ingin Login")
    print("Ketik '2' untuk mendaftar\n")
    print("=" * 50)
    option = str(input("Silahkan masukkan : "))
    option = option.lower()
    if option == '1':
        login()
    elif option == '2':
        signup()
    else:
        print('Silahkan Masukkan salah satunya!\n')
        begin()

def login():
    global name
    name = input("\nMasukkan Username : ")
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
        print("\t\tLogin berhasil")
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
    global opsi_transaksi
    print("Ketik '1' Pemesanan tiket")
    print("Ketik '2' Pusat Bantuan")
    option = input("\nPilih menu : ")
    print()
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
    else:
        print('\nTidak terdapat dalam menu!\n')
        menu()

def pusat_bantuan():
    global kode_pembayaran
    global opsi_transaksi
    kode_pembayaran = input("Masukan kode unik anda : ")
    print("Ketik '1' Reschedule")
    print("Ketik '2' Refund")
    option = input("Pilih menu : ")
    if option == '1':
        pilihfilm('2')
    elif option == '2':
        print("refund ya")
        pilihfilm('3')



def pilihfilm(opsimenu):
    global film_dipilih, list_kursi_pilihan, df,list_kursi
    list_kursi = ["A1","A2","A3","A4","A5","A6","A7","A8","B1","B2","B3","B4","B5","B6","B7","B8","C1","C2","C3","C4","C5","C6","C7","C8","D1","D2","D3","D4","D5","D6","D7","D8","E1","E2","E3","E4","E5","E6","E7","E8"]
    def reset_kursi():
        global df
        dataPembelian = pd.read_csv('riwayat pembelian.csv')
        dfPembelian = pd.DataFrame(dataPembelian)
        index_pembelian=dfPembelian.index[(dfPembelian['kode'] == kode_pembayaran)].tolist()
                                          

        dataPembelian = pd.read_csv('riwayat pembelian.csv')
        dfPembelian = pd.DataFrame(dataPembelian)
        index_pembelian=dfPembelian.index[(dfPembelian['kode'] == 1)].tolist()

        dataKursi = pd.read_csv('test data jadwal.csv')
        df = pd.DataFrame(dataKursi)
        index_data=df.index[(df['jam'] == dfPembelian.iloc[index_pembelian[0],4]) & 
                            (df['tanggal'] == dfPembelian.iloc[index_pembelian[0],5])& 
                            (df['judul'] == dfPembelian.iloc[index_pembelian[0],3])].tolist()

        string_kursi_pilihan = pd.read_csv('riwayat pembelian.csv')['kursi'][0]
        print(string_kursi_pilihan)
        list_kursi_pilihan = ast.literal_eval(string_kursi_pilihan)

        for i in list_kursi_pilihan:
            listdf = df.iloc[index_data[0],5:45]
            listdf.values[list_kursi.index(i)]=1
            df.iloc[index_data[0],5:45] = listdf 

    if opsimenu == '2':
        reset_kursi()
    elif opsimenu == '3':
        reset_kursi()
        transaksi(opsimenu)




    
    def print_layout(checklist):
    #=== PRINT LAYOUT
        dataKursi = pd.read_csv('test data jadwal.csv')
        df = pd.DataFrame(dataKursi)
        global index_data
        
        index_data=df.index[(df['jam'] == input_jam_pilihan) & (df['tanggal'] == tanggal_pilihan)& (df['judul'] == film_dipilih)].tolist()
        print(index_data)
        nama_kolom = ["A","B","C","D","E"]
        nama_baris = [1,2,3,4,5,6,7,8]
        print('\n=============   LAYAR   =============\n')
    
        x=0
    
        for i in nama_kolom:
            for j in nama_baris:
                if df.iloc[index_data[0],5:45].values[x] == 1:
                    print(i,end="")
                    print(j,end="   ")
                elif df.iloc[index_data[0],5:45].values[x] == 0:
                    print("|x|",end=' ')
                elif checklist == 'v':
                    print("|v|",end=' ')
                x=x+1
            print()    #spasi stiap baris kursi
        print() #spasi

    def pilih_tanggal():
        global tanggal_pilihan, df, dataKursi
        #=== BACA DATA TANGGAL
        dataKursi = pd.read_csv('test data jadwal.csv')
        df = pd.DataFrame(dataKursi)
        #=== PILIH TANGGAL
        tanggal_tersedia=list(set(df.loc[(df['judul'] == film_dipilih)].tanggal))
        print(tanggal_tersedia)                                                                                 # PRINT TANGGAL TERSEDIA
        tanggal_pilihan = int(input("\nMasukan Tanggal pilihan : "))
        if tanggal_pilihan in tanggal_tersedia and tanggal_pilihan>=datetime.datetime.now().day:
            print("success\n")
            pilih_jam()
        else:
            print("\nTanggal tidak tersedia!\n")
            pilih_tanggal()

    def pilih_jam():
        global input_jam_pilihan
        #=== BACA DATA TANGGAL
        dataKursi = pd.read_csv('test data jadwal.csv')
        df = pd.DataFrame(dataKursi)
        #=== PILIH JAM
        jam_tersedia=list(set(df.loc[(df['judul'] == film_dipilih)&(df['tanggal'] == tanggal_pilihan)].jam))
        print(jam_tersedia)                                                                                     # PRINT JAM TERSEDIA
        try:
            input_jam_pilihan = input("\nMasukan jam pilihan anda : ")
            jam_pilihan = datetime.datetime.strptime(input_jam_pilihan, "%H:%M").time()
        except:
            print()
            pilih_jam()
        if input_jam_pilihan in jam_tersedia and (jam_pilihan>=datetime.datetime.now().time() or tanggal_pilihan>=datetime.datetime.now().day):
            print("success")
            print_layout('')
            pilih_kursi()
        else:
            print("\nJam tidak sesuai\n")
            pilih_jam()
    

    #=== PILIH KURSI

    list_kursi_pilihan =[]
    def pilih_kursi():
        dataKursi = pd.read_csv('test data jadwal.csv')
        df = pd.DataFrame(dataKursi)
        while True:
            kursi_pilihan = input("Pilih kursi anda. Ketik Confirm jika sudah selesai : ")
            if kursi_pilihan == "confirm" or  kursi_pilihan == "Confirm":
                print(list_kursi_pilihan)
                ringkasan_beli()
                break
            elif kursi_pilihan in list_kursi_pilihan or df.iloc[index_data[0],5:45].values[list_kursi.index(kursi_pilihan)]==0:
                print("Kursi tidak tersedia / sudah dipilih\n")
            elif kursi_pilihan in list_kursi and df.iloc[index_data[0],5:45].values[list_kursi.index(kursi_pilihan)]==1:
                list_kursi_pilihan.append(kursi_pilihan)
                print(list_kursi_pilihan)
                #print_layout('v')
            else:
                print("Input salah")
    
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
        
        konfirmasi_bayar = input("Apakah anda ingin melanjutkan pembayaran? (y/n) : ")
        print()
        if konfirmasi_bayar == 'y':
            transaksi(opsimenu)
        else:
            pilih_kursi()

    #=== BACA DAFTAR FILM
    dataFilm = pd.read_csv('Daftar Film.csv')
    df = pd.DataFrame(dataFilm)

    #=== INPUT FILM
    inputan=int(input("\nMasukkan no Film : "))-1

    #try:
    film_dipilih = df.iloc[inputan,1]
    print(film_dipilih)
    print()
    pilih_tanggal()
    #except:
        #print("error ngab")

def transaksi(jenis_transaksi):
    def print_konfirmasibayar():
        print('''
        ==================================================
                      Konfirmasi Pembayaran
        ==================================================

        Nama                  : {nama}
        Judul                 : {judul}
        Jam tayang            : {jam}
        Jam Pembelian         : {jambeli}
        Tanggal Penayangan    : {tanggaltayang}
        Tanggal Pembelian     : {tanggal}
        Kursi                 : {kursi}
        Total                 : {total}
        Kode Unik             : {kode}

        ==================================================
        '''.format(nama=name,
                judul=film_dipilih,
                jam=input_jam_pilihan,
                jambeli=datetime.datetime.now().strftime('%H:%M'),
                tanggal=datetime.datetime.now().strftime('%d-%m-%Y'),
                tanggaltayang=str(tanggal_pilihan)+"-"+str(datetime.datetime.now().strftime('%m-%Y')),
                kursi=list_kursi_pilihan,
                total=(int(len(list_kursi_pilihan))*25000),
                kode=kode_pembayaran
                ))
    

    if jenis_transaksi =='1':
        kode_pembayaran = "TK"+str(random.randint(10000000, 99999999))
        print_konfirmasibayar()
        konfirmasi_bayar = input("Bayar? (y/n) : ")

        print('''
        =====================================================================
        Pembayaran Berhasil. Terimakasih telah memesan melalui aplikasi kami!
        =====================================================================
        ''')

        dataKursi = pd.read_csv('test data jadwal.csv')
        df = pd.DataFrame(dataKursi)

        for i in list_kursi_pilihan:
            listdf = df.iloc[index_data[0],5:45]
            listdf.values[list_kursi.index(i)]=0
            df.iloc[index_data[0],5:45] = listdf   
        
        updateKursi = pd.DataFrame(df)
        updateKursi.to_csv('test data jadwal.csv',index=False)

    elif jenis_transaksi =='2':
        print_konfirmasibayar()
        konfirmasi_bayar = input("Pesanan sudah benar? (y/n) : ")

        print('''
        =====================================================================
        Reschedule Berhasil. Terimakasih telah memesan melalui aplikasi kami!
        =====================================================================
        ''')

        dataKursi = pd.read_csv('test data jadwal.csv')
        df = pd.DataFrame(dataKursi)

        for i in list_kursi_pilihan:
            listdf = df.iloc[index_data[0],5:45]
            listdf.values[list_kursi.index(i)]=0
            df.iloc[index_data[0],5:45] = listdf   
        
        updateKursi = pd.DataFrame(df)
        updateKursi.to_csv('test data jadwal.csv',index=False)

    elif jenis_transaksi =='3':
        konfirmasi_bayar = input("Yakin melakukan refund? (y/n) : ")

        print('''
        =============================================================
        Refund Berhasil. Terimakasih telah menggunakan aplikasi kami!
        =============================================================
        ''')


begin()