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