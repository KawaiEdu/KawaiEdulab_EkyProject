while True:

    tambah = lambda x, y: x + y
    kurang = lambda x, y: x - y
    kali = lambda x, y: x * y
    bagi = lambda x, y: x / y

    print("Selamat datang di Kalkulator Lambda!")
    x = float(input("Masukkan angka pertama: "))
    y = float(input("Masukkan angka kedua: "))

    if y != 0 and x != 0:
        operasi = input("Pilih operasi (+, -, *, /): ")

        if operasi == '+':
            print("Hasil: ", tambah(x, y))
        elif operasi == '-':
            print("Hasil: ", kurang(x, y))
        elif operasi == '*':
            print("Hasil: ", kali(x, y))
        elif operasi == '/':
            print("Hasil: ", bagi(x, y))
        elif operasi == 'exit':
            print("Keluar dari Program")
            break
        else:
            print("Operasi tidak valid!")

    else:
        print("tidak bisa dibagi dengan 0")