from data import daftar_perjalanan
import data
from dipanggil import clear

def catat() -> None:
    while True:
        clear()
        print("=" * 60)
        print("CATAT PERJALANAN BARU")
        print("=" * 60)

        try:
            nama_perjalanan = input("Nama Perjalanan : ").strip()
            if not nama_perjalanan:
                raise ValueError("\nNama perjalanan tidak boleh kosong!")

            destinasi = input("Destinasi : ").strip()
            if not destinasi:
                raise ValueError("\nDestinasi tidak boleh kosong!")

            tanggal = input("Tanggal Pergi : ").strip()
            durasi = input("Berapa Lama : ").strip()

            budget = input("Budget (angka saja) : ").strip()
            if not budget.isdigit():
                raise ValueError("\nBudget harus berupa angka!")

            cerita = input("Cerita/Experience : ").strip()

            daftar_perjalanan["Nama"].append(data.user_login)
            daftar_perjalanan["Nama Perjalanan"].append(nama_perjalanan)
            daftar_perjalanan["Destinasi"].append(destinasi)
            daftar_perjalanan["Tanggal"].append(tanggal)
            daftar_perjalanan["Durasi"].append(durasi)
            daftar_perjalanan["Budget"].append(budget)
            daftar_perjalanan["Cerita"].append(cerita)

            print("\nPerjalanan berhasil dicatat!")
            input("\nTekan Enter untuk kembali ke menu...")
            return

        except ValueError as e:
            print(e)
            ulang = input("\nCoba isi lagi? (ya/tidak): ").strip().lower()
            if ulang in ("ya", "y"):
                continue
            else:
                return