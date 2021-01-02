def garis():
    print("-----------------------------------------")
def gariss():
    print("=========================================")

class makanan:

    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def tampilkan(self):
        print("Nama Makanan : ", self.nama)
        print("Harga        : ", self.harga)

a1 = makanan ("Nasi Rawon", "9000")
a2 = makanan ("Nasi Soto", "7000")
a3 = makanan ("Nasi Goreng", "8000")
a4 = makanan ("Bakso", "6000")
a5 = makanan ("Mie Ayam", "8000")

        


         

print("RUMAH MAKAN QR".center(70))
print("JL. Paulo Dybala ITALiA".center(75))
gariss()
print("1. Tampilkan Menu     : ")
print("2. Lakukan Pembayaran : ")
pilih = input("Masukan Angka : ")
if pilih == "1":
    print("Ini Daftar Menu Kami")
    (gariss())
    (a1.tampilkan())
    (garis())
    (a2.tampilkan())
    (garis())
    (a3.tampilkan())
    (garis())
    (a4.tampilkan())
    (garis())
    (a5.tampilkan())
    
    
elif pilih == "2":
    garis()
    listnb=[]
    listhb=[]
    listst=[]
    listjb=[]
    totalitem=0
    totalkeseluruhan=0
    #input
    kasir=input("Nama Kasir            : ")
    tanggal=input("Masukkan Tanggal      : ")
    j=int(input("Banyaknya Pembelian   : "))
    garis()
    for i in range (j):
        nb=input("Makanan  : ")
        listnb.append(nb)
        hb=int(input("Harga Barang   : "))
        listhb.append(hb)
        jb=int(input("Jumlah Barang  : "))
        listjb.append(jb)
        st=listhb[i]*listjb[i]
        listst.append(st)

    #hasil
    print("")
    print("Pembelian")
    print("Kasir   :", kasir)
    print("Tanggal :",tanggal)
    garis()
    print("Hg.Jual          Qty          Subtotal")
    garis()
    for i in range (j):
        print("",(listnb[i]))
        print("Rp.%d          %d         Rp.%d"%(listhb[i],listjb[i],listst[i]))
        totalitem=totalitem+listjb[i]
        totalkeseluruhan=totalkeseluruhan+listst[i]
    print("Total Item          =%d"%totalitem)
    print("Total Keseluruhan   =Rp.%d"%totalkeseluruhan)
    bayar=int(input("Pembayaran Tunai.....:Rp."))
    kembali = bayar - totalkeseluruhan
    print("Kembali :Rp.", kembali)
    print("Terima Kasih Telah Datang Di Rumah Makan Kami".center(70))
    garis()

    

    
    


