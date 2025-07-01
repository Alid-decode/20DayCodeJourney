print("=== Kalkulator Sederhana ===")

while True:
    # 1. Minta input
    angka1 = input("Masukkan angka pertama (atau 'q' untuk keluar): ")
    if angka1.lower() == "q":
        print("Terima kasih telah menggunakan kalkulator.")
        break

    operator = input("Pilih operator (+, -, *, /): ")
    angka2 = input("Masukkan angka kedua: ")

    # 2. Ubah ke float
    try:
        angka1 = float(angka1)
        angka2 = float(angka2)
    except ValueError:
        print("Error: Input harus berupa angka.")
        continue  # balik ke atas loop

    # 3. Hitung
    if operator == "+":
        hasil = angka1 + angka2
    elif operator == "-":
        hasil = angka1 - angka2
    elif operator == "*":
        hasil = angka1 * angka2
    elif operator == "/":
        if angka2 == 0:
            hasil = "Error: Tidak bisa dibagi dengan nol!"
        else:
            hasil = angka1 / angka2
    else:
        hasil = "Operator tidak dikenali."

    # 4. Tampilkan hasil
    print("Hasil:")
    if isinstance(hasil, float):
        print(f"{angka1} {operator} {angka2} = {hasil}")
    else:
        print(hasil)

    print("-" * 30)  # garis pemisah biar rapi
