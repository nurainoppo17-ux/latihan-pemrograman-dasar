# ==========================================
# Program Gaji Karyawan
# ==========================================

# Konstanta
PERSEN_BPJS = 100

# Perulangan dengan pilihan y/t
while True:

    print("\n===================================")
    print("        PROGRAM GAJI KARYAWAN")
    print("===================================")

    # Variabel awal
    gaji_pokok = 3000000
    tunjangan_makan = 500000
    potongan_bpjs = 2.5

    # Menghitung gaji kotor
    gaji_kotor = gaji_pokok + tunjangan_makan

    # Menghitung nominal potongan BPJS
    nominal_potongan = gaji_kotor * potongan_bpjs / PERSEN_BPJS

    # Menghitung gaji bersih
    gaji_bersih = gaji_kotor - nominal_potongan

    # Menampilkan rincian gaji
    print("Gaji Pokok          : Rp", gaji_pokok)
    print("Tunjangan Makan     : Rp", tunjangan_makan)
    print("Gaji Kotor          : Rp", gaji_kotor)
    print("Potongan BPJS       :", potongan_bpjs, "%")
    print("Nominal Potongan    : Rp", nominal_potongan)
    print("Gaji Bersih         : Rp", gaji_bersih)

    # Menampilkan tipe data gaji_bersih
    print("\nTipe data gaji_bersih:", type(gaji_bersih))

    # Input pilihan perulangan
    pilihan = input("\nApakah ingin menghitung gaji lagi? (y/t): ")

    # Jika memilih t, program berhenti
    if pilihan.lower() == "t":
        break

print("\nProgram selesai.")
