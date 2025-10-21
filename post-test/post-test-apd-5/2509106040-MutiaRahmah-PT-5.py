import os

daftar_users = [["Mutia", "040"]]

daftar_perjalanan = [["Mutia", "Liburan ke Bali", "Bali", "1 Januari 2025", "5 hari", "5000000", "Seru banget",]]

user_login = ""

os.system("cls" if os.name == "nt" else "clear")

print("=" * 60)
print("SELAMAT DATANG DI APLIKASI JURNAL PERJALANAN")
print("=" * 60)


sudah_login = False

while sudah_login == False:
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
        i = 0

        while i < len(daftar_users):
            if daftar_users[i][0] == username_input:
                if daftar_users[i][1] == password_input:
                    ketemu = True
                    user_login = daftar_users[i][0]
                    break
            i = i + 1

        if ketemu == True:
            sudah_login = True
            os.system("cls" if os.name == "nt" else "clear")
            print("\nLogin berhasil! Selamat datang", user_login)
            input("\nTekan Enter untuk melanjutkan...")
        else:
            print("\nUsername atau password salah!")
            input("\nTekan Enter untuk kembali...")
            os.system("cls" if os.name == "nt" else "clear")

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
            username_sudah_ada = False
            i = 0

            while i < len(daftar_users):
                if daftar_users[i][0] == username_baru:
                    username_sudah_ada = True
                    break
                i = i + 1

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
                    user_baru = [username_baru, password_baru]
                    daftar_users.append(user_baru)

                    print("\nRegister berhasil! Silakan login.")
                    input("\nTekan Enter untuk kembali...")
                    os.system("cls" if os.name == "nt" else "clear")

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

        perjalanan_saya = []

        i = 0
        while i < len(daftar_perjalanan):
            if daftar_perjalanan[i][0] == user_login:
                perjalanan_saya.append(daftar_perjalanan[i])
            i = i + 1

        if len(perjalanan_saya) == 0:
            print("\nBelum ada perjalanan yang tercatat.")
        else:
            nomor = 1
            for perjalanan in perjalanan_saya:
                print("\nPerjalanan", nomor)
                print("-" * 40)
                print("Nama Perjalanan  :", perjalanan[1])
                print("Destinasi        :", perjalanan[2])
                print("Tanggal Pergi    :", perjalanan[3])
                print("Durasi           :", perjalanan[4])
                print("Budget           : Rp", perjalanan[5])
                print("Cerita           :", perjalanan[6])
                nomor = nomor + 1

        input("\nTekan Enter untuk kembali...")

    elif pilihan == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 60)
        print("CATAT PERJALANAN BARU")
        print("=" * 60)

        nama = input("\nNama Perjalanan         : ")

        if nama == "":
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

                    perjalanan_baru = [
                        user_login,
                        nama,
                        destinasi,
                        tanggal,
                        durasi,
                        budget,
                        cerita,
                    ]
                    daftar_perjalanan.append(perjalanan_baru)

                    print("\nPerjalanan berhasil dicatat!")
                    input("\nTekan Enter untuk kembali...")

    elif pilihan == "3":
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 60)
        print("EDIT PERJALANAN")
        print("=" * 60)

        perjalanan_saya = []

        i = 0
        while i < len(daftar_perjalanan):
            if daftar_perjalanan[i][0] == user_login:
                perjalanan_saya.append(daftar_perjalanan[i])
            i = i + 1

        if len(perjalanan_saya) == 0:
            print("\nBelum ada perjalanan yang bisa diedit.")
            input("\nTekan Enter untuk kembali...")
        else:
            print("\nDaftar Perjalanan:")
            nomor = 1
            for perjalanan in perjalanan_saya:
                print(nomor, ".", perjalanan[1], "-", perjalanan[2])
                nomor = nomor + 1

            pilih_edit = input("\nPilih nomor perjalanan yang mau diedit: ")

            if pilih_edit.isdigit() == False:
                print("\nInput harus berupa angka!")
                input("\nTekan Enter untuk kembali...")
            else:
                index_pilihan = int(pilih_edit) - 1

                if index_pilihan < 0 or index_pilihan >= len(perjalanan_saya):
                    print("\nNomor tidak valid!")
                    input("\nTekan Enter untuk kembali...")
                else:
                    perjalanan_dipilih = perjalanan_saya[index_pilihan]
                    index_asli = 0

                    i = 0
                    while i < len(daftar_perjalanan):
                        if daftar_perjalanan[i] == perjalanan_dipilih:
                            index_asli = i
                            break
                        i = i + 1

                    print(
                        "\nMasukkan data baru (tekan Enter jika tidak ingin mengubah):"
                    )

                    nama_baru = input(
                        "Nama Perjalanan [" + daftar_perjalanan[index_asli][1] + "]: "
                    )
                    if nama_baru != "":
                        daftar_perjalanan[index_asli][1] = nama_baru

                    destinasi_baru = input(
                        "Destinasi [" + daftar_perjalanan[index_asli][2] + "]: "
                    )
                    if destinasi_baru != "":
                        daftar_perjalanan[index_asli][2] = destinasi_baru

                    tanggal_baru = input(
                        "Tanggal Pergi [" + daftar_perjalanan[index_asli][3] + "]: "
                    )
                    if tanggal_baru != "":
                        daftar_perjalanan[index_asli][3] = tanggal_baru

                    durasi_baru = input(
                        "Durasi [" + daftar_perjalanan[index_asli][4] + "]: "
                    )
                    if durasi_baru != "":
                        daftar_perjalanan[index_asli][4] = durasi_baru

                    budget_baru = input(
                        "Budget [" + daftar_perjalanan[index_asli][5] + "]: "
                    )
                    if budget_baru != "":
                        if budget_baru.isdigit() == False:
                            print(
                                "\nBudget harus berupa angka! Data budget tidak diubah."
                            )
                        else:
                            daftar_perjalanan[index_asli][5] = budget_baru

                    cerita_baru = input(
                        "Cerita [" + daftar_perjalanan[index_asli][6] + "]: "
                    )
                    if cerita_baru != "":
                        daftar_perjalanan[index_asli][6] = cerita_baru

                    print("\nPerjalanan berhasil diedit!")
                    input("\nTekan Enter untuk kembali...")

    elif pilihan == "4":
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 60)
        print("HAPUS PERJALANAN")
        print("=" * 60)

        perjalanan_saya = []

        i = 0
        while i < len(daftar_perjalanan):
            if daftar_perjalanan[i][0] == user_login:
                perjalanan_saya.append(daftar_perjalanan[i])
            i = i + 1

        if len(perjalanan_saya) == 0:
            print("\nBelum ada perjalanan yang bisa dihapus.")
            input("\nTekan Enter untuk kembali...")
        else:
            print("\nDaftar Perjalanan:")
            nomor = 1
            for perjalanan in perjalanan_saya:
                print(nomor, ".", perjalanan[1], "-", perjalanan[2])
                nomor = nomor + 1

            pilih_hapus = input("\nPilih nomor perjalanan yang mau dihapus: ")

            if pilih_hapus.isdigit() == False:
                print("\nInput harus berupa angka!")
                input("\nTekan Enter untuk kembali...")
            else:
                index_pilihan = int(pilih_hapus) - 1

                if index_pilihan < 0 or index_pilihan >= len(perjalanan_saya):
                    print("\nNomor tidak valid!")
                    input("\nTekan Enter untuk kembali...")
                else:
                    perjalanan_terpilih = perjalanan_saya[index_pilihan]

                    konfirmasi = input(
                        "Yakin mau hapus '" + perjalanan_terpilih[1] + "'? (ya/tidak): "
                    )

                    if konfirmasi == "ya" or konfirmasi == "Ya" or konfirmasi == "YA":
                        daftar_perjalanan.remove(perjalanan_terpilih)
                        print("\nPerjalanan berhasil dihapus!")
                    else:
                        print("\nPenghapusan dibatalkan.")

                    input("\nTekan Enter untuk kembali...")

    elif pilihan == "5":
        konfirmasi_logout = input("\nYakin mau logout? (ya/tidak): ")

        if (
            konfirmasi_logout == "ya"
            or konfirmasi_logout == "Ya"
            or konfirmasi_logout == "YA"
        ):
            os.system("cls" if os.name == "nt" else "clear")
            print("\nLogout berhasil!")
            print("\n" + "=" * 60)
            print("Terima kasih sudah menggunakan Jurnal Perjalanan!")
            print("Sampai jumpa lagi!")
            print("=" * 60)
            break
        else:
            print("\nLogout dibatalkan.")
            input("\nTekan Enter untuk kembali...")

    else:
        print("\nPilihan tidak valid!")
        input("\nTekan Enter untuk kembali...")