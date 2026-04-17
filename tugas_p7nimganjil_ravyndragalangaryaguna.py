def pangkat(a, b):
    if b == 0:
        return 1
    else:
        return a * pangkat(a, b - 1)

def fib(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def deret(n):
    if n == 1:
        return fib(1) / fib(2)   # ← fix: pakai rumus, bukan hardcode 1
    else:
        suku = ((-1) ** (n - 1)) * (fib(2 * n - 1) / fib(2 * n))
        return deret(n - 1) + suku

while True:
    print("\nMenu:")
    print("1. A pangkat B")
    print("2. Hitung deret")
    print("0. Keluar")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        try:                                      # ← fix: tangkap input invalid
            a = int(input("Masukkan bilangan bulat: "))
            b = int(input("Masukkan pangkat: "))
        except ValueError:
            print("Input harus berupa bilangan bulat")
            continue
        if b < 0:
            print("Pangkat harus >= 0")
            continue
        hasil = pangkat(a, b)
        print(f"Hasil {a}^{b} = {hasil}")

    elif pilihan == "2":
        try:                                      # ← fix: tangkap input invalid
            n = int(input("Masukkan jumlah N: "))
        except ValueError:
            print("Input harus berupa bilangan bulat")
            continue
        if n <= 0:
            print("N harus > 0")
            continue
        hasil = deret(n)
        print("Hasil:", round(hasil, 6))

    elif pilihan == "0":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")
        