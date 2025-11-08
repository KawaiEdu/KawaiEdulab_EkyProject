while True:
    print("Program Menghitung BMI")
    TB = float(input("Masukkan tinggi badan")) 
    BB = float(input("Masukkan berat badan"))
    tinggi_badan_meter = tinggi_badan_cm / 100
    bmi = berat_badan / (tinggi_badan_meter * tinggi_badan_meter)
    bmi = float(input("Masukkan BMI: "))
    if bmi < 18.5:
    print("kategori: Kekurangan berat badan.")
    elif bmi <= 24.9:
    print("kategori: Normal.")
    else:i <= 29.9:
    print("kategori: Berat badan berlebih.")
    print("kategori: Obesitas.")
    

    




