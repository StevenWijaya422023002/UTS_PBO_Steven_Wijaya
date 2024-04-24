from base.user import User

class Superadmin(User):
    def __init__(self, user_id, name, email, password, super_admin_id):
        super().__init__(user_id, password)
        self.name = name
        self.email = email
        self.super_admin_id = super_admin_id

    def get_name(self):
        return self.name

    def login(self, user_id, password):
        return super().login(user_id, password)

    def tambah_fitur(self, fitur):
        print(f"Fitur '{fitur}' telah ditambahkan.")

    def maintenance_sistem(self):
        print("Sistem sedang dalam maintenance.")

    def terima_laporan_bug(self, e_ticket):
        print(f"Laporan bug diterima dari e-ticket: {e_ticket}")
        print("Superadmin akan menindaklanjuti laporan ini.")
        print("Laporan bug telah diterima dan akan segera ditinjau.")
    
    def receive_bug_report(self, e_ticket):
        print(f"Laporan bug diterima: {e_ticket}")
        print("Bug report telah diterima dan akan ditinjau.")
