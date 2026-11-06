# ==========================================
# Program Konversi Waktu
# ==========================================

# Konstanta
DETIK_PER_MENIT = 60
DETIK_PER_JAM = 3600

# Perulangan dengan pilihan y/t
while True:

    print("\n===================================")
    print("         PROGRAM KONVERSI WAKTU")
    print("===================================")

    # Input total detik
    total_detik = int(input("Masukkan total detik: "))

    # Konversi total detik menjadi jam, menit, dan sisa detik
    jam = total_detik // DETIK_PER_JAM
    sisa_detik = total_detik % DETIK_PER_JAM

    menit = sisa_detik // DETIK_PER_MENIT
    detik = sisa_detik % DETIK_PER_MENIT

    # Menampilkan hasil
    print("\n=== HASIL KONVERSI ===")
    print(
        total_detik,
        "detik sama dengan",
        jam,
        "jam,",
        menit,
        "menit, dan",
        detik,
        "detik."
    )

    # Menampilkan tipe data
    print("\n=== TIPE DATA ===")
    print("Total detik :", type(total_detik))
    print("Jam         :", type(jam))
    print("Menit       :", type(menit))
    print("Detik       :", type(detik))

    # Input pilihan untuk mengulang
    pilihan = input("\nApakah ingin melakukan konversi lagi? (y/t): ")

    # Jika memilih t, program berhenti
    if pilihan.lower() == "t":
        break

print("\nProgram selesai.")
