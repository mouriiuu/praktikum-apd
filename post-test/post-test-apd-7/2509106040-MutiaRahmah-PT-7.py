import os

daftar_users = { "Username" : ["Mutia"], "Password" : ["040"]}

daftar_perjalanan = { "Nama" : ["Mutia"], "Nama Perjalanan" : ["Liburan ke Bali"], "Destinasi" : ["Bali"], 
                     "Tanggal" : ["1 Januari 2025"], "Durasi" : ["5 hari"], "Budget" : ["5000000"], "Cerita" : ["Seru banget"]}

user_login = ""
sudah_login = False

def tampilan_perjalanan(idx):
            print("\nNama Perjalanan  :", daftar_perjalanan["Nama Perjalanan"][idx])
            print("Destinasi        :", daftar_perjalanan["Destinasi"][idx])
            print("Tanggal Pergi    :", daftar_perjalanan["Tanggal"][idx])
            print("Durasi           :", daftar_perjalanan["Durasi"][idx])
            print("Budget           : Rp", daftar_perjalanan["Budget"][idx])
            print("Cerita           :", daftar_perjalanan["Cerita"][idx])

def clear(hilang):
     hilang

def menu():
    while True:
        clear(os.system("cls" if os.name == "nt" else "clear"))
        print("=" * 60)
        print("SELAMAT DATANG DI APLIKASI JURNAL PERJALANAN")
        print("=" * 60)

        print("\n--- MENU AWAL ---")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")

        try :
                pilihan_awal = input("\nPilih menu (1-3): ")
                if not pilihan_awal.isdigit():
                    raise ValueError('Pilihan Harus Angka')

                
                if pilihan_awal == "1":
                    pilihan1()
                elif pilihan_awal == "2":
                    pilihan2()
                elif pilihan_awal == "3":
                    pilihan3()
                
                else:
                    print("Pilihan Tidak Valid")
        except ValueError as e :
            print(e)
            input("\nTekan Enter untuk kembali...")

def pilihan1(): 
    global user_login
    clear(os.system("cls" if os.name == "nt" else "clear"))  
    print("=" * 60)
    print("LOGIN")
    print("=" * 60)

    username_input = input("Username: ")
    password_input = input("Password: ")

    ketemu = False
    if username_input in daftar_users["Username"]:
            idx = daftar_users["Username"].index(username_input)
            if idx < len(daftar_users["Password"]) and daftar_users["Password"][idx] == password_input:
                ketemu = True
                user_login = username_input

    if ketemu == True:
        
        print("\nLogin berhasil! Selamat datang", user_login)
        input("\nTekan Enter untuk melanjutkan...")
        menulogin()
    else:
        print("\nUsername atau password salah!")
        input("\nTekan Enter untuk kembali...")
        return

# ini rekursif bang
def pilihan2():
    clear(os.system("cls" if os.name == "nt" else "clear"))  
    print("=" * 60)
    print("REGISTER AKUN BARU")
    print("=" * 60)

    username_baru = input("Username baru: ")

    if username_baru == "":
        print("\nUsername tidak boleh kosong!")
        input("\nTekan Enter untuk kembali...")
        pilihan2()
        
    else:
        username_sudah_ada = username_baru in daftar_users["Username"]

        if username_sudah_ada == True:
            print("\nUsername sudah digunakan! Pilih username lain.")
            input("\nTekan Enter untuk kembali...")
            pilihan2()
            
        else:
            password_baru = input("Password baru: ")

            if password_baru == "":
                print("\nPassword tidak boleh kosong!")
                input("\nTekan Enter untuk kembali...")
                pilihan2()
                
            else:
                daftar_users["Username"].append(username_baru)
                daftar_users["Password"].append(password_baru)
                user_login = ""
                print("\nRegister berhasil! Silakan login.")
                input("\nTekan Enter untuk kembali...")
                return

def pilihan3():
    clear(os.system("cls" if os.name == "nt" else "clear"))
    print("=" * 60)
    print("Terima kasih! Sampai jumpa!")
    print("=" * 60)
    exit()
        


def pilihan_menu1():
    clear(os.system("cls" if os.name == "nt" else "clear"))          
    print("=" * 60)
    print("DAFTAR PERJALANAN")
    print("=" * 60)

    perjalanan = []
    i = 0
    while i < len(daftar_perjalanan["Nama"]):
        if daftar_perjalanan["Nama"][i] == user_login:
            perjalanan.append(i)
        i += 1

    if len(perjalanan) == 0:
        print("\nBelum ada perjalanan yang tercatat.")
    else:
        nomor = 1
        for idx in perjalanan:
            print("\nPerjalanan", nomor)
            print("-" * 40)
            tampilan_perjalanan(idx)
            nomor += 1

    input("\nTekan Enter untuk kembali...")

def pilihan_menu2():
    clear(os.system("cls" if os.name == "nt" else "clear"))       
    print("=" * 60)
    print("CATAT PERJALANAN BARU")
    print("=" * 60)
    try:
        nama_perjalanan = input("\nNama Perjalanan         : ")
        if nama_perjalanan == "":
            raise ValueError("\nNama perjalanan tidak boleh kosong!")
        
        destinasi = input("Destinasi               : ")
        if destinasi == "":
            raise ValueError("\nDestinasi tidak boleh kosong!")
        
        tanggal = input("Tanggal Pergi           : ")
        durasi = input("Berapa Lama             : ")

        budget = input("Budget (angka saja)     : ")
        if budget.isdigit() == False:
            raise ValueError("\nBudget harus berupa angka!")
        
        cerita = input("Cerita/Experience       : ") 

        daftar_perjalanan["Nama"].append(user_login)
        daftar_perjalanan["Nama Perjalanan"].append(nama_perjalanan)
        daftar_perjalanan["Destinasi"].append(destinasi)
        daftar_perjalanan["Tanggal"].append(tanggal)
        daftar_perjalanan["Durasi"].append(durasi)
        daftar_perjalanan["Budget"].append(budget)
        daftar_perjalanan["Cerita"].append(cerita)
        print("\nPerjalanan berhasil dicatat!")

    except ValueError as e:
        print(e)
    finally:
        input("\nTekan Enter untuk kembali...")

def pilihan_menu3():
    clear(os.system("cls" if os.name == "nt" else "clear"))
    print("=" * 60)
    print("EDIT PERJALANAN")
    print("=" * 60)

    try:
        perjalanan_saya = [
            i for i in range(len(daftar_perjalanan["Nama"]))
            if daftar_perjalanan["Nama"][i] == user_login
        ]

        if len(perjalanan_saya) == 0:
            raise ValueError("Belum ada perjalanan yang bisa diedit.")

        print("\nDaftar Perjalanan:")
        for nomor, idx in enumerate(perjalanan_saya, start=1):
            print(f"{nomor}. {daftar_perjalanan['Nama Perjalanan'][idx]} - {daftar_perjalanan['Destinasi'][idx]}")

        pilih_edit = input("\nPilih nomor perjalanan yang mau diedit: ").strip()
        if not pilih_edit.isdigit():
            raise ValueError("Input harus berupa angka!")

        pilihan_edit = int(pilih_edit) - 1
        if pilihan_edit < 0 or pilihan_edit >= len(perjalanan_saya):
            raise ValueError("Nomor perjalanan tidak valid!")

        index_dict = perjalanan_saya[pilihan_edit]

        clear(os.system("cls" if os.name == "nt" else "clear"))
        print("=" * 60)
        print("EDIT DATA PERJALANAN")
        print("=" * 60)
        print("\nMasukkan data baru (tekan Enter jika tidak ingin mengubah):")

        nama_sekarang = daftar_perjalanan["Nama Perjalanan"][index_dict]
        destinasi_sekarang = daftar_perjalanan["Destinasi"][index_dict]
        tanggal_sekarang = daftar_perjalanan["Tanggal"][index_dict]
        durasi_sekarang = daftar_perjalanan["Durasi"][index_dict]
        budget_sekarang = daftar_perjalanan["Budget"][index_dict]
        cerita_sekarang = daftar_perjalanan["Cerita"][index_dict]

        nama_baru = input(f"Nama Perjalanan [{nama_sekarang}]: ").strip()
        if nama_baru != "":
            daftar_perjalanan["Nama Perjalanan"][index_dict] = nama_baru

        destinasi_baru = input(f"Destinasi [{destinasi_sekarang}]: ").strip()
        if destinasi_baru != "":
            daftar_perjalanan["Destinasi"][index_dict] = destinasi_baru

        tanggal_baru = input(f"Tanggal Pergi [{tanggal_sekarang}]: ").strip()
        if tanggal_baru != "":
            daftar_perjalanan["Tanggal"][index_dict] = tanggal_baru

        durasi_baru = input(f"Durasi [{durasi_sekarang}]: ").strip()
        if durasi_baru != "":
            daftar_perjalanan["Durasi"][index_dict] = durasi_baru

        budget_baru = input(f"Budget [{budget_sekarang}]: ").strip()
        if budget_baru != "":
            if not budget_baru.isdigit():
                raise ValueError("Budget harus berupa angka!")
            daftar_perjalanan["Budget"][index_dict] = budget_baru

        cerita_baru = input(f"Cerita [{cerita_sekarang}]: ").strip()
        if cerita_baru != "":
            daftar_perjalanan["Cerita"][index_dict] = cerita_baru

        print("\nPerjalanan berhasil diedit!")

    except ValueError as e:
        print(e)
    finally:
        input("\nTekan Enter untuk kembali...")
        clear(os.system("cls" if os.name == "nt" else "clear"))

def pilihan_menu4():
    clear(os.system("cls" if os.name == "nt" else "clear"))    
    print("=" * 60)
    print("HAPUS PERJALANAN")
    print("=" * 60)
    try:
        perjalanan_saya = []
        i = 0
        while i < len(daftar_perjalanan["Nama"]):
            if daftar_perjalanan["Nama"][i] == user_login:
                perjalanan_saya.append(i)
            i = i + 1

        if len(perjalanan_saya) == 0:
            raise ValueError("\nBelum ada perjalanan yang bisa dihapus.")

        else:
            print("\nDaftar Perjalanan:")
            nomor = 1
            for idx in perjalanan_saya:
                print(nomor, ".", daftar_perjalanan["Nama Perjalanan"][idx], "-", daftar_perjalanan["Destinasi"][idx])
                nomor = nomor + 1

            pilih_hapus = input("\nPilih nomor perjalanan yang mau dihapus: ")
            if pilih_hapus.isdigit() == False:
                raise ValueError("\nInput harus berupa angka!")
            
            pilihan_hapus = int(pilih_hapus) - 1
            if pilihan_hapus < 0 or pilihan_hapus >= len(perjalanan_saya):
                raise ValueError("\nNomor tidak valid!")
            else:
                index_asli = perjalanan_saya[pilihan_hapus]
                nama_perjalanan_terpilih = daftar_perjalanan["Nama Perjalanan"][index_asli]

                konfirmasi = input(
                    "Yakin mau hapus '" + nama_perjalanan_terpilih + "'? (ya/tidak): "
                )

                if konfirmasi == "ya" or konfirmasi == "Ya" or konfirmasi == "YA":
                    daftar_perjalanan["Nama"].pop(index_asli)
                    daftar_perjalanan["Nama Perjalanan"].pop(index_asli)
                    daftar_perjalanan["Destinasi"].pop(index_asli)
                    daftar_perjalanan["Tanggal"].pop(index_asli)
                    daftar_perjalanan["Durasi"].pop(index_asli)
                    daftar_perjalanan["Budget"].pop(index_asli)
                    daftar_perjalanan["Cerita"].pop(index_asli)

                    print("\nPerjalanan berhasil dihapus!")
                else:
                    print("\nPenghapusan dibatalkan.")

    except ValueError as e:
        print(e)
    finally:
        input("\nTekan Enter untuk kembali...")
        clear(os.system("cls" if os.name == "nt" else "clear"))

def pilihan_menu5():
    clear(os.system("cls" if os.name == "nt" else "clear"))
    print("=" * 60)
    print("LOGOUT")
    print("=" * 60)

    try:
        konfirmasi_logout = input("\nYakin mau logout? (ya/tidak): ").strip().lower()

        if konfirmasi_logout == "ya":
            clear(os.system("cls" if os.name == "nt" else "clear"))
            print("\nLogout berhasil!")
            print("Terima kasih sudah menggunakan Jurnal Perjalanan")
            print("Kembali ke Menu Awal...")
            input("\nTekan Enter untuk melanjutkan...")
            clear(os.system("cls" if os.name == "nt" else "clear"))
        elif konfirmasi_logout == "tidak":
            print("\nLogout dibatalkan.")
            input("\nTekan Enter untuk kembali...")
            clear(os.system("cls" if os.name == "nt" else "clear"))
            menulogin()
        else:
            raise ValueError("Input tidak valid! Harus 'ya' atau 'tidak'.")

    except ValueError as e:
        print(e)
        input("\nTekan Enter untuk kembali...")
        clear(os.system("cls" if os.name == "nt" else "clear"))
        return False

def menulogin():
    while True:
        clear(os.system("cls" if os.name == "nt" else "clear"))
        print("=" * 60)
        print("User:", user_login)
        print("=" * 60)

        print("\n--- MENU UTAMA ---")
        print("1. Lihat perjalanan yang sudah ditempuh")
        print("2. Catat perjalanan baru")
        print("3. Edit perjalanan yang sudah ada")
        print("4. Hapus salah satu perjalanan")
        print("5. Logout")

        try:
            pilihan = input("\nMasukkan pilihan (1-5): ").strip()
            if not pilihan.isdigit():
                raise ValueError("Pilihan harus berupa angka!")

            if pilihan == "1":
                pilihan_menu1()
            elif pilihan == "2":
                pilihan_menu2()
            elif pilihan == "3":
                pilihan_menu3()
            elif pilihan == "4":
                pilihan_menu4()
            elif pilihan == "5":
                pilihan_menu5()
                break
            else:
                print("Pilihan tidak valid!")

        except ValueError as e:
            print(e)
            input("\nTekan Enter untuk kembali...")

if __name__ == "__main__":
            menu()