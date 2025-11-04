from data import daftar_perjalanan
import data
from dipanggil import clear
from prettytable import PrettyTable

def daftar() -> None:
    clear()
    print("=" * 60)
    print("DAFTAR PERJALANAN")
    print("=" * 60)
    
    perjalanan = []
    i = 0
    while i < len(daftar_perjalanan["Nama"]):
        if daftar_perjalanan["Nama"][i] == data.user_login:
            perjalanan.append(i)
        i += 1
    
    if len(perjalanan) == 0:
        print("\nBelum ada perjalanan yang tercatat.")
    else:
        table = PrettyTable()
        table.field_names = ["No", "Nama Perjalanan", "Destinasi", "Tanggal", "Durasi", "Budget", "Cerita"]
        
        table.align["No"] = "c"
        table.align["Nama Perjalanan"] = "l"
        table.align["Destinasi"] = "l"
        table.align["Tanggal"] = "c"
        table.align["Durasi"] = "c"
        table.align["Budget"] = "r"
        table.align["Cerita"] = "l"
        
        table.max_width["Cerita"] = 40
        
        nomor = 1
        for idx in perjalanan:
            table.add_row([
                nomor,
                daftar_perjalanan["Nama Perjalanan"][idx],
                daftar_perjalanan["Destinasi"][idx],
                daftar_perjalanan["Tanggal"][idx],
                daftar_perjalanan["Durasi"][idx],
                f"Rp {daftar_perjalanan['Budget'][idx]}",
                daftar_perjalanan["Cerita"][idx]
            ])
            nomor += 1
        
        print(table)
    
    input("\nTekan Enter untuk kembali...")