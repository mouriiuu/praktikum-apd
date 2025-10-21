import os

daftar_users = { "Username" : ["Mutia"], "Password" : ["040"]}

daftar_perjalanan = { "Nama" : ["Mutia"], "Nama Perjalanan" : ["Liburan ke Bali"], "Destinasi" : ["Bali"], 
                     "Tanggal" : ["1 Januari 2025"], "Durasi" : ["5 hari"], "Budget" : ["5000000"], "Cerita" : ["Seru banget"]}

user_login = ""

os.system("cls" if os.name == "nt" else "clear")

print("=" * 60)
print("SELAMAT DATANG DI APLIKASI JURNAL PERJALANAN")
print("=" * 60)

sudah_login = False

while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("=" * 60)
    print("SELAMAT DATANG DI APLIKASI JURNAL PERJALANAN")
    print("=" * 60)

    sudah_login == False
    print("\n--- MENU AWAL ---")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    pilihan_awal = input("\nPilih menu (1-3): ")

    if pilihan_awal == "1":
        os.system("cls" if os.name == "nt" else "clear")
        print("\n" + "=" * 60)
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
            sudah_login = True
            os.system("cls" if os.name == "nt" else "clear")
            print("\nLogin berhasil! Selamat datang", user_login)
            input("\nTekan Enter untuk melanjutkan...")
        else:
            print("\nUsername atau password salah!")
            input("\nTekan Enter untuk kembali...")
            os.system("cls" if os.name == "nt" else "clear")
            continue

    elif pilihan_awal == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("\n" + "=" * 60)
        print("REGISTER AKUN BARU")
        print("=" * 60)

        username_baru = input("Username baru: ")

        if username_baru == "":
            print("\nUsername tidak boleh kosong!")
            input("\nTekan Enter untuk kembali...")
            os.system("cls" if os.name == "nt" else "clear")
        else:
            username_sudah_ada = username_baru in daftar_users["Username"]

            if username_sudah_ada == True:
                print("\nUsername sudah digunakan! Pilih username lain.")
                input("\nTekan Enter untuk kembali...")
                os.system("cls" if os.name == "nt" else "clear")
            else:
                password_baru = input("Password baru: ")

                if password_baru == "":
                    print("\nPassword tidak boleh kosong!")
                    input("\nTekan Enter untuk kembali...")
                    os.system("cls" if os.name == "nt" else "clear")
                else:
                    daftar_users["Username"].append(username_baru)
                    daftar_users["Password"].append(password_baru)
                    user_login = ""
                    print("\nRegister berhasil! Silakan login.")
                    input("\nTekan Enter untuk kembali...")
                    os.system("cls" if os.name == "nt" else "clear")
                    continue

    elif pilihan_awal == "3":
        os.system("cls" if os.name == "nt" else "clear")
        print("\n" + "=" * 60)
        print("Terima kasih! Sampai jumpa!")
        print("=" * 60)
        exit()

    else:
        print("\nPilihan tidak valid!")
        input("\nTekan Enter untuk kembali...")
        os.system("cls" if os.name == "nt" else "clear")
        continue

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 60)
        print("User:", user_login)
        print("=" * 60)

        print("\n--- MENU UTAMA ---")
        print("1. Lihat perjalanan yang sudah ditempuh")
        print("2. Catat perjalanan baru")
        print("3. Edit perjalanan yang sudah ada")
        print("4. Hapus salah satu perjalanan")
        print("5. Logout")

        pilihan = input("\nMasukkan pilihan (1-5): ")

        if pilihan == "1":
            os.system("cls" if os.name == "nt" else "clear")
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
                    print("Nama Perjalanan  :", daftar_perjalanan["Nama Perjalanan"][idx])
                    print("Destinasi        :", daftar_perjalanan["Destinasi"][idx])
                    print("Tanggal Pergi    :", daftar_perjalanan["Tanggal"][idx])
                    print("Durasi           :", daftar_perjalanan["Durasi"][idx])
                    print("Budget           : Rp", daftar_perjalanan["Budget"][idx])
                    print("Cerita           :", daftar_perjalanan["Cerita"][idx])
                    nomor += 1

            input("\nTekan Enter untuk kembali...")

        elif pilihan == "2":
            os.system("cls" if os.name == "nt" else "clear")
            print("=" * 60)
            print("CATAT PERJALANAN BARU")
            print("=" * 60)

            nama_perjalanan = input("\nNama Perjalanan         : ")

            if nama_perjalanan == "":
                print("\nNama perjalanan tidak boleh kosong!")
                input("\nTekan Enter untuk kembali...")
            else:
                destinasi = input("Destinasi               : ")

                if destinasi == "":
                    print("\nDestinasi tidak boleh kosong!")
                    input("\nTekan Enter untuk kembali...")
                else:
                    tanggal = input("Tanggal Pergi           : ")
                    durasi = input("Berapa Lama             : ")
                    budget = input("Budget (angka saja)     : ")

                    if budget.isdigit() == False:
                        print("\nBudget harus berupa angka!")
                        input("\nTekan Enter untuk kembali...")
                    else:
                        cerita = input("Cerita/Experience       : ")
                        daftar_perjalanan["Nama"].append(user_login)
                        daftar_perjalanan["Nama Perjalanan"].append(nama_perjalanan)
                        daftar_perjalanan["Destinasi"].append(destinasi)
                        daftar_perjalanan["Tanggal"].append(tanggal)
                        daftar_perjalanan["Durasi"].append(durasi)
                        daftar_perjalanan["Budget"].append(budget)
                        daftar_perjalanan["Cerita"].append(cerita)

                        print("\nPerjalanan berhasil dicatat!")
                        input("\nTekan Enter untuk kembali...")

        elif pilihan == "3":
            os.system("cls" if os.name == "nt" else "clear")
            print("=" * 60)
            print("EDIT PERJALANAN")
            print("=" * 60)

            perjalanan_saya = []
            i = 0
            while i < len(daftar_perjalanan["Nama"]):
                if daftar_perjalanan["Nama"][i] == user_login:
                    perjalanan_saya.append(i)
                i = i + 1

            if len(perjalanan_saya) == 0:
                print("\nBelum ada perjalanan yang bisa diedit.")
                input("\nTekan Enter untuk kembali...")
            else:
                print("\nDaftar Perjalanan:")
                nomor = 1
                for idx in perjalanan_saya:
                    print(nomor, ".", daftar_perjalanan["Nama Perjalanan"][idx], "-", 
                          daftar_perjalanan["Destinasi"][idx])
                    nomor = nomor + 1

                pilih_edit = input("\nPilih nomor perjalanan yang mau diedit: ")

                if pilih_edit.isdigit() == False:
                    print("\nInput harus berupa angka!")
                    input("\nTekan Enter untuk kembali...")
                else:
                    pilihan_edit = int(pilih_edit) - 1

                    if pilihan_edit < 0 or pilihan_edit >= len(perjalanan_saya):
                        print("\nNomor tidak valid!")
                        input("\nTekan Enter untuk kembali...")
                    else:
                        index_dict = perjalanan_saya[pilihan_edit]

                        print("\nMasukkan data baru (tekan Enter jika tidak ingin mengubah):")

                        nama_sekarang = daftar_perjalanan["Nama Perjalanan"][index_dict]
                        destinasi_sekarang = daftar_perjalanan["Destinasi"][index_dict]
                        tanggal_sekarang = daftar_perjalanan["Tanggal"][index_dict]
                        durasi_sekarang = daftar_perjalanan["Durasi"][index_dict]
                        budget_sekarang = daftar_perjalanan["Budget"][index_dict]
                        cerita_sekarang = daftar_perjalanan["Cerita"][index_dict]

                        nama_baru = input("Nama Perjalanan [" + nama_sekarang + "]: ")
                        if nama_baru != "":
                            daftar_perjalanan["Nama Perjalanan"][index_dict] = nama_baru

                        destinasi_baru = input("Destinasi [" + destinasi_sekarang + "]: ")
                        if destinasi_baru != "":
                            daftar_perjalanan["Destinasi"][index_dict] = destinasi_baru

                        tanggal_baru = input("Tanggal Pergi [" + tanggal_sekarang + "]: ")
                        if tanggal_baru != "":
                            daftar_perjalanan["Tanggal"][index_dict] = tanggal_baru

                        durasi_baru = input("Durasi [" + durasi_sekarang + "]: ")
                        if durasi_baru != "":
                            daftar_perjalanan["Durasi"][index_dict] = durasi_baru

                        budget_baru = input("Budget [" + budget_sekarang + "]: ")
                        if budget_baru != "":
                            if budget_baru.isdigit() == False:
                                print("\nBudget harus berupa angka! Data budget tidak diubah.")
                            else:
                                daftar_perjalanan["Budget"][index_dict] = budget_baru

                        cerita_baru = input("Cerita [" + cerita_sekarang + "]: ")
                        if cerita_baru != "":
                            daftar_perjalanan["Cerita"][index_dict] = cerita_baru

                        print("\nPerjalanan berhasil diedit!")
                        input("\nTekan Enter untuk kembali...")

        elif pilihan == "4":
            os.system("cls" if os.name == "nt" else "clear")
            print("=" * 60)
            print("HAPUS PERJALANAN")
            print("=" * 60)

            perjalanan_saya = []
            i = 0
            while i < len(daftar_perjalanan["Nama"]):
                if daftar_perjalanan["Nama"][i] == user_login:
                    perjalanan_saya.append(i)
                i = i + 1

            if len(perjalanan_saya) == 0:
                print("\nBelum ada perjalanan yang bisa dihapus.")
                input("\nTekan Enter untuk kembali...")
            else:
                print("\nDaftar Perjalanan:")
                nomor = 1
                for idx in perjalanan_saya:
                    print(nomor, ".", daftar_perjalanan["Nama Perjalanan"][idx], "-", daftar_perjalanan["Destinasi"][idx])
                    nomor = nomor + 1

                pilih_hapus = input("\nPilih nomor perjalanan yang mau dihapus: ")

                if pilih_hapus.isdigit() == False:
                    print("\nInput harus berupa angka!")
                    input("\nTekan Enter untuk kembali...")
                else:
                    pilihan_hapus = int(pilih_hapus) - 1

                    if pilihan_hapus < 0 or pilihan_hapus >= len(perjalanan_saya):
                        print("\nNomor tidak valid!")
                        input("\nTekan Enter untuk kembali...")
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

                        input("\nTekan Enter untuk kembali...")

        elif pilihan == "5":
            konfirmasi_logout = input("\nYakin mau logout? (ya/tidak): ")

            if (konfirmasi_logout == "ya" or konfirmasi_logout == "Ya" or konfirmasi_logout == "YA"):
                os.system("cls" if os.name == "nt" else "clear")
                print("\nLogout berhasil!")
                print("Terima kasih sudah menggunakan Jurnal Perjalanan!")
                print("Kembali ke Menu Awal")
                input("\nTekan Enter untuk kembali...")
                os.system("cls" if os.name == "nt" else "clear")
                break
            else:
                print("\nLogout dibatalkan.")
                input("\nTekan Enter untuk kembali...")

        else:
            print("\nPilihan tidak valid!")
            input("\nTekan Enter untuk kembali...")