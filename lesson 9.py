def celsius_ke_fahrenheit(celsius):
    return celsius * 9/5 + 32
def celsius_ke_reamur(celsius):
    return 4/5 * celsius
def celsius_ke_kelvin(celsius):
    return celsius + 273.15

while True:
    print("1. menghitung celsius ke fahrenheit")
    print("2. menghitung celsius ke reamur")
    print("3. menghitung celsius ke kelvin")
    celsius = int(input("masukkan suhu"))

    pilihanmenu = int(input("pilihan"))

    if pilihanmenu==1:
        suhu = celsius_ke_fahrenheit(celsius)
        print(suhu)

    if pilihanmenu==2:
        suhu = celsius_ke_reamur(celsius)
        print(suhu)

    if pilihanmenu==3:
        suhu = celsius_ke_kelvin(celsius)
        print(suhu)
