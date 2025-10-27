
# while True: 
#     try :
#         angka = int(input('Masukkan Angka : '))
#     except ValueError:
#         print('angka tidak boleh string')
#     else :
#         print(f'angkamu adalah :{angka}')
#     finally:
#         print('Selesai')

# while True: 
#         try :
#             umur = int(input('Masukkan umur : '))
#             if umur >=0:
#                raise ValueError('umur tidak boleh kurang dari 0')
#         except ValueError as e:
#              print(e)

try :
    nama = input('Masukkan nama : ')
    if nama == "" or nama == " ":
        raise ValueError('nama tidak boleh kosong')
except ValueError as e :
    print(e)