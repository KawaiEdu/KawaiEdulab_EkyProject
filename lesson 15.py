daftar_belanja = set()

while True:
    item = input("masukkan item belanja (atau 'selesai' untuk berhenti): ")
    if item.lower() == "selesai":
        break
    daftar_belanja.add(item)

print("Daftar Belanja Unik Anda:")
for item in daftar_belanja:
    print(f"- {item}")