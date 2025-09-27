# angka = 5

# if angka > 5:
#    print("angka lebih besar dari 5")

# cuaca = "hujan"

#if cuaca == "hujan":
#    print("Dirumah aja")
#else :
#    print("Nongkrong")


# if nilai >= 70:
#     print("lulus")
# else:
#     print("tidak lulus")
# nilai = 70
# nilai = int(input("nilai : "))

# status = "lulus" if nilai>= 70 else "tidak lulus"
# print(status)

#contoh 3

# cuaca = 'mendung'

# if cuaca == "hujan"
#    print("Dirumah aja")
# elif cuaca == 'mendung':
#    print("Makan mie")

# else :
#    print("nongkrong")

#contoh 4

# usia = int(input("Masukkan Usia Anda : "))

# if usia <= 0:
#     print("usia tidak valid")
# elif usia <= 13:
#     print("anak-anak")
# elif usia <= 18:
#     print("remaja")
# elif usia <= 40:
#     print("dewasa")
# else :
#     print("tua")

#contoh 5

# nilai = int(input("Masukkan Nilai Anda : "))

# if nilai >= 90:
#     print("Nilai anda A")
# elif nilai >= 70:
#     print("Nilai anda B")
# elif nilai >= 60:
#     print("Nilai anda C")
# else:
#     print("Nilai anda D")

# Neseted if

# a = 2
# b = 5
# c = 6

# if a<b :
#     if a <c:
#         print ("A paling kecil")
#     else:
#         print("C lebih kecil dari A")
# elif a>c :
#     print("C paling besar")
# else:
#     print("A paling besar")

# Studi kasus

# tinggi = float(input("Masukkan Tinggi Badan : "))

# status = "Diizinkan Masuk Wahana" if tinggi>= 145 else "Tidak Bisa Naik Wahana"
# print(status)

# a = 100000
# b = 50000
# total = int(input("Masukkan Total Belanja : "))

# if total >100000:
#     diskon = total*.02
#     bayar = total-diskon
#     print("selamat anda mendapatkan diskon 20%, dan hanya membayar : ", {bayar})
# elif total >50000:
#     diskon = total*.01
#     bayar = total-diskon
#     print("selamat anda mendapatkan diskon 20%, dan hanya membayar : ", {bayar})
# else:
#     bayar = total
#     print("Maaf anda tidak mendapakan diskon", {bayar})


nilai = int(input("masukkan nilai : "))
kelas = input("masukkan kelas :")

if nilai >= 80 and (kelas == "A" or kelas =="a"):
    print("IPK 4")
elif nilai >= 80 and (kelas == "B" or kelas =="b"):
    print("IPK 3")

else:
    print("IPK 2")