# For the first problem, we’re going back to the old good day C++ Problem. Given any integer input, a triangle must be printed with the corresponding height. 

tinggi = int(input("Masukkan Tinggi Segitiga: "))

for kolom in range(1, tinggi + 1):
    spasi = tinggi - kolom
    perbintangan = 2 * kolom - 1
    print(' ' * spasi + '*' * perbintangan)
