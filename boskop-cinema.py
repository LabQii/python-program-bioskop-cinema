kode = ['1', '2', '3', '4', '5']
menu = ['Dilan','Laskar Pelangi','Yowe Ben','Lemon Tea','Coffe']
harga = [35000,40000,45000,7000,6000]
daerah = ['Mojokerto','Lamongan','Bojonegoro','Tuban','Kediri','Solo']
bio_dpsn = []
mnn_dpsn = []
jbio_dpsn = []
jmnn_dpsn = []
H_bio = []
H_mnn = []
JH_bio = []
JH_mnn = []
asal = []

pilih = str(input("Masukkan asal daerah anda : "))
nama = str(input("Nama              : "))
asal.append(pilih)
chose = str(asal[0])
select = str(chose[3:4])
select_drmn =str(chose[3:6])
ulang = "y"
while ulang == "y" or ulang == "Y":

        print("")
        print("=============WELCOME TO BIOSKOP CINEMA=============")
        print("|DISKON 25% UNTUK MASYARAKAT DAERAH JAWA TIMUR     |")
        print("|DISKON 10% UNTUK MASYARAKAT DAERAH JAWA TENGAH    |")
        print("===================================================")
        print("Ketik (y/Y) untuk setuju, (t/T) untuk batal.. ")
        pesan_bio = input("Pesan Bioskop? ")
        if pesan_bio == "y" or pesan_bio == "Y":
            bio = "y"
            while bio == "y" or bio == "Y":
                print("==========================================")
                print(" DAFTAR BIOSKOP : ")
                print("==========================================")
                for x in range(len(menu) and len(harga)):
                    if x <= 2 :
                        print(x+1,"=>", menu[x], "dengan harga", harga[x])
                    elif x ==  3 :
                        print("==========================================")
                        print(" MENU MINUMAN: ")
                        print("==========================================")
                        print(x+1,"=>", menu[x], "dengan harga", harga[x])
                    else :
                        print(x+1,"=>", menu[x], "dengan harga",  harga[x])
                print("")
                pilihan_bio = input("Pilih kode Menu bioskop: ")
                qty = input("Berapa banyak yang akan di beli: ")
                jbio_dpsn.append(qty)
                i = 0
                while i < len(menu):
                    if kode[i] == pilihan_bio:
                        nm_bio = menu[i]
                        hrg_bio = harga[i]
                    i += 1

                totHarBio = hrg_bio * int(qty)
                totHar1 = totHarBio

                bio_dpsn.append(nm_bio)
                H_bio.append(hrg_bio)
                JH_mnn.append(totHar1)

                print("")
                print("==========================================")
                print(">>> NAMA Menu        : " + nm_bio)
                print(">>> HARGA            : " + str(hrg_bio))
                print(">>> JUMLAH           : " + qty)
                print(("-------------------------------"))
                print(">>> TOTAL Harga      : " + str(totHar1))
                bio = input("Pesan bioskop lagi? ")
                if bio == "t" or bio == "T":
                    pass

        elif pesan_bio == "t" or pesan_bio == "T":
            totHar1=0
            pass

        pesan_mnm = input("Pesan minum? ")
        if pesan_mnm == "y" or pesan_mnm == "Y":
            mnn = "y"
            while mnn == "y" or mnn == "Y":
                print("")
                print("==========================================")
                print(" DAFTAR BIOSKOP : ")
                print("==========================================")
                for n in range(len(menu) and len(harga)):
                    if n <= 2:
                        print(n+1,"=>", menu[n], "dengan harga", harga[n])
                    elif n == 3:
                        print("==========================================")
                        print(" MENU MINUMAN: ")
                        print("==========================================")
                        print(n+1,"=>", menu[n], "dengan harga", harga[n])
                    else:
                        print(n+1,"=>", menu[n], "dengan harga", harga[n])
                pilihan_mnm = input("Pilih kode Menu minuman: ")
                qty2 = input("Berapa banyak yang akan di beli: ")
                jmnn_dpsn.append(qty2)
                i = 0
                while i < len(menu):
                    if kode[i] == pilihan_mnm:
                        nm_mnn = menu[i]
                        hrg_mnn = harga[i]
                    i += 1

                totHarMnn = hrg_mnn * int(qty2)
                totHar2 = totHarMnn

                mnn_dpsn.append(nm_mnn)
                H_mnn.append(hrg_mnn)
                JH_mnn.append(totHar2)

                print("")
                print("==========================================")
                print(">>> NAMA Menu        : " + nm_mnn)
                print(">>> HARGA            : " + str(hrg_mnn))
                print(">>> JUMLAH           : " + qty2)
                print(("-------------------------------"))
                print(">>> TOTAL Harga      : " + str(totHar2))
                mnn = input("Pesan minuman lagi? ")
                if mnn == "t" or mnn == "T":
                    pass

        elif pesan_mnm == "t" or pesan_mnm == "T":
            totHar2 = 0
            pass

        Har1 = totHar1 and sum(H_bio)
        Har2 = totHar2 and sum(H_mnn)

        selesai = input("Cetak tagihan pembayaran? ")
        if selesai == "y" or selesai == "Y":
            totHar = Har1 + Har2
            print("")
            print("Rincian Transaksi:")
            print("==========================================")
            print(">>> NAMA Menu         ")
            print("Bioskop: ")
            print("---------------")
            for y in bio_dpsn:
                print(y + "    || Jumlah: " + str(qty) + " || Harga tiap menu ==> " + str(totHarBio))
            print("Minuman: ")
            print("---------------")
            for y in mnn_dpsn:
                print(y + "    || Jumlah: " + str(qty2) + " || Harga tiap menu ==> " + str(totHarMnn))
            print(("****************************************"))
            print(">>> TOTAL Harga      : Rp " + str(totHar))
            if select_drmn == "441":
                print("Asal : ", daerah[5])
                totHar = totHar * 75 / 100
                print("Anda mendapatkan diskon 25%")
                print("==========================================")
                print(">>> TOTAL Harga setelah diskon : Rp " + str(totHar))
                Bayar = input("=> Masukkan nominal pembayaran: Rp ")
                Kembalian = int(Bayar) - totHar

                print("")
                print("=> Kembalian: Rp " + str(Kembalian))
                print("==========================================")
            elif select_drmn == "411":
                print("Prodi : ", daerah[0])
                print("==========================================")
                totHar = totHar * 90 / 100
                print("Anda mendapatkan diskon 10%")
                print("==========================================")
                print(">>> TOTAL Harga setelah diskon : Rp " + str(totHar))
                Bayar = input("=> Masukkan nominal pembayaran: Rp ")
                Kembalian = int(Bayar) - totHar

                print("")
                print("=> Kembalian: Rp " + str(Kembalian))
                print("==========================================")
            elif select_drmn == "421":
                print("Prodi : ", daerah[1])
                print("==========================================")
                totHar = totHar * 90 / 100
                print("Anda mendapatkan diskon 10%")
                print("==========================================")
                print(">>> TOTAL Harga setelah diskon : Rp " + str(totHar))
                Bayar = input("=> Masukkan nominal pembayaran: Rp ")
                Kembalian = int(Bayar) - totHar

                print("")
                print("=> Kembalian: Rp " + str(Kembalian))
                print("==========================================")
            elif select_drmn == "431":
                print("Prodi : ", daerah[2])
                print("==========================================")
                totHar = totHar * 90 / 100
                print("Anda mendapatkan diskon 10%")
                print("==========================================")
                print(">>> TOTAL Harga setelah diskon : Rp " + str(totHar))
                Bayar = input("=> Masukkan nominal pembayaran: Rp ")
                Kembalian = int(Bayar) - totHar

                print("")
                print("=> Kembalian: Rp " + str(Kembalian))
                print("==========================================")
            elif select_drmn == "451":
                print("Prodi : ", daerah[3])
                print("==========================================")
                totHar = totHar * 90 / 100
                print("Anda mendapatkan diskon 10%")
                print("==========================================")
                print(">>> TOTAL Harga setelah diskon : Rp " + str(totHar))
                Bayar = input("=> Masukkan nominal pembayaran: Rp ")
                Kembalian = int(Bayar) - totHar

                print("")
                print("=> Kembalian: Rp " + str(Kembalian))
                print("==========================================")
            elif select_drmn == "461":
                print("Prodi : ", daerah[4])
                print("==========================================")
                totHar = totHar * 90 / 100
                print("Anda mendapatkan diskon 10%")
                print("==========================================")
                print(">>> TOTAL Harga setelah diskon : Rp " + str(totHar))
                Bayar = input("=> Masukkan nominal pembayaran: Rp ")
                Kembalian = int(Bayar) - totHar

                print("")
                print("=> Kembalian: Rp " + str(Kembalian))
                print("==========================================")
            else :
                print("Anda bukan dari Daerah yang mendapat diskon")
                print("Maka anda harus membayar harga normal")
                print("==========================================")
                print(">>> TOTAL Harga : Rp " + str(totHar))
                Bayar = input("=> Masukkan nominal pembayaran: Rp ")
                Kembalian = int(Bayar) - totHar

                print("")
                print("=> Kembalian: Rp " + str(Kembalian))
                print("==========================================")

        elif selesai == "t" or selesai == "T":
            pass
        print("Terimakasih Sudah Mampir di BIOSKOP CINEMA")
        print("Datang Lagi Lain Waktu....")
        break