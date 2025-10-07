import os
from time import sleep

username = "Mutia"
password = "040"

for i in range(0,5):
        un = input("Masukkan Username Anda : ")
        ps = input("Masukkan Password Anda : ")
        if un != username and ps != password:
            print("Password Salah. Sisa Percobaan : ", 4-i)
            if i == 4:
                print("\n"+"|            Program Keluar            |"+"\n")
            continue
        print("\n"+"|            Login Berhasil            |"+"\n")
        break

if i < 4:
    jawab = 'ya' or 'Ya' or 'Iya' or 'iya'
    while (jawab == 'ya' or jawab == 'Ya' or jawab == 'Iya' or jawab == 'iya'):

        print("=" * 50)
        print("|            PENENTUAN JENIS SEGITIGA            |")
        print("=" * 50)

        print("Masukkan panjang ketiga sisi segitiga:")
        a = float(input("Sisi A : "))
        b = float(input("Sisi B : "))
        c = float(input("Sisi C : "))

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
            print("     Hitung Juga Luasnya ")
            print("-" * 30)
    
            alas = float(input("Masukkan Alasnya : "))
            tinggi = float(input("Masukkan Tingginya : "))
    
            luas = (1/2 * alas * tinggi)

            print("Luas Segitiga = ", (luas))
    
        else:
            print("Bukan Segitiga")

        print("\n" + "=" * 50)
        jawab = input("Apakah ingin menghitung lagi? (ya/tidak) : ")

    print("\n Perhitunga Selesai, Terima kasih")
    print("=" * 50 + "\n")

sleep(30)
os.system('cls')
