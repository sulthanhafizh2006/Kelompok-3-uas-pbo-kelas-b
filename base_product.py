"""
base_product.py
Dikerjakan oleh: Zahra Faizza Kuncoroningrum (K3525017)

File ini berisi:
- BaseProduct      -> abstract superclass untuk seluruh produk Hanari Bakery
- ProductionInterface   -> kontrak wajib (baking, packaging, labeling)
- FermentationInterface -> kontrak khusus untuk produk yang mengembang
- ToppingInterface      -> kontrak khusus untuk produk yang ada proses topping
"""

from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Abstract superclass untuk semua jenis produk roti Hanari Bakery."""

    def __init__(self, nama, kode, bahan_baku, biaya_produksi, harga_jual, jumlah_pcs=0):
        self.nama = nama
        self.kode = kode
        self.bahan_baku = bahan_baku          # dict -> {nama_bahan: jumlah}
        self.biaya_produksi = biaya_produksi  # float, biaya produksi per resep (per-n pcs)
        self.harga_jual = harga_jual          # float, harga jual per resep (per-n pcs)
        self.jumlah_pcs = jumlah_pcs          # int, jumlah pcs yang ingin diproduksi

    def tampilkan_info(self):
        """Menampilkan informasi detail spesifikasi produk."""
        print(f"\n=== {self.nama} ({self.kode}) ===")
        print("Bahan baku:")
        for bahan, jumlah in self.bahan_baku.items():
            print(f"  - {bahan}: {jumlah}")
        print(f"Biaya produksi (per resep): Rp{self.biaya_produksi:,.0f}")
        print(f"Harga jual (per resep)    : Rp{self.harga_jual:,.0f}")

    def hitung_profit(self, jumlah_pcs):
        """
        Menghitung estimasi profit berdasarkan jumlah pcs yang akan diproduksi.
        Asumsi: biaya_produksi dan harga_jual yang disimpan adalah nilai per pcs.
        """
        profit = (self.harga_jual - self.biaya_produksi) * jumlah_pcs
        return profit

    @abstractmethod
    def pengadonan(self):
        """Prosedur pengadonan, wajib di-override oleh setiap subclass."""
        pass

    @abstractmethod
    def pemanggangan(self):
        """Prosedur pemanggangan, wajib di-override oleh setiap subclass."""
        pass


class ProductionInterface:
    """
    Interface/mixin untuk proses standar wajib yang harus dimiliki
    semua produk: baking, packaging, dan labeling.
    """

    def baking(self):
        print(f"[{self.nama}] Menjalankan simulasi proses pembakaran (baking)...")

    def packaging(self):
        print(f"[{self.nama}] Mengemas produk ke dalam kemasan (packaging)...")

    def labeling(self):
        print(f"[{self.nama}] Menempelkan label merek Hanari Bakery (labeling)...")


class FermentationInterface(ABC):
    """
    Interface khusus untuk proses pengembangan adonan.
    Hanya diimplementasikan oleh produk yang mengembang:
    RotiManis, Croissant, dan Muffin.
    """

    @abstractmethod
    def pengembangan(self):
        pass


class ToppingInterface(ABC):
    """
    Interface khusus untuk proses pemberian topping.
    Hanya diimplementasikan oleh produk roti kering:
    ButterCookies dan Muffin.
    """

    @abstractmethod
    def topping(self):
        pass