while True:
    print("\nMENU: [1] Sapa [2] Hitung [0] Keluar")
    pilih = input("pilih: ").strip()
    if not pilih:
        continue
    if pilih == "0":
        print("Sampai Jumpa!")
        break
    elif pilih == "1":
        nama = input("Namamu: ").strip()
        if not nama:
            continue
        print("Halo, ", nama + "!")
    elif pilih == "2":
        n = int(input("Masukkan n: "))
        total = 0
        for i in range(1, n+1):
            total += i
        print("Jumlah 1..", n, "=", total)
    else:
        print("Pilihan tidak valid.")