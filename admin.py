from mahasiswa import Mahasiswa



class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if username == self.username and password == self.password:
            print("Login successful as  Admin.")
            return True
        else:
            print("Login gagal. Username atau password salah.")
            return False

    def informasi_biaya_kuliah(self, mahasiswa, biaya):
        print(f"Biaya tagihan untuk Mahasiswa {mahasiswa.nama} ({mahasiswa.nim}): IDR{biaya}")



