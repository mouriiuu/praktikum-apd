print("=" * 50)
print("|            PENENTUAN JENIS SEGITIGA            |")
print("=" * 50)

print("Masukkan panjang ketiga sisi segitiga:")
a = int(input("Sisi A : "))
b = int(input("Sisi B : "))
c = int(input("Sisi C : "))

print("\n" + "=" * 30)
print("|           HASIL            |")
print("=" * 30)


if (a + b > c) and (a + c > b) and (b + c > a):
    
    if a == b == c:
        print("Segitiga sama sisi, karna ketiga sisinya sama panjang")
    elif a == b or a == c or b == c:
        print("Segitiga sama kaki, karna dua sisinya sama panjang")
    else:
        print("Segitiga sembarang, karna ketiga sisinya berbeda")

    print("\n" + "-" * 30)
    print("Hasil Luas")
    print("-" * 30)
    
    s = (a + b + c) / 2
    luas = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    print("Luas Segitiga = ", (luas))
    
else:
    print("Bukan Segitiga")