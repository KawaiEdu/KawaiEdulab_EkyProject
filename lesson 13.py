hari_libur = ("sabtu", "minggu")
hari = input("masukkan hari: ")
if hari in hari_libur:
    print(f"{hari}adalah hari libur!")
else:
    print(f"{hari} adalah hari kerja.")

kamus_buah = {
    "apel": "buah berwarna merah",
    "jeruk": "buah berwarna oranye",
    "pisang": "buah berwarna kuning",
}

buah = input("masukkan nama buah:")
if buah in kamus_buah:
    print(f"{buah}: {kamus_buah[buah]}")
else:
    print("buah tidak ditemukan dalam kamus.")