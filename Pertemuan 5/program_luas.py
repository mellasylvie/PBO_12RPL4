while True:
    print("======= Menghitung Luas Bangun Datar =======")
    print("Daftar pilihan" + "\n" +
      "1. Luas Persegi" + "\n" +
      "2. Luas Segitiga" + "\n" +
      "3. Exit")
 
    opsi = int(input("Pilih opsi :"))
    print("\n")

    if opsi == 1 :
        print("=== Menghitung luas persegi ===")
        sisi = int(input("Masukkan panjang sisi :"))
        luas_persegi = sisi * sisi
        print("Luas Persegi =", luas_persegi)

    elif opsi == 2 :
        print("=== Menghitung luas segitiga ===")
        a = int(input("Masukkan panjang alas :"))
        t = int(input("Masukkan tinggi :"))
        luas_segitiga = 0.5 * a * t
        print("Luas segitiga =", luas_segitiga)
 
    elif opsi == 3 :
        break
    
    else :
        print("Pilihan opsi tidak sesuai")