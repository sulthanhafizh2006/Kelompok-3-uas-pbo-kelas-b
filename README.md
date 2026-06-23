<div align="center">

```
██╗  ██╗ █████╗ ███╗   ██╗ █████╗ ██████╗ ██╗
██║  ██║██╔══██╗████╗  ██║██╔══██╗██╔══██╗██║
███████║███████║██╔██╗ ██║███████║██████╔╝██║
██╔══██║██╔══██║██║╚██╗██║██╔══██║██╔══██╗██║
██║  ██║██║  ██║██║ ╚████║██║  ██║██║  ██║██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝
       B A K E R Y  ·  S Y S T E M
```

**Sistem Informasi Produksi & Manajemen Produk Bakery**

*Proyek Akhir Mata Kuliah Pemrograman Berorientasi Objek*

---

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Paradigma-OOP-F7B731?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-2ECC71?style=for-the-badge)
![License](https://img.shields.io/badge/License-Academic-9B59B6?style=for-the-badge)

</div>

---

## 🥐 Tentang Proyek

**Hanari Bakery System** adalah aplikasi manajemen produksi berbasis Python yang dirancang untuk membantu toko roti **Hanari Bakery** mengelola produk, bahan baku, estimasi profit, dan simulasi proses produksi secara digital.

Proyek ini dikembangkan menggunakan konsep **Object-Oriented Programming (OOP)** dengan menerapkan:
- 🔷 **Abstraction** — Kelas induk abstrak untuk standarisasi produk
- 🔶 **Inheritance** — Setiap produk mewarisi properti dari base class
- 🔹 **Interface** — Standarisasi proses `baking`, `packaging`, dan `labeling`
- 🔸 **Encapsulation** — Data produk terlindungi dalam masing-masing kelas

---

## 🍞 Produk yang Dikelola

| Produk | Kode | Proses Khusus |
|--------|------|---------------|
| 🍞 Roti Manis | `RM-001` | Pengadonan → Pengembangan → Pemanggangan |
| 🥐 Croissant | `CR-001` | Pengadonan → Pengembangan (laminasi) → Pemanggangan |
| 🍪 Butter Cookies | `BC-001` | Pengadonan → Topping → Pemanggangan |
| 🧁 Muffin | `MF-001` | Pengadonan → Pengembangan → Topping → Pemanggangan |

---

## ✨ Fitur Utama

```
┌─────────────────────────────────────────────┐
│         HANARI BAKERY MANAGEMENT             │
├─────────────────────────────────────────────┤
│  1.  Tambah Produk Baru                     │
│  2.  Tampilkan Semua Produk                 │
│  3.  Kalkulator Estimasi Profit             │
│  4.  Simulasi Proses Produksi               │
│  0.  Keluar                                 │
└─────────────────────────────────────────────┘
```

- **📦 Manajemen Produk** — Tambah dan tampilkan produk beserta detail bahan baku
- **💰 Kalkulator Profit** — Estimasi keuntungan berdasarkan jumlah pcs yang diproduksi
- **⚙️ Simulasi Produksi** — Jalankan tahapan produksi secara berurutan per produk

---

## 🗂️ Struktur Proyek

```
HanariBakery/
│
├── 📄 main.py                          # Entry point & menu utama
│
├── 📁 interfaces/
│   └── production_interface.py         # Abstract interface (baking, packaging, labeling)
│
├── 📁 models/
│   ├── base_product.py                 # Abstract base class semua produk
│   ├── roti_manis.py                   # Kelas Roti Manis
│   ├── croissant.py                    # Kelas Croissant
│   ├── butter_cookies.py               # Kelas Butter Cookies
│   └── muffin.py                       # Kelas Muffin
│
├── 📁 services/
│   ├── product_manager.py              # Manajemen & penyimpanan produk
│   └── profit_calculator.py            # Logika kalkulasi profit
│
├── 📁 utils/
│   └── display.py                      # Helper tampilan menu CLI
│
├── 📁 docs/
│   └── class_diagram.png               # Diagram UML (Draw.io)
│
└── 📄 README.md
```

---

## 🧱 Arsitektur OOP

```
          «interface»
       ProductionInterface
      ┌───────────────────┐
      │ + baking()        │
      │ + packaging()     │
      │ + labeling()      │
      └────────┬──────────┘
               │ implements
      ┌────────▼──────────┐
      │   BaseProduct     │  ← Abstract Class
      │ ─────────────── │
      │ # nama           │
      │ # kode           │
      │ # bahan_baku     │
      │ # biaya_produksi │
      │ # harga_jual     │
      │ # jumlah_pcs     │
      │ ─────────────── │
      │ + tampilkan_info()│
      │ + packaging()    │
      │ + labeling()     │
      └──┬──────┬──┬──┬──┘
         │      │  │  │
    ┌────▼─┐ ┌──▼─┐ ┌▼──────────┐ ┌──▼───┐
    │Roti  │ │Croi│ │  Butter   │ │Muffin│
    │Manis │ │ssnt│ │  Cookies  │ │      │
    └──────┘ └────┘ └───────────┘ └──────┘
```

---

## 🚀 Cara Menjalankan

### Prasyarat
- Python **3.10** atau lebih baru
- Tidak memerlukan library eksternal

### Instalasi & Menjalankan

```bash
# 1. Clone repository ini
git clone https://github.com/username/HanariBakery.git

# 2. Masuk ke direktori proyek
cd HanariBakery

# 3. Jalankan program
python main.py
```

### Contoh Output Kalkulator Profit

```
== Kalkulator Estimasi Profit ==
Produk          : Croissant
Jumlah Produksi : 30 pcs
Total Biaya     : Rp 125.000
Total Pendapatan: Rp 225.000
Estimasi Profit : Rp 100.000
```

---

## 👥 Tim Pengembang

<div align="center">

<table>
  <tr>
    <td align="center" width="300">
      <img src="https://img.shields.io/badge/01-Anggota-F7B731?style=for-the-badge" /><br><br>
      <b>🧑‍💻 Sulthan Hafizh Putra Agung</b><br>
      <sub>NIM: K3525013</sub><br><br>
      <img src="https://img.shields.io/badge/File-main.py-3776AB?style=flat-square&logo=python" /><br>
      <sub>Menu utama, routing antar fitur, dan entry point program</sub>
    </td>
    <td align="center" width="300">
      <img src="https://img.shields.io/badge/02-Anggota-E74C3C?style=for-the-badge" /><br><br>
      <b>🧑‍💻 [Nama Anggota 2]</b><br>
      <sub>NIM: [XXXXXXXXXX]</sub><br><br>
      <img src="https://img.shields.io/badge/File-interfaces%20%26%20base__product-E74C3C?style=flat-square" /><br>
      <sub>Abstract interface & base class sebagai fondasi arsitektur OOP</sub>
    </td>
    <td align="center" width="300">
      <img src="https://img.shields.io/badge/03-Anggota-2ECC71?style=for-the-badge" /><br><br>
      <b>🧑‍💻 [Nama Anggota 3]</b><br>
      <sub>NIM: [XXXXXXXXXX]</sub><br><br>
      <img src="https://img.shields.io/badge/File-roti__manis%20%26%20croissant-2ECC71?style=flat-square" /><br>
      <sub>Implementasi produk Roti Manis dan Croissant beserta proses produksinya</sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="300">
      <img src="https://img.shields.io/badge/04-Anggota-9B59B6?style=for-the-badge" /><br><br>
      <b>🧑‍💻 [Nama Anggota 4]</b><br>
      <sub>NIM: [XXXXXXXXXX]</sub><br><br>
      <img src="https://img.shields.io/badge/File-butter__cookies%20%26%20muffin-9B59B6?style=flat-square" /><br>
      <sub>Implementasi produk Butter Cookies dan Muffin beserta proses produksinya</sub>
    </td>
    <td align="center" width="300">
      <img src="https://img.shields.io/badge/05-Anggota-1ABC9C?style=for-the-badge" /><br><br>
      <b>🧑‍💻 [Nama Anggota 5]</b><br>
      <sub>NIM: [XXXXXXXXXX]</sub><br><br>
      <img src="https://img.shields.io/badge/File-services%2F-1ABC9C?style=flat-square" /><br>
      <sub>Logika bisnis: manajemen produk & kalkulator estimasi profit</sub>
    </td>
    <td align="center" width="300">
      <img src="https://img.shields.io/badge/06-Anggota-E67E22?style=for-the-badge" /><br><br>
      <b>🧑‍💻 [Nama Anggota 6]</b><br>
      <sub>NIM: [XXXXXXXXXX]</sub><br><br>
      <img src="https://img.shields.io/badge/File-utils%20%26%20docs-E67E22?style=flat-square" /><br>
      <sub>Display helper CLI, README.md, dan diagram UML Draw.io</sub>
    </td>
  </tr>
</table>

</div>

---

## 📚 Konsep OOP yang Diterapkan

<details>
<summary><b>🔷 Abstraction</b></summary>

`BaseProduct` adalah abstract class yang mendefinisikan kerangka umum semua produk. Method `pengadonan()` dan `pemanggangan()` dideklarasikan abstract, memaksa setiap subclass mengimplementasikan proses produksinya sendiri.

</details>

<details>
<summary><b>🔶 Inheritance</b></summary>

Semua produk (`RotiManis`, `Croissant`, `ButterCookies`, `Muffin`) mewarisi `BaseProduct`, sehingga tidak perlu mendefinisikan ulang atribut dan method yang sama. Kode menjadi DRY *(Don't Repeat Yourself)*.

</details>

<details>
<summary><b>🔹 Interface</b></summary>

`ProductionInterface` mendefinisikan kontrak standar proses produksi: `baking()`, `packaging()`, dan `labeling()`. Semua produk wajib memenuhi kontrak ini.

</details>

<details>
<summary><b>🔸 Encapsulation</b></summary>

Setiap produk menyimpan data bahan baku, biaya, dan harga jual di dalam kelasnya sendiri. Akses dikelola melalui method `tampilkan_info()`, bukan akses langsung ke atribut.

</details>

---

## 📋 Dokumentasi

- 📐 **Class Diagram** — Lihat `docs/class_diagram.png` (dibuat dengan [Draw.io](https://draw.io))
- 🖥️ **Screenshot Output** — Lihat folder `docs/screenshots/`

---

<div align="center">

*Dibuat dengan 🍞 untuk Tugas Proyek PBO*

**Politeknik · Kelas B · 2024/2025**

</div>
