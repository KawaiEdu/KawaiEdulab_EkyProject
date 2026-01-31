friend = []

while True:
    teman = input("siapa name your teman: ")
    if teman.lower()=="stop":
        break
    elif teman.strip():
        friend.append(teman.strip())
    if not friend:
        print("daftar kosong woy")
    else:
        for teman in friend:
            print("hai,",friend)