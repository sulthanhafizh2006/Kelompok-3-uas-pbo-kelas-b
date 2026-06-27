"""
roti_manis.py
Dikerjakan oleh: Aksya Nayla Fitriana (K3525047)

Class RotiManis: turunan dari BaseProduct, mengimplementasikan
ProductionInterface (baking, packaging, labeling) dan
FermentationInterface (pengembangan), karena roti manis melalui
proses fermentasi/pengembangan adonan.
"""

from base_product import BaseProduct, ProductionInterface, FermentationInterface


class RotiManis(BaseProduct, ProductionInterface, FermentationInterface):
    def __init__(self, jumlah_pcs=0):
        bahan_baku = {
            "Tepung terigu protein tinggi": "500 gram",
            "Telur": "2 butir",
            "Butter tawar": "80 gram",
            "Gula pasir": "100 gram",
            "Garam": "5 gram",
            "Ragi instan": "8 gram",
            "Susu cair": "200 ml",
        }
        super().__init__(
            nama="Roti Manis",
            kode="RT001",
            bahan_baku=bahan_baku,
            biaya_produksi=3000,   # Rp per pcs
            harga_jual=6000,       # Rp per pcs
            jumlah_pcs=jumlah_pcs,
        )

    def pengadonan(self):
        print(f"[{self.nama}] Mencampur tepung, telur, butter, gula, garam, ragi, "
              f"dan susu cair hingga kalis...")

    def pengembangan(self):
        print(f"[{self.nama}] Mendiamkan adonan selama 45-60 menit hingga mengembang "
              f"dua kali lipat...")

    def pemanggangan(self):
        print(f"[{self.nama}] Memanggang adonan pada suhu 180°C selama 15-18 menit...")

    def simulasi_produksi(self):
        """Menjalankan seluruh urutan proses produksi Roti Manis."""
        print(f"\n--- Simulasi Produksi {self.nama} ---")
        self.pengadonan()
        self.pengembangan()
        self.pemanggangan()
        self.baking()
        self.packaging()
        self.labeling()
        print(f"--- Produksi {self.nama} selesai ---\n")