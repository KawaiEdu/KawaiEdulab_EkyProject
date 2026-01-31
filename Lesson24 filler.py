def pola_segitiga_kanan(n):
    for i in range(1, n+1):
        for j in range(i):
            print("*", end="")
        print()

def pola_segitiga_kiri(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end="")
        for k in range(i):
            print("*", end="")
        print()

def pola_segitiga_terbalik(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end="")
        print()

def pola_piramida(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end="")
        for k in range(2*i - 1):
            print("*", end="")
        print()

def main():
    print("program pola bintang")
    print("1. segitiga rata kiri")
    print("2. segitiga rata kanan")
    print("3. segitiga terbalik")
    print("4. pola segitiga piramida")
    c = int(input("masukkan pilihan:"))
    t = int(input("masukkan jumlah baris:"))
    if c == 1:
        pola_segitiga_kiri(t)
    elif c == 2:
        pola_segitiga_kanan(t)
    elif c == 3:
        pola_segitiga_terbalik(t)
    elif c == 4:
        pola_piramida(t)
    else:
        print("pilihan tidak valid")

while True:
    main()