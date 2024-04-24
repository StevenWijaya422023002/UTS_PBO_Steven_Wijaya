class Grade:
    def __init__(self):
        self.nilai_mahasiswa = {}

    def update_nilai(self, nim, mata_kuliah, nilai):
        if nim in self.nilai_mahasiswa:
            if mata_kuliah in self.nilai_mahasiswa[nim]:
                self.nilai_mahasiswa[nim][mata_kuliah] = nilai
                print(f"Nilai untuk Mahasiswa dengan NIM {nim} pada mata kuliah {mata_kuliah} berhasil diperbarui.")
            else:
                self.nilai_mahasiswa[nim][mata_kuliah] = nilai
                print(f"Nilai untuk Mahasiswa dengan NIM {nim} pada mata kuliah {mata_kuliah} berhasil ditambahkan.")
        else:
            self.nilai_mahasiswa[nim] = {mata_kuliah: nilai}
            print(f"Nilai untuk Mahasiswa dengan NIM {nim} pada mata kuliah {mata_kuliah} berhasil ditambahkan.")


