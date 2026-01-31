def kalkulator():
    try:
        angka1 = float(input("masukkan angka pertama:"))
        angka2 = float(input("masukkan angka kedua:"))
        operasi = input("msukkan operasi(+,-,*,/):")
        if operasi == "+":
            hasil = angka1 + angka2
        elif operasi == "-":
            hasil = angka1 - angka2
        elif operasi == "*":
            hasil = angka1 * angka2
        elif operasi == "/": 
            hasil = angka1 / angka2
        else:
            print("operasi tidak valid!")
        return print(f"hasil:{hasil}")
    
    except ValueError:
        print("input harus angka!")
        
    except ZeroDivisionError:
        print("tidak bia dibagi dengan nol!")

while True:
    print("\nkalkulator sederhana")
    kalkulator()
    lagi = input("apakah anda ingin menghitung lagi?(ya/tidak): ")
    if lagi.lower()!="ya":
        print("terima kasih! sampai jumpa.")
        break