"""
main.py
Dikerjakan oleh: Sulthan Hafizh Putra Agung (K3525013)

Program utama Sistem Informasi Produksi dan Manajemen Produk
Hanari Bakery. Berisi menu:
  1. Tambah Produk Baru
  2. Tampilkan Semua Produk
  3. Kalkulator Estimasi Profit
  4. Simulasi Proses Produksi
  5. Keluar
"""

from roti_manis import RotiManis
from croissant import Croissant
from butter_cookies import ButterCookies
from muffin import Muffin

daftar_produk = []

JENIS_PRODUK = {
    "1": ("Roti Manis", RotiManis),
    "2": ("Croissant", Croissant),
    "3": ("Butter Cookies", ButterCookies),
    "4": ("Muffin", Muffin),
}

def tampilkan_menu_jenis():
    print("\nPilih jenis roti:")
    for kode, (nama, _) in JENIS_PRODUK.items():
        print(f"  {kode}. {nama}")

def input_jumlah_pcs(prompt="Masukkan jumlah pcs: "):
    while True:
        try:
            nilai = int(input(prompt))
            if nilai <= 0:
                print("Jumlah pcs harus lebih dari 0.")
                continue
            return nilai
        except ValueError:
            print("Input tidak valid, masukkan angka.")

def tambah_produk_baru():
    tampilkan_menu_jenis()
    pilihan = input("Pilihan: ").strip()

    if pilihan not in JENIS_PRODUK:
        print("Pilihan tidak valid.")
        return

    nama_jenis, kelas_produk = JENIS_PRODUK[pilihan]
    jumlah_pcs = input_jumlah_pcs("Masukkan jumlah pcs yang akan diproduksi: ")

    produk = kelas_produk(jumlah_pcs=jumlah_pcs)
    daftar_produk.append(produk)
    print(f"\nProduk '{nama_jenis}' berhasil ditambahkan dengan jumlah produksi "
          f"{jumlah_pcs} pcs.")

def tampilkan_semua_produk():
    if not daftar_produk:
        print("\nBelum ada produk yang ditambahkan.")
        return

    print("\n=== Daftar Seluruh Produk Hanari Bakery ===")
    for produk in daftar_produk:
        produk.tampilkan_info()
        print(f"Jumlah pcs diproduksi: {produk.jumlah_pcs}")

def kalkulator_profit():
    if not daftar_produk:
        print("\nBelum ada produk yang dapat dihitung profitnya.")
        return

    print("\nPilih produk yang akan dihitung estimasi profitnya:")
    for i, produk in enumerate(daftar_produk, start=1):
        print(f"  {i}. {produk.nama} ({produk.kode})")

    try:
        index = int(input("Pilihan nomor produk: ")) - 1
        if index < 0 or index >= len(daftar_produk):
            print("Pilihan tidak valid.")
            return
    except ValueError:
        print("Input tidak valid.")
        return

    produk = daftar_produk[index]
    jumlah_pcs = input_jumlah_pcs("Masukkan jumlah pcs yang akan diproduksi: ")
    profit = produk.hitung_profit(jumlah_pcs)
    print(f"\nEstimasi profit untuk {jumlah_pcs} pcs {produk.nama}: Rp{profit:,.0f}")


def simulasi_proses_produksi():
    if not daftar_produk:
        print("\nBelum ada produk yang dapat disimulasikan.")
        return

    print("\nPilih produk yang akan disimulasikan proses produksinya:")
    for i, produk in enumerate(daftar_produk, start=1):
        print(f"  {i}. {produk.nama} ({produk.kode})")

    try:
        index = int(input("Pilihan nomor produk: ")) - 1
        if index < 0 or index >= len(daftar_produk):
            print("Pilihan tidak valid.")
            return
    except ValueError:
        print("Input tidak valid.")
        return

    produk = daftar_produk[index]
    produk.simulasi_produksi()


def tampilkan_menu_utama():
    print("\n========================================")
    print("   HANARI BAKERY - SISTEM INFORMASI")
    print("       PRODUKSI & MANAJEMEN PRODUK")
    print("========================================")
    print("1. Tambah Produk Baru")
    print("2. Tampilkan Semua Produk")
    print("3. Kalkulator Estimasi Profit")
    print("4. Simulasi Proses Produksi")
    print("5. Keluar")


def main():
    while True:
        tampilkan_menu_utama()
        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            tambah_produk_baru()
        elif pilihan == "2":
            tampilkan_semua_produk()
        elif pilihan == "3":
            kalkulator_profit()
        elif pilihan == "4":
            simulasi_proses_produksi()
        elif pilihan == "5":
            print("\nTerima kasih telah menggunakan Sistem Informasi Hanari Bakery!")
            break
        else:
            print("\nPilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()