from data import daftar_perjalanan
import data
from dipanggil import clear
from prettytable import PrettyTable

def update() -> None:
    clear()
    while True:
        clear()
        print("=" * 60)
        print("EDIT PERJALANAN")
        print("=" * 60)
        try:
            perjalanan_saya = [
                i
                for i in range(len(daftar_perjalanan["Nama"]))
                if daftar_perjalanan["Nama"][i] == data.user_login
            ]
            if not perjalanan_saya:
                raise ValueError("Belum ada perjalanan yang bisa diedit.")
            
            table = PrettyTable()
            table.field_names = ["No", "Nama Perjalanan", "Destinasi", "Tanggal", "Durasi", "Budget"]
            
            for nomor, idx in enumerate(perjalanan_saya, start=1):
                table.add_row([
                    nomor,
                    daftar_perjalanan['Nama Perjalanan'][idx],
                    daftar_perjalanan['Destinasi'][idx],
                    daftar_perjalanan['Tanggal'][idx],
                    daftar_perjalanan['Durasi'][idx],
                    f"Rp {daftar_perjalanan['Budget'][idx]}"
                ])
            
            print("\nDaftar Perjalanan:")
            print(table)
            
            pilih_edit = input("\nPilih nomor perjalanan yang mau diedit (atau ketik 'batal'): ").strip()
            if pilih_edit.lower() == "batal":
                break
            if not pilih_edit.isdigit():
                raise ValueError("Input harus berupa angka!")
            pilihan_edit = int(pilih_edit) - 1
            if pilihan_edit < 0 or pilihan_edit >= len(perjalanan_saya):
                raise ValueError("Nomor perjalanan tidak valid!")
            
            index_dict = perjalanan_saya[pilihan_edit]
            clear()
            print("=" * 60)
            print("EDIT DATA PERJALANAN")
            print("=" * 60)
            
            current_table = PrettyTable()
            current_table.field_names = ["Field", "Nilai Saat Ini"]
            current_table.align["Field"] = "l"
            current_table.align["Nilai Saat Ini"] = "l"
            
            nama_sekarang = daftar_perjalanan["Nama Perjalanan"][index_dict]
            destinasi_sekarang = daftar_perjalanan["Destinasi"][index_dict]
            tanggal_sekarang = daftar_perjalanan["Tanggal"][index_dict]
            durasi_sekarang = daftar_perjalanan["Durasi"][index_dict]
            budget_sekarang = daftar_perjalanan["Budget"][index_dict]
            cerita_sekarang = daftar_perjalanan["Cerita"][index_dict]
            
            current_table.add_row(["Nama Perjalanan", nama_sekarang])
            current_table.add_row(["Destinasi", destinasi_sekarang])
            current_table.add_row(["Tanggal", tanggal_sekarang])
            current_table.add_row(["Durasi", durasi_sekarang])
            current_table.add_row(["Budget", f"Rp {budget_sekarang}"])
            current_table.add_row(["Cerita", cerita_sekarang[:50] + "..." if len(cerita_sekarang) > 50 else cerita_sekarang])
            
            print("\nData Perjalanan Saat Ini:")
            print(current_table)
            print("\nMasukkan data baru (tekan Enter jika tidak ingin mengubah):")
            
            nama_baru = input(f"Nama Perjalanan [{nama_sekarang}]: ").strip()
            if nama_baru:
                daftar_perjalanan["Nama Perjalanan"][index_dict] = nama_baru
            
            destinasi_baru = input(f"Destinasi [{destinasi_sekarang}]: ").strip()
            if destinasi_baru:
                daftar_perjalanan["Destinasi"][index_dict] = destinasi_baru
            
            tanggal_baru = input(f"Tanggal Pergi [{tanggal_sekarang}]: ").strip()
            if tanggal_baru:
                daftar_perjalanan["Tanggal"][index_dict] = tanggal_baru
            
            durasi_baru = input(f"Durasi [{durasi_sekarang}]: ").strip()
            if durasi_baru:
                daftar_perjalanan["Durasi"][index_dict] = durasi_baru
            
            budget_baru = input(f"Budget [{budget_sekarang}]: ").strip()
            if budget_baru:
                if not budget_baru.isdigit():
                    raise ValueError("Budget harus berupa angka!")
                daftar_perjalanan["Budget"][index_dict] = budget_baru
            
            cerita_baru = input(f"Cerita [{cerita_sekarang}]: ").strip()
            if cerita_baru:
                daftar_perjalanan["Cerita"][index_dict] = cerita_baru
            
            print("\n✓ Perjalanan berhasil diedit!")
            input("\nTekan Enter untuk kembali ke menu...")
            break 
        except ValueError as e:
            print(e)
            input("\nTekan Enter untuk mencoba lagi...")
            continue