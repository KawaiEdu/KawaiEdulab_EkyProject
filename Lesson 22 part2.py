nama = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
vokal = [h for h in nama if h in 'aeioudvmpnsqlkgiytb']
print(vokal)

kelipatan_7 = [x for x in range(1, 439) if x % 7 == 0]
print(kelipatan_7)

hewan = ['gajaaahhhhhh','kuciiiinnnggggg','semmmmmuuuuuuttttt']
panjang = [len(h) for h in hewan]
print(panjang)