def diskon(harga, persen):
    potongan = harga * persen / 100
    return harga - potongan

# contoh penggunaan:
print(diskon(100000, 20)) # Output: 80000.0

def halo(nama='Siswa'):
    if nama == 'Siswa':
        print("halo, peserta belajar python!")
    else:
        print(f"halo,{nama}!")
        
 # contoh penggunaan:
halo("rafi") # output: halo, rafi!
halo()       # output: halo, peserta belajar python!
 
def perkalian(a, b=2):
     return a * b

# contoh penggunaan:
print(perkalian(4))    # output: 8 (karena b=2)
print(perkalian(4,5))  # output: 20