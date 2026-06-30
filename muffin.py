"""
muffin.py
Dikerjakan oleh: Faris Rafiuddin Hannan (K3525058)

Class Muffin: turunan dari BaseProduct, mengimplementasikan
ProductionInterface (baking, packaging, labeling),
FermentationInterface (pengembangan, karena muffin menggunakan
baking powder sebagai bahan pengembang), dan ToppingInterface
(topping choco chip).
"""

from base_product import (
    BaseProduct,
    ProductionInterface,
    FermentationInterface,
    ToppingInterface,
)

class Muffin(BaseProduct, ProductionInterface, FermentationInterface, ToppingInterface):
    def __init__(self, jumlah_pcs=0):
        bahan_baku = {
            "Tepung terigu": "300 gram",
            "Gula pasir": "150 gram",
            "Telur": "2 butir",
            "Minyak sayur": "120 ml",
            "Susu cair": "180 ml",
            "Baking powder": "8 gram",
            "Garam": "3 gram",
            "Choco chip": "100 gram",
        }
        super().__init__(
            nama="Muffin",
            kode="RT004",
            bahan_baku=bahan_baku,
            biaya_produksi=2500,   
            harga_jual=5500,       
            jumlah_pcs=jumlah_pcs,
        )

    def pengadonan(self):
        print(f"[{self.nama}] Mencampur tepung, gula, telur, minyak sayur, susu cair, "
              f"baking powder, dan garam hingga merata, lalu menuang ke cup muffin...")

    def pengembangan(self):
        print(f"[{self.nama}] Baking powder bereaksi membentuk gas yang membuat "
              f"adonan mengembang secara alami selama proses pemanggangan...")

    def topping(self):
        print(f"[{self.nama}] Menaburkan choco chip di atas permukaan adonan "
              f"sebagai topping sebelum dipanggang...")

    def pemanggangan(self):
        print(f"[{self.nama}] Memanggang pada suhu 175°C selama 20-22 menit hingga "
              f"matang dan bagian atas merekah...")

    def simulasi_produksi(self):
        """Menjalankan seluruh urutan proses produksi Muffin."""
        print(f"\n--- Simulasi Produksi {self.nama} ---")
        self.pengadonan()
        self.pengembangan()
        self.topping()
        self.pemanggangan()
        self.baking()
        self.packaging()
        self.labeling()
        print(f"--- Produksi {self.nama} selesai ---\n")
