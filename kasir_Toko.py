# ==========================================
# Program Kasir Toko
# ==========================================

# Konstanta
NAMA_TOKO = "TOKO MAJU JAYA"

# List daftar barang
daftar_barang = ["Buku", "Pensil", "Penggaris"]

# Dictionary harga barang
harga_barang = {
    "Buku": 5000,
    "Pensil": 2000,
    "Penggaris": 3000
}

# Perulangan dengan pilihan y/t
while True:

    print("\n===================================")
    print("         ", NAMA_TOKO)
    print("===================================")

    # Menampilkan daftar barang
    print("Daftar Barang:")
    for barang in daftar_barang:
        print("-", barang, "Rp", harga_barang[barang])

    # Jumlah barang yang dibeli
    jumlah_buku = 2
    jumlah_pensil = 1

    # Menghitung total menggunakan operator * dan +
    total_buku = harga_barang["Buku"] * jumlah_buku
    total_pensil = harga_barang["Pensil"] * jumlah_pensil

    total_bayar = total_buku + total_pensil

    # Output hasil perhitungan
    print("\n=== STRUK BELANJA ===")
    print("Buku    :", jumlah_buku, "x Rp", harga_barang["Buku"])
    print("Pensil  :", jumlah_pensil, "x Rp", harga_barang["Pensil"])
    print("-----------------------------------")
    print("Total Bayar : Rp", total_bayar)

    # Input pilihan
    pilihan = input("\nApakah ingin menghitung lagi? (y/t): ")

    # Jika memilih t, program berhenti
    if pilihan.lower() == "t":
        break

print("\nTerima kasih telah berbelanja!")
print("Program selesai.")
