from data import daftar_perjalanan
import data
from dipanggil import clear


def hapus() -> None:
    clear()
    print("=" * 60)
    print("HAPUS PERJALANAN")
    print("=" * 60)

    try:
        perjalanan_saya = [i for i, pemilik in enumerate(daftar_perjalanan["Nama"]) if pemilik == data.user_login]

        if not perjalanan_saya:
            raise ValueError("Belum ada perjalanan yang bisa dihapus.")

        print("\nDaftar Perjalanan:")
        for nomor, idx in enumerate(perjalanan_saya, start=1):
            print(f"{nomor}. {daftar_perjalanan['Nama Perjalanan'][idx]} - "f"{daftar_perjalanan['Destinasi'][idx]}")

        pilih_hapus = input("\nPilih nomor perjalanan yang mau dihapus: ").strip()
        if not pilih_hapus.isdigit():
            raise ValueError("Input harus berupa angka!")

        pilihan_hapus = int(pilih_hapus) - 1
        if pilihan_hapus < 0 or pilihan_hapus >= len(perjalanan_saya):
            raise ValueError("Nomor tidak valid!")

        index_asli = perjalanan_saya[pilihan_hapus]
        nama_perjalanan_terpilih = daftar_perjalanan["Nama Perjalanan"][index_asli]

        konfirmasi = input(
            f"Yakin mau hapus '{nama_perjalanan_terpilih}'? (ya/tidak): "
        ).strip().lower()

        if konfirmasi == "ya":
            for k in ("Nama", "Nama Perjalanan", "Destinasi", "Tanggal", "Durasi", "Budget", "Cerita"):
                daftar_perjalanan[k].pop(index_asli)
            print("\nPerjalanan berhasil dihapus!")
        else:
            print("\nPenghapusan dibatalkan.")

    except ValueError as e:
        print(e)
    finally:
        input("\nTekan Enter untuk kembali...")