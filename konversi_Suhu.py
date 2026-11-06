# ==========================================
# Program Konversi Suhu
# ==========================================

# Konstanta
NILAI_KELVIN = 273.15
NILAI_FAHRENHEIT = 9 / 5
NILAI_REAMUR = 4 / 5

# Perulangan dengan pilihan y/t
while True:

    print("\n===================================")
    print("        PROGRAM KONVERSI SUHU")
    print("===================================")

    # Input suhu Celsius
    celsius = float(input("Masukkan suhu dalam Celsius: "))

    # Proses konversi
    fahrenheit = NILAI_FAHRENHEIT * celsius + 32
    reamur = NILAI_REAMUR * celsius
    kelvin = celsius + NILAI_KELVIN

    # Menampilkan hasil konversi
    print("\n=== HASIL KONVERSI ===")

    print("Celsius    :", celsius)
    print("Tipe data  :", type(celsius))

    print("Fahrenheit :", fahrenheit)
    print("Tipe data  :", type(fahrenheit))

    print("Reamur     :", reamur)
    print("Tipe data  :", type(reamur))

    print("Kelvin     :", kelvin)
    print("Tipe data  :", type(kelvin))

    # Input pilihan untuk mengulang
    pilihan = input("\nApakah ingin melakukan konversi lagi? (y/t): ")

    # Jika memilih t, perulangan berhenti
    if pilihan.lower() == "t":
        break

print("\nProgram selesai.")
