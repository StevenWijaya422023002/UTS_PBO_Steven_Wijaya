from grade import Grade
from mahasiswa import Mahasiswa
from kehadiran import Kehadiran

class Dosen:
    def __init__(self, nama, nip):
        self.nama = nama
        self.nip = nip
        self.mata_pelajaran = {}
        self.nilai = {}
        self.grade = Grade()
        self.kehadiran = Kehadiran()
        self.daftar_absen = set()  

    def login(self, nip, password):
        if nip == self.nip and password == "default_password":
            print(f"Login successful as Dosen {self.nama} ({self.nip})")
            return True
        else:
            print("Login failed. Incorrect NIP or password.")
            return False
    
    def absen_mahasiswa(self, mahasiswa):
        print(f"Dosen {self.nama} telah mengabsen mahasiswa {mahasiswa.get_name()} ({mahasiswa.nim})")
        self.kehadiran.tambah_kehadiran(mahasiswa)
        self.daftar_absen.add(mahasiswa.get_name())  
    
    def lihat_daftar_absen(self):
        print("Daftar Mahasiswa yang Sudah Diabsen:")
        for nama in self.daftar_absen:
            print(nama)


    def upload_nilai(self, nim, pelajaran, nilai):
        self.grade.update_nilai(nim, pelajaran, nilai)

    def update_pelajaran(self, matkul):
        self.mata_pelajaran[matkul] = True
        print(f"Mata pelajaran {matkul} ditambahkan ke jadwal mengajar Dosen {self.nama}.")


    def update_jadwal(self, matkul, jadwal_baru):
        if matkul in self.mata_pelajaran:
            print(f"Jadwal for {matkul} updated to {jadwal_baru}.")
        else:
            print(f"{matkul} is not taught by this lecturer.")
