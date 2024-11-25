import csv
import os

# Fungsi utama untuk login
def main():
    file_path = "akun.csv"

    # Fungsi untuk memastikan file CSV ada
    def ensure_csv_exists():
        if not os.path.exists(file_path):
            with open(file_path, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["role", "username", "password"])
                writer.writerow(["pemilik_toko", "pemilik", "pemilik123"])
                writer.writerow(["penjual", "penjual", "penjual123"])
            print(f"File '{file_path}' berhasil dibuat dengan akun default.")

    # Fungsi untuk membaca data akun dari file CSV
    def load_accounts():
        accounts = []
        try:
            with open(file_path, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    accounts.append(row)
        except FileNotFoundError:
            print("File akun.csv tidak ditemukan! Pastikan file ada di folder yang sama.")
        return accounts

    # Pastikan file CSV ada sebelum memulai
    ensure_csv_exists()

    # Baca data akun dari CSV
    accounts = load_accounts()

    print("=== LOGIN ===")
    print("1. Pemilik Toko")
    print("2. Penjual")

    try:
        role_choice = int(input("Pilih peran (1 atau 2): "))
        if role_choice == 1:
            role = "pemilik_toko"
        elif role_choice == 2:
            role = "penjual"
        else:
            print("Pilihan tidak valid.")
            return

        username = input("Masukkan Nama Pengguna: ")
        password = input("Masukkan Kata Sandi: ")

        # Validasi login
        for account in accounts:
            if account["role"] == role and account["username"] == username and account["password"] == password:
                print(f"Login Berhasil! Selamat datang, {role}.")
                return

        print("Login Gagal! Nama pengguna atau kata sandi salah.")
    except ValueError:
        print("Masukkan pilihan yang valid!")

# Jalankan program utama
if __name__ == "__main__":
    main()
