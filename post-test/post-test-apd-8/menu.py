from autentikasi import login, register
import data
from dipanggil import clear
from read_jurnal import daftar
from create_jurnal import catat
from update_jurnal import update
from delete_jurnal import hapus
from logout_akun import out
import inquirer

def menu_awal() -> None:
    while True:
        clear()
        print("=" * 60)
        print("SELAMAT DATANG DI APLIKASI JURNAL PERJALANAN")
        print("=" * 60)
        
        pertanyaan = [
            inquirer.List('menu',
                         message="Pilih menu",
                         choices=[
                             'Login',
                             'Register',
                             'Keluar'
                         ],
                         ),
        ]
        
        try:
            jawaban = inquirer.prompt(pertanyaan)
            
            if jawaban is None:
                clear()
                print("=" * 60)
                print("Terima kasih! Sampai jumpa!")
                print("=" * 60)
                break
            
            if jawaban['menu'] == 'Login':
                if login():
                    menu_login()
            elif jawaban['menu'] == 'Register':
                register()
            elif jawaban['menu'] == 'Keluar':
                clear()
                print("=" * 60)
                print("Terima kasih! Sampai jumpa!")
                print("=" * 60)
                break
                
        except KeyboardInterrupt:
            clear()
            print("=" * 60)
            print("Terima kasih! Sampai jumpa!")
            print("=" * 60)
            break

def menu_login() -> None:
    while True:
        clear()
        print("=" * 60)
        print(f"User: {data.user_login}")
        print("=" * 60)
        
        pertanyaan = [
            inquirer.List('menu',
                         message="Pilih menu utama",
                         choices=[
                             'Lihat perjalanan yang sudah ditempuh',
                             'Catat perjalanan baru',
                             'Edit perjalanan yang sudah ada',
                             'Hapus salah satu perjalanan',
                             'Logout'
                         ],
                         ),
        ]
        
        try:
            jawaban = inquirer.prompt(pertanyaan)
            
            if jawaban is None:
                if out():
                    break
            
            if jawaban['menu'] == 'Lihat perjalanan yang sudah ditempuh':
                daftar()
            elif jawaban['menu'] == 'Catat perjalanan baru':
                catat()
            elif jawaban['menu'] == 'Edit perjalanan yang sudah ada':
                update()
            elif jawaban['menu'] == 'Hapus salah satu perjalanan':
                hapus()
            elif jawaban['menu'] == 'Logout':
                if out():
                    break
                    
        except KeyboardInterrupt:
            if out():
                break