bmi = float(input("Masukkan BMI: "))
if bmi < 18.5:
    print("Kekurangan berat badan.")
elif bmi <= 24.9:
    print("Normal.")
elif bmi <= 29.9:
    print("Berat badan berlebih.")
else:
    print("Obesitas.")