# fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\nselamat datang diprogram daaftar tugas!")
    print("1.tambah tugas")
    print("2.tampilkan daftar tugas")
    print("3.hapus tugas")
    print("4.simpan  daftar ke file")
    print("5.muat daftar dari file")
    print("6.keluar")
# fungsi untuk menambah tugas
def tambah_tugas(daftar):
    tugas =input("masukkan nama tugas!")
    daftar.append(tugas)
    print("{}berhasil tambahkan ke daftar tugas.".format("tugas"))
    
# fungsi untuk menampilkan tugas
def tampilkan_tugas(daftar):
    if daftar:
        print("\nDaftar tugas:")
        for i, tugas in enumerate(daftar, start=1):
            print("{}. {}".format(i,tugas))
    else:
        print("daftar tugas kosong.")
# fungsi untuk menghapus tugas
def hapus_tugas(daftar):
    tampilkan_tugas(daftar)
    try:
        nomor = int(input("masukkan nomor tugas yang ingin dihapus:"))
        if 1 <= nomor <= len(daftar):
            tugas = daftar.pop(nomor -1)
            print("{}berhasil dihapus dari daftar tugas".format(tugas))
        else:
            print("nomor tugas tidak valid")
    except ValueError:
        print("input harus angka woy")
# fungsi untuk menyimpan daftar ke file
def simpan_daftar(daftar):
    try:
        with open("daftar_tugas.txt", "w") as file:
            for tugas in daftar:
                file.write(tugas+"\n")
                print("✅ daftar tugas berhasil disimpan ke file.")
    except Exception as e:
        print("⚠ terjadi kesalahan woy saat menyimpan: {}".format (e))
# fungsi untuk memuat daftar drai file
def muat_daftar():
    try:
        with open("daftar_tugas.txt", "r") as file:
            daftar = [line.strip() for line in file]
        print("✅ Daftar tugas berhasil dimuat dari file.")
        return daftar
    except IOError: # Gunakan IOError agar kompatibel dengan Python 3.4
        print("⚠ File daftar tugas tidak ditemukan. Membuat daftar baru.")
        return[]
    except Exception as e:
        print("⚠ terjadi kesalahan saat memuat: {}".format(e))
        return[]
# program utama
def main():
    daftar = muat_daftar() # Memuat daftar dari file saat program dimulai

    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan (1-6): ")

        if pilihan == "1":
            tambah_tugas(daftar)
        elif pilihan == "2":
            tampilkan_tugas(daftar)
        elif pilihan == "3":
            hapus_tugas(daftar)  
        elif pilihan == "4":
            simpan_daftar(daftar)  
        elif pilihan == "5":
            daftar = muat_daftar()
        elif pilihan == "6":
            print("Suwon all, babai guys ")
            break
        else:
            print("⚠ Pilihan tidak valid. Silakan coba lagi.")
            
if __name__=="_main_":
    main()