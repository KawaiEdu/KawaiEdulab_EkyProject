jadwal = []

while True:
    print("\njadwal kegiatan harian", jadwal)
    print("1. tambah kegiatan ")
    print("2. hapus kegiatan ")
    print("3. extend ")
    print("4. copy ")
    print("5. sort ")
    print("6. keluar ")
    pilihan = input("pilih opsi (1/2/3/4/5/6): ")

    if pilihan == "1":
        kegiatan = input("masukkan kegiatan baru:")
        jadwal.append(kegiatan)
    elif pilihan == "2":
        kegiatan = input("masukkan kegiatan yang ingin dihapus:")
        if kegiatan in jadwal:
            jadwal.remove(kegiatan)
            print(f"kegiatan {kegiatan} telah dihapus.")
        else:
            print("Kegiatan tidak ditemukan!") 
    elif pilihan == "3":
        kegiatan_tambahan = input("masukkan kegiatan tambahan!")
        jadwal.extend(kegiatan_tambahan)
        print("kegiatan telah di extend")
        print(f"jadwal baru : {jadwal}")
    elif pilihan == "4":
        kegiatan_tambahan = []
        jadwal.copy(kegiatan_tambahan)
        print(f"jadwal baru : {jadwal}")
    elif pilihan == "5":
        number_list = []
        max_num = int(input("Masukkan Jumlah Angka: "))
        for i in max_num:
            angka = int(input(f"masukkan angka ke-{i}")) 
            number_list.append(angka)
            print(f"angka ke-{i} berhasil dimasukkan")
        number_list.sort()
    elif pilihan == "6":
        print("Suwon sampun gawe program iki!")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")