from dipanggil import clear

def out() -> bool:
    clear()
    print("=" * 60)
    print("LOGOUT")
    print("=" * 60)

    try:
        konfirmasi_logout = input("\nYakin mau logout? (ya/tidak): ").strip().lower()

        if konfirmasi_logout == "ya":
            clear()
            print("\nLogout berhasil!")
            print("Terima kasih sudah menggunakan Jurnal Perjalanan")
            print("Kembali ke Menu Awal...")
            input("\nTekan Enter untuk melanjutkan...")
            return True

        elif konfirmasi_logout == "tidak":
            print("\nLogout dibatalkan.")
            input("\nTekan Enter untuk kembali...")
            return False
        else:
            raise ValueError("Input tidak valid! Harus 'ya' atau 'tidak'.")

    except ValueError as e:
        print(e)
        input("\nTekan Enter untuk kembali...")
        clear()
        return False