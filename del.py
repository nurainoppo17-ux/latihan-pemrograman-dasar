# Program Menghitung Luas Segitiga dengan Perulangan

# Konstanta
ALAS = 20
TINGGI = 4

# Variabel perulangan
ulang = "y"

while ulang == "y":
    # Menghitung luas
    luas = 0.5 * ALAS * TINGGI

    # Output
    print("\n=== PROGRAM MENGHITUNG LUAS SEGITIGA ===")
    print("Alas   :", ALAS)
    print("Tinggi :", TINGGI)
    print("Luas   :", luas)

    # Menanyakan apakah ingin mengulang
    ulang = input("\nApakah ingin menghitung lagi? (y/n): ").lower()

print("\nProgram selesai. Terima kasih!")
