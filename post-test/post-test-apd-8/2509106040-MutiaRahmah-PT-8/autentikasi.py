from data import daftar_users
import data
from dipanggil import clear

def login() -> bool:
    clear()
    print("=" * 60)
    print("LOGIN")
    print("=" * 60)

    username_input = input("Username: ").strip()
    password_input = input("Password: ").strip()

    ketemu = False
    if username_input in daftar_users["Username"]:
        idx = daftar_users["Username"].index(username_input)
        if (idx < len(daftar_users["Password"]) and daftar_users["Password"][idx] == password_input):
            ketemu = True
            data.user_login = username_input

    if ketemu:
        print("\nLogin berhasil! Selamat datang", data.user_login)
        input("\nTekan Enter untuk melanjutkan...")
        return True
    else:
        print("\nUsername atau password salah!")
        input("\nTekan Enter untuk kembali...")
        return False


def register() -> None:
    clear()
    print("=" * 60)
    print("REGISTER AKUN BARU")
    print("=" * 60)

    username_baru = input("Username baru: ").strip()
    if username_baru == "":
        print("\nUsername tidak boleh kosong!")
        input("\nTekan Enter untuk kembali...")
        return

    if username_baru in daftar_users["Username"]:
        print("\nUsername sudah digunakan! Pilih username lain.")
        input("\nTekan Enter untuk kembali...")
        return

    password_baru = input("Password baru: ").strip()
    if password_baru == "":
        print("\nPassword tidak boleh kosong!")
        input("\nTekan Enter untuk kembali...")
        return

    daftar_users["Username"].append(username_baru)
    daftar_users["Password"].append(password_baru)
    print("\nRegister berhasil! Silakan login.")
    input("\nTekan Enter untuk kembali...")

