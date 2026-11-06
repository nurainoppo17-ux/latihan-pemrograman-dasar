# ==========================================
# Program Identitas Mahasiswa
# ==========================================

# Konstanta
STATUS_KULIAH = True
BATAS_UMUR = 100

# Variabel identitas
nama = "Dela Puspita"     # String
umur = 19                      # Integer
ipk = 3.75                     # Float
status_aktif = True            # Boolean

# Perulangan dengan pilihan y/t
while True:
    print("\n===================================")
    print("       IDENTITAS MAHASISWA")
    print("===================================")

    # Menampilkan nilai dan tipe data
    print("Nama         :", nama)
    print("Tipe data    :", type(nama))

    print("Umur         :", umur)
    print("Tipe data    :", type(umur))

    print("IPK Target   :", ipk)
    print("Tipe data    :", type(ipk))

    print("Status Aktif :", status_aktif)
    print("Tipe data    :", type(status_aktif))

    # Operator dan percabangan
    print("\n=== HASIL PENGECEKAN ===")

    if umur < BATAS_UMUR:
        print("Umur masih dalam batas normal.")

    if status_aktif == STATUS_KULIAH:
        print("Status mahasiswa: Aktif.")

    # Input pilihan perulangan
    pilihan = input("\nApakah ingin menampilkan data lagi? (y/t): ")

    # Menghentikan perulangan jika memilih t
    if pilihan.lower() == "t":
        break

print("\nProgram selesai.")
