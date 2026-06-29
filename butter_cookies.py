"""
butter_cookies.py
Dikerjakan oleh: Allicya Nailah Fairuza (K3525048)

Class ButterCookies: turunan dari BaseProduct, mengimplementasikan
ProductionInterface (baking, packaging, labeling) dan
ToppingInterface (topping). Butter cookies tidak mengembang (tidak
menggunakan ragi), sehingga TIDAK mengimplementasikan
FermentationInterface.
"""

from base_product import BaseProduct, ProductionInterface, ToppingInterface


class ButterCookies(BaseProduct, ProductionInterface, ToppingInterface):
    def __init__(self, jumlah_pcs=0):
        bahan_baku = {
            "Tepung terigu": "300 gram",
            "Butter tawar": "200 gram",
            "Gula halus": "100 gram",
            "Kuning telur": "2 butir",
            "Vanila ekstrak": "1 sdt",
            "Garam": "2 gram",
        }
        super().__init__(
            nama="Butter Cookies",
            kode="RT003",
            bahan_baku=bahan_baku,
            biaya_produksi=1500,   # Rp per pcs
            harga_jual=3500,       # Rp per pcs
            jumlah_pcs=jumlah_pcs,
        )

    def pengadonan(self):
        print(f"[{self.nama}] Mengocok butter dan gula halus hingga lembut, lalu "
              f"menambahkan kuning telur, vanila, dan tepung terigu hingga tercampur rata...")

    def topping(self):
        print(f"[{self.nama}] Mencetak adonan menggunakan piping bag membentuk "
              f"pola khas butter cookies sebagai sentuhan akhir sebelum dipanggang...")

    def pemanggangan(self):
        print(f"[{self.nama}] Memanggang pada suhu 150°C selama 20-25 menit hingga "
              f"matang dan berwarna kuning keemasan di bagian pinggir...")

    def simulasi_produksi(self):
        """Menjalankan seluruh urutan proses produksi Butter Cookies."""
        print(f"\n--- Simulasi Produksi {self.nama} ---")
        self.pengadonan()
        self.topping()
        self.pemanggangan()
        self.baking()
        self.packaging()
        self.labeling()
        print(f"--- Produksi {self.nama} selesai ---\n")
