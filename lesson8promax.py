while True:
    print("Program Menghitung BMI")
    TB = float(input("Masukkan tinggi badan")) 
    BB = float(input("Masukkan berat badan"))
    tinggi_badan_meter = TB / 100
    bmi = BB / (tinggi_badan_meter * tinggi_badan_meter)
    print (bmi)
    if bmi < 18.5:
        print("kategori: Kekurangan berat badan.")
    elif bmi >= 18.5 and bmi < 25:
        print("kategori: Normal.")
    elif bmi >= 25 and bmi < 29.9:
        print("kategori: Berat badan berlebih.")
    else:
        print("kategori: Obesitas.")

    

    




