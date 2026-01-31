kelas = {
    "kelas A": ["nouxx", "everone"],
    "kelas B": ["nl", "lancelords"]
}

for nama_kelas, siswa in kelas.items():
    print(nama_kelas + ":")
    for s in siswa:
        print("-" + s)
    print()

for baris in range(9):
    for kolom in range(4):
        print("hv", end="")
    print()

for i in range(1, 4):
    for j in range(1, 4):
        print(i, "x", j, "=", i*j)
        print("---")

ulang = 1
while ulang <= 3:
    print("welcome to beach island!")
    ulang += 1