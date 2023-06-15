while True:
    konfirmasi_bayar = input("Bayar? (y/n) : ")
    if konfirmasi_bayar == 'y':
        print("Lanjutt")
        break
    elif konfirmasi_bayar == 'n':
        konfirmasi_bayar2 = input('Yakin ingin membatalkan pesanan? (y/n) : ')
        if konfirmasi_bayar2 == 'y':
            print('p')
        
    else:
        print('Input tidak valid. Harap masukkan "y" atau "n".')
