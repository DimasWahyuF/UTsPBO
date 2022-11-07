#Buatlah program sederhana seperti dibawah ini dengan rumus ppn 10/100 dari total harga input

#NIM = input("Masukan NIM :")
#Nama = input("Masukan Nama:")

menu = "y" or "Y"
while menu == "y" or "Y":
    input("NIM  : 20210801259")
    input("Nama : Dimas Wahyu Firmansyah")
 
    print(" 1. Cappucino")
    print(" 2. Teh")
    print(" 3. Exit")
    listMenu=str(input(" Masukkan angka sesuai dengan menu yang tersedia = "))
    jumlahPesanan=int(input(" Jumlah dibeli = "))
    if listMenu == "1":
        namaMenu= " Cappucino"
        harga=(10000*jumlahPesanan)
        pajak= int(harga * 0.1)
        if jumlahPesanan >= 5:
            totalHarga=int(harga+pajak)
        else:
            totalHarga=int(harga+pajak)
    elif listMenu == "2":
        namaMenu= " Teh"
        harga = (5000*jumlahPesanan)
        pajak = int(harga * 0.1)
        if jumlahPesanan >= 5:
            totalHarga =int(harga+pajak)
        else:
            totalHarga =int(harga+pajak)
   
    print(" Menu :",namaMenu)
    print(" Jumlah Pesanan :", jumlahPesanan)
    print(" Harga :", harga)
    print(" Pajak :", pajak)
    print(" ------------------------------")
    print(" Total Pembayaran :", totalHarga)
    print(" ------------------------------")
