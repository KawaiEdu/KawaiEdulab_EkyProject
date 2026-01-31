for i in range(1, 11):
    if i == 5:
        break
    print(i)
    
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
    
for huruf in "PYTHON":
    if huruf in "AEIOU":
        pass # nanti diisi logika khusus vokal
    else:
        print(huruf)
        
angka = [0, -2, 4, 7, -1, 9, 12]
target = 9

for a in angka:
    if a < 0:
        continue  # skip negatif
    if a == target:
        print("ketemu:", a)
        break     # berhenti saat ketemu
    print("cek:", a)
    

