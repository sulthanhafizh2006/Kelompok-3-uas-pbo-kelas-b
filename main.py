from services.product_manager import ProductManager
from services.profit_calculator import ProfitCalculator
from utils.display import Display

def main():
    manager = ProductManager()
    calculator = ProfitCalculator()
    display = Display()

    while True:
        display.show_menu()
        choice = input("Pilih menu: ").strip()

        if choice == "1":
            manager.tambah_produk()
        elif choice == "2":
            manager.tampilkan_semua_produk()
        elif choice == "3":
            calculator.hitung_profit(manager)
        elif choice == "4":
            manager.simulasi_produksi()
        elif choice == "0":
            print("Terima kasih telah menggunakan Hanari Bakery System!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main() 