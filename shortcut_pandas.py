import pandas as pd
#1
def read(nama_file):
    data = pd.read_csv(nama_file)
    df = pd.DataFrame(data)
    return df
#2
def konf(a,b,c,d,e,f,g,h):
    print(
    '''
    ==================================================
    Konfirmasi Pembayaran
    ==================================================

    Nama                    : {nama}
    Judul                   : {judul}
    Jam Pembelian           : {jam}
    Tanggal Pembelian       : {tanggal}
    Tanggal Penayangan      : {tanggaltayang}
    Kursi                   : {kursi}
    Total                   : {total}
    Kode Unik               : {kode}

    ==================================================
    '''.format(nama=a,
            judul=b,
            jam=c,
            tanggal=d,
            tanggaltayang=e,
            kursi=f,
            total=g,
            kode=h
        ))
    
