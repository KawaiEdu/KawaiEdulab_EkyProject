def c_txt(n):
    if n >= 85:
        return "A"
    elif n >= 75:
        return "B"
    elif n >= 65:
        return "C"
    elif n >= 50:
        return "D"
    else:
        return "E"

d = []
kkm = None

while True:
    print("\n==== Menu Utama ====")
    print("1. input siswa")
    print("2. tampilkan siswa yang lulus")
    print("3. tampilkan nilai akhir dan nilai huruf")
    print("4. keluar")
    
    c = input("pilih menu: ")
    
    if c == "1":
        js = int(input("masukkan jumlah siswa: "))
        d =[{
            "nama" : input(f"nama siswa ke-{i + 1 } "),
            "nilai" : float(input(f"nilai siswa ke-{i + 1 } "))
            }
            for i in range(js)
        ]
        kkm = float(input("masukkan nilai kkm"))
        
        for s in d:
            s["tugas"] = float(input(f"nilai tugas{s}['nama'] "))
            s["ujian"] = float(input(f"nilal ujian {s}['nama'] "))    
            s["nilai"] = round(0.3 * s["tugas"] + 0.7 * s["ujian"], 2)   
            
        print("data siswa berhasil disimpan")
        
    elif c == "2":
        if not d:
            print("data belum dimasukkan")
            continue
        sl = [s["nama"] for s in d if s["nilai"] >= kkm]
        print("\nsiswa yang lulus berdasarkan nilai awal")
        if sl:
            print(",".join(sl))
        else:
            print("tidak ada siswa yang lulus")
            
    elif c == "3":
        if not d:
            print("fata belum di masukkan")
            continue
        sdnh = [{
            "nama": s["nama"],
            "nilai": s["nilai"],
            "nilai_huruf": c_txt(s["nilai"])}
            for s in d
        ]
        
        print("\ndaftar niali akhir dan nilai huruf")
        for s in sdnh:
            print(f"{s['nama']}:{s['nilai']}:{s['nilai_huruf']}")
            
    elif c == "4":
        print("terima kasih telah menggunakan program")
        break
    else:
        print("inpuuuuutttttttt tidaaaakkkkkkk valiiiiiiidddddddddddddddd")    