import csv
import os

# Simulasi database akun
database = {
    "pemilik_toko": {"username": "pemilik", "password": "pemilik123"},
    "penjual": {"username": "penjual", "password": "penjual123"}
}

# Fungsi login
def login():
    print("=== LOGIN ===")
    print("1. Pemilik Toko")
    print("2. Penjual")
    
    try:
        role = int(input("Pilih peran (1 atau 2): "))
        if role == 1:
            account_type = "pemilik_toko"
        elif role == 2:
            account_type = "penjual"
        else:
            print("Pilihan tidak valid.")
            return

        username = input("Masukkan Nama Pengguna: ")
        password = input("Masukkan Kata Sandi: ")

        # Validasi username dan password sesuai role
        if (
            username == database[account_type]["username"]
            and password == database[account_type]["password"]
        ):
            print(f"Login Berhasil! Selamat datang, {account_type}.")
        else:
            print("Login Gagal! Nama pengguna atau kata sandi salah.")
    except ValueError:
        print("Masukkan pilihan yang valid!")

# Memanggil fungsi login
if __name__ == "__main__":
    login()

