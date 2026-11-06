# Program Menghitung Luas Segitiga

# Konstanta
ALAS = 20
TINGGI = 4
SETENGAH = 0.5

# Perulangan
while True:
    # Output
    print("\n=== PROGRAM LUAS SEGITIGA ===")
    print("Alas   :", ALAS)
    print("Tinggi :", TINGGI)

    # Proses perhitungan menggunakan operator
    luas = SETENGAH * ALAS * TINGGI

    # Output hasil
    print("Luas segitiga =", luas)

    # Input
    pilihan = input("Apakah ingin menghitung lagi? (y/t): ")

    # Percabangan
    if pilihan.lower() != "y":
        break

print("\nProgram selesai.")
