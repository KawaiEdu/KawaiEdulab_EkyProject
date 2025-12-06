hari_libur = ("sabtu", "minggu")
hari = input("masukkan hari: ")
if hari in hari_libur:
    print(f"{hari}adalah hari libur!")
else:
    print(f"{hari} adalah hari kerja.")