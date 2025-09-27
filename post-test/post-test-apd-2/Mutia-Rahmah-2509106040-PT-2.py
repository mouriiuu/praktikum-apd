# List berisi int, float, string (numerik), dan boolean
daftar_data = [10, 2.5, "3.14", True]

print("=== SEBELUM DIUBAH ===")
print("1.", "nilai =", daftar_data[0], "| tipe =", type(daftar_data[0]))
print("2.", "nilai =", daftar_data[1], "| tipe =", type(daftar_data[1]))
print("3.", "nilai =", daftar_data[2], "| tipe =", type(daftar_data[2]))
print("4.", "nilai =", daftar_data[3], "| tipe =", type(daftar_data[3]))


# penjumlahan integer dan float
hasil_penjumlahan_1 = daftar_data[0] + daftar_data[1]
print ("hasil penjumlahan = ",hasil_penjumlahan_1)


nilai0_baru = str(daftar_data[0])   
nilai1_baru = int(daftar_data[1])    
nilai2_baru = float(daftar_data[2]) 
nilai3_baru = int(daftar_data[3])

daftar_setelah = [nilai0_baru, nilai1_baru, nilai2_baru, nilai3_baru]

print("\n=== SESUDAH DIUBAH ===")
print("1.", "nilai =", daftar_setelah[0], "| tipe =", type(daftar_setelah[0]))
print("2.", "nilai =", daftar_setelah[1], "| tipe =", type(daftar_setelah[1]))
print("3.", "nilai =", daftar_setelah[2], "| tipe =", type(daftar_setelah[2]))
print("4.", "nilai =", daftar_setelah[3], "| tipe =", type(daftar_setelah[3]))

# penjumlahan integer dan float
hasil_penjumlahan_2 = daftar_setelah[2] + daftar_setelah[1]
print ("hasil penjumlahan = ",hasil_penjumlahan_2)