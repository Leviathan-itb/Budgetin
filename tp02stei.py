def segitiga_sama_kaki(H):
    angka = 1
    for i in range(1, H+1):
        if i % 2 == 0:
            for j in range(i):
                print(angka + j, end=' ')
            print()
            angka += i
        else:
            print(angka)
            angka += 1
    for i in range(H-1, 0, -1):
        if i % 2 == 0:
            angka -= i
            for j in range(i):
                print(angka + j, end=' ')
            print()
        else:
            angka -= 1
            print(angka)

H = int(input("Masukkan nilai H: "))
segitiga_sama_kaki(H)
