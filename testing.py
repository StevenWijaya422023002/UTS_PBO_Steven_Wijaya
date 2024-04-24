from mahasiswa import Mahasiswa
from dosen import Dosen
from admin import Admin
from superadmin import Superadmin
from library import Library
from kehadiran import Kehadiran


def main():
    mahasiswa1 = Mahasiswa("Steven Wijaya", "422023002", "steven_wijaya", "default_password")
    login_success = mahasiswa1.login("422023002", "default_password")
    
    dosen1 = Dosen("Hendrik", "987654321")
    login_success = dosen1.login("987654321", "default_password")
    
    admin1 = Admin("admin", "admin_password")  
    login_success = admin1.login("admin", "admin_password")

    superadmin_user = Superadmin("SA1", "Tubagus", "tubagus.marzuqi@ukrida.ac.id", "supad1", "s111")  
    login_success = superadmin_user.login("SA1", "supad1")
    if login_success:
        print("Login successful as Superadmin.")

    print("\n")

    mahasiswa1.lihat_jadwal_kuliah()

    print("\n")

    print(f"Mahasiswa dengan nama  {mahasiswa1.get_name()} berhasil")
    mahasiswa1.tambah_krs(" Analisa & Perancangan SI", "Manajemen Sistem Informasi", "Pemrograman Berorientasi Objek", "Pemrograman Web Lanjutan", "Analisa & Perancangan Proses Bisnis")

    print("\n")

    bug_report = "Bug pada halaman login."
    mahasiswa1.kirim_laporan_bug("E-ticket: Bug pada halaman login")

    print("\n")

    mahasiswa1.tambah_nilai("Analisa & Perancangan SI", 85)
    mahasiswa1.tambah_nilai("Manajemen Sistem Informasi", 78)
    mahasiswa1.tambah_nilai("Pemrograman Berorientasi Objek", 70)

    mahasiswa1.lihat_nilai()

   

    print("\n")

    mahasiswa1.pinjam_buku("Learning JavaScript Design Patterns")

    print("\n")

    mahasiswa1.upload_sertifikat("Sertifikat PSMB universitas")  
    mahasiswa1.upload_sertifikat("Sertifikat LKMM tingkat 1")  

    print("Daftar sertifikat yang diupload oleh Mahasiswa:")
    for sertifikat in mahasiswa1.sertifikat:
            print(sertifikat)

    print("\n")

    

    dosen1.upload_nilai("422023002", "Analisa & Perancangan SI", 85)
    dosen1.upload_nilai("422023011", "Manajemen Sistem Informasi", 78)
    dosen1.upload_nilai("422023013", "Pemrograman Berorientasi Objek", 70)

    

    print("\n")

    dosen1.update_pelajaran("Pemrograman Berorientasi Objek")

    print("\n")
    dosen1.update_jadwal("Pemrograman Berorientasi Objek", "Kamis 11:00 - 13:00")

    print("\n")

    dosen1.absen_mahasiswa(mahasiswa1)
    dosen1.lihat_daftar_absen()
    
    
    print("\n")
    print("admin")
    biaya_tagihan = 5000000  
    admin1.informasi_biaya_kuliah(mahasiswa1, biaya_tagihan)

    print("\n")
    print("super admin")
    superadmin_user.tambah_fitur("Dashboard baru")
    superadmin_user.maintenance_sistem()
    e_ticket = "E-ticket: Bug pada halaman login"
    superadmin_user.terima_laporan_bug(e_ticket)
    


    print("\n")

    library = Library()

    library.add_book("Python Programing", "Thomas H. Cormen")
    library.add_book("Python Crash Course", "Eric Matthes")

 
    library.books[0].borrow("Steven Wijaya")
    library.books[1].borrow("Alice")
    
    
    search_keyword = "Python"
    found_books = library.search_book(search_keyword)
    print(f"Search results for '{search_keyword}':")
    for book in found_books:
        print(f"- {book.title} by {book.author}")


    

    
    library.view_returned_borrowers()

    print("\n")
    print("Daftar Buku yang Bisa Dipinjam:")
    library.view_available_books()
   



    

if __name__ == "__main__":
    main()
