import os
from data import daftar_perjalanan

def tampilan_perjalanan(idx):
            print("\nNama Perjalanan  :", daftar_perjalanan["Nama Perjalanan"][idx])
            print("Destinasi        :", daftar_perjalanan["Destinasi"][idx])
            print("Tanggal Pergi    :", daftar_perjalanan["Tanggal"][idx])
            print("Durasi           :", daftar_perjalanan["Durasi"][idx])
            print("Budget           : Rp", daftar_perjalanan["Budget"][idx])
            print("Cerita           :", daftar_perjalanan["Cerita"][idx])

def clear():
     os.system("cls" if os.name == "nt" else "clear")