class Mahasiswa:
    def __init__(self, nama, nim, username, password):
        self.nama = nama
        self.nim = nim
        self.username = username
        self.password = password
        self.jadwal_kuliah = {
            "Senin": ["Kosong"],
            "Selasa": ["Analisa & Perancangan Proses Bisnis"],
            "Rabu": ["Analisa & Perancangan SI", "Manajemen Sistem Informasi"],
            "Kamis": ["Pemrograman Berorientasi Objek"],
            "Jumat": ["Pemrograman Web Lanjutan"]
            
        }

        self.daftar_krs = []
        self.nilai = {}
        self.daftar_buku_pinjaman = []
        self.sertifikat = []


    def get_name(self): 
        return self.nama

    def lihat_jadwal_kuliah(self):
        print("Jadwal Kuliah:")
        for hari, mata_kuliah in self.jadwal_kuliah.items():
            print(f"{hari}: {', '.join(mata_kuliah)}")
    
    def login(self, nim, password):
        if nim == self.nim and password == self.password:
            print(f"Login successful as Mahasiswa {self.nama} ({self.nim})")
            return True
        else:
            print("Login failed. Incorrect NIM or password.")
        return False

    def tambah_krs(self, *mata_kuliah):  
        for mk in mata_kuliah:
            self.daftar_krs.append(mk)
            print(f"Berhasil mendaftarkan mata kuliah {mk}.")


    def tambah_nilai(self, matkul, nilai):  
        self.nilai[matkul] = nilai
        

    
    def lihat_nilai(self):
        if self.nilai:
            print("Nilai:")
            for matkul, nilai in self.nilai.items():
                print(f"{matkul}: {nilai}")
        else:
            print("Belum ada nilai.")
    
    def pinjam_buku(self, judul_buku):  
        self.daftar_buku_pinjaman.append(judul_buku)
        print(f"{self.nama}  meminjam buku dengan judul '{judul_buku}'.")


    def upload_sertifikat(self, nama_sertifikat):  
        self.sertifikat.append(nama_sertifikat)
        print(f"Sertifikat '{nama_sertifikat}' berhasil diupload.")
    
    def kirim_laporan_bug(self, e_ticket):
        print(f"Laporan bug berhasil dikirim melalui e-ticket: {e_ticket}")
    


