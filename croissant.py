"""
croissant.py
Dikerjakan oleh: Adibah Ruhil (K3525044)

Class Croissant: turunan dari BaseProduct, mengimplementasikan
ProductionInterface (baking, packaging, labeling) dan
FermentationInterface (pengembangan), karena croissant juga melalui
proses fermentasi/pengembangan adonan berlapis (laminating dough).
"""

from base_product import BaseProduct, ProductionInterface, FermentationInterface

class Croissant(BaseProduct, ProductionInterface, FermentationInterface):
    def __init__(self, jumlah_pcs=0):
        bahan_baku = {
            "Tepung terigu protein tinggi": "500 gram",
            "Butter tawar (korsvet)": "300 gram",
            "Gula pasir": "60 gram",
            "Garam": "10 gram",
            "Ragi instan": "10 gram",
            "Susu cair dingin": "250 ml",
            "Telur (untuk olesan)": "1 butir",
        }
        super().__init__(
            nama="Croissant",
            kode="RT002",
            bahan_baku=bahan_baku,
            biaya_produksi=4500,  
            harga_jual=9000,       
            jumlah_pcs=jumlah_pcs,
        )

    def pengadonan(self):
        print(f"[{self.nama}] Membuat adonan dasar (detrempe), kemudian melapisi "
              f"adonan dengan butter (laminating) melalui proses lipat berulang...")

    def pengembangan(self):
        print(f"[{self.nama}] Mendiamkan adonan berlapis di lemari pendingin lalu "
              f"proofing pada suhu ruang hingga mengembang sebelum dipanggang...")

    def pemanggangan(self):
        print(f"[{self.nama}] Mengoles permukaan dengan telur, lalu memanggang pada "
              f"suhu 200°C selama 18-20 menit hingga berlapis renyah keemasan...")

    def simulasi_produksi(self):
        """Menjalankan seluruh urutan proses produksi Croissant."""
        print(f"\n--- Simulasi Produksi {self.nama} ---")
        self.pengadonan()
        self.pengembangan()
        self.pemanggangan()
        self.baking()
        self.packaging()
        self.labeling()
        print(f"--- Produksi {self.nama} selesai ---\n")