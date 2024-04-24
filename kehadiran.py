class Kehadiran:
    def __init__(self):
        self.data_kehadiran = {}

    def absen(self, mahasiswa):
        if mahasiswa.nim in self.data_kehadiran:
            print(f"{mahasiswa.nama} sudah absen.")
        else:
            self.data_kehadiran[mahasiswa.nim] = mahasiswa.nama
            print(f"{mahasiswa.nama} berhasil diabsen.")

    def tambah_kehadiran(self, mahasiswa):
        self.data_kehadiran[mahasiswa.nim] = mahasiswa.nama
