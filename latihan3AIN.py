# Meminta masukan dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Menentukan angka maksimal
if angka1 > angka2:
    maksimal = angka1
else:
    maksimal = angka2

# Menampilkan hasil
print(f"Angka maksimal adalah: {maksimal}")

import math

# Menampilkan menu pilihan
print("=== MENU LINGKARAN ===")
print("1. Hitung Keliling Lingkaran")
print("2. Hitung Luas Lingkaran")
pilihan = input("Masukkan pilihan Anda (1 atau 2): ")

# Meminta masukan jari-jari
jari_jari = float(input("Masukkan nilai jari-jari (r): "))

# Proses percabangan berdasarkan pilihan
if pilihan == "1":
    # Rumus Keliling = 2 * pi * r
    keliling = 2 * math.pi * jari_jari
    print(f"Keliling lingkaran dengan jari-jari {jari_jari} adalah: {keliling:.2f}")
elif pilihan == "2":
    # Rumus Luas = pi * r^2
    luas = math.pi * (jari_jari ** 2)
    print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah: {luas:.2f}")
else:
    print("Pilihan tidak valid! Silakan jalankan ulang dan pilih antara 1 atau 2.")
