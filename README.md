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

*Proyek Ujian Akhir Semester Mata Kuliah Pemrograman Berorientasi Objek*

---

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Paradigma-OOP-F7B731?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Selesai-2ECC71?style=for-the-badge)
![License](https://img.shields.io/badge/License-Academic-9B59B6?style=for-the-badge)

</div>

---

## 🥐 Tentang Proyek

**Hanari Bakery System** adalah aplikasi manajemen produksi berbasis Python yang dirancang untuk membantu toko roti **Hanari Bakery** mengelola produk, bahan baku, estimasi profit, dan simulasi proses produksi secara digital.

Proyek ini dikembangkan menggunakan konsep **Object-Oriented Programming (OOP)** dengan menerapkan:
- 🔷 **Abstraction** — Kelas induk abstrak (`BaseProduct`) untuk standarisasi produk
- 🔶 **Inheritance** — Setiap produk mewarisi properti dan method dari `BaseProduct`
- 🔹 **Interface** — Standarisasi proses melalui `ProductionInterface`, `FermentationInterface`, dan `ToppingInterface`
- 🔸 **Encapsulation** — Data produk terlindungi dan diakses melalui method masing-masing kelas

---

## 🍞 Produk yang Dikelola

| Produk | Kode | Proses Produksi |
|--------|------|------------------|
| 🍞 Roti Manis | `RT001` | Pengadonan → Pengembangan → Pemanggangan |
| 🥐 Croissant | `RT002` | Pengadonan → Pengembangan (laminasi) → Pemanggangan |
| 🍪 Butter Cookies | `RT003` | Pengadonan → Topping → Pemanggangan |
| 🧁 Muffin | `RT004` | Pengadonan → Pengembangan → Topping → Pemanggangan |

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
│  5.  Keluar                                 │
└─────────────────────────────────────────────┘
```

- **📦 Manajemen Produk** — Tambah dan tampilkan produk beserta detail bahan baku
- **💰 Kalkulator Profit** — Estimasi keuntungan berdasarkan jumlah pcs yang diproduksi
- **⚙️ Simulasi Produksi** — Jalankan tahapan produksi secara berurutan sesuai jenis roti

---

## 🗂️ Struktur Proyek

```
HanariBakery/
│
├── 📄 main.py                  # Entry point, menu utama & logika program
│
├── 🏗️ base_product.py          # Abstract base class + ProductionInterface,
│                                #   FermentationInterface, ToppingInterface
│
├── 🍞 roti_manis.py            # Kelas RotiManis
├── 🥐 croissant.py             # Kelas Croissant
├── 🍪 butter_cookies.py        # Kelas ButterCookies
├── 🧁 muffin.py                # Kelas Muffin
│
├── 📁 assets/
│   └── class_diagram.png       # Diagram UML (Draw.io)
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
      │ + hitung_profit() │
      │ + pengadonan()*   │
      │ + pemanggangan()* │
      └──┬──────┬──┬──┬──┘
         │      │  │  │
    ┌────▼─┐ ┌──▼─┐ ┌▼──────────┐ ┌──▼───┐
    │Roti  │ │Croi│ │  Butter   │ │Muffin│
    │Manis │ │ssnt│ │  Cookies  │ │      │
    └──────┘ └────┘ └───────────┘ └──────┘
```

<div align="center">
<img src="assets/class_diagram.png" alt="Diagram Class Hanari Bakery" width="800"/>
</div>

---

## 🚀 Cara Menjalankan

### Prasyarat
- Python **3.10** atau lebih baru
- Tidak memerlukan library eksternal

### Instalasi & Menjalankan

```bash
# 1. Clone repository ini
git clone https://github.com/sulthanhafizh2006/Kelompok-3-uas-pbo-kelas-b.git

# 2. Masuk ke direktori proyek
cd Kelompok-3-uas-pbo-kelas-b

# 3. Jalankan program
python main.py
```

### Contoh Output Kalkulator Profit

```
== Kalkulator Estimasi Profit ==
Produk          : Muffin
Jumlah Produksi : 15 pcs
Biaya Produksi  : Rp 2.500 / pcs
Harga Jual      : Rp 5.500 / pcs
Estimasi Profit : Rp 45.000
```

---

## 👥 Tim Pengembang — Kelompok 3

<div align="center">

<table>
  <tr>
    <td align="center" width="300">
      <img src="https://img.shields.io/badge/01-Anggota-F7B731?style=for-the-badge" /><br><br>
      <b>🧑‍💻 Sulthan Hafizh Putra Agung</b><br>
      <sub>NIM: K3525013</sub><br><br>
      <img src="https://img.shields.io/badge/File-README.md%20%26%20main.py-3776AB?style=flat-square&logo=python" /><br>
      <sub>Menu utama, routing antar fitur, dan entry point program</sub>
    </td>
    <td align="center" width="300">
      <img src="https://img.shields.io/badge/02-Anggota-E74C3C?style=for-the-badge" /><br><br>
      <b>🧑‍💻 Zahra Faizza Kuncoroningrum</b><br>
      <sub>NIM: K3525017</sub><br><br>
      <img src="https://img.shields.io/badge/File-base__product.py-E74C3C?style=flat-square" /><br>
      <sub>Abstract base class & seluruh interface sebagai fondasi arsitektur OOP</sub>
    </td>
    <td align="center" width="300">
      <img src="https://img.shields.io/badge/03-Anggota-2ECC71?style=for-the-badge" /><br><br>
      <b>🧑‍💻 Aksya Nayla Fitriana</b><br>
      <sub>NIM: K3525047</sub><br><br>
      <img src="https://img.shields.io/badge/File-roti__manis.py-2ECC71?style=flat-square" /><br>
      <sub>Implementasi produk Roti Manis beserta proses produksinya</sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="300">
      <img src="https://img.shields.io/badge/04-Anggota-9B59B6?style=for-the-badge" /><br><br>
      <b>🧑‍💻 Adibah Ruhil</b><br>
      <sub>NIM: K3525044</sub><br><br>
      <img src="https://img.shields.io/badge/File-croissant.py-9B59B6?style=flat-square" /><br>
      <sub>Implementasi produk Croissant beserta proses produksinya</sub>
    </td>
    <td align="center" width="300">
      <img src="https://img.shields.io/badge/05-Anggota-1ABC9C?style=for-the-badge" /><br><br>
      <b>🧑‍💻 Allicya Nailah Fairuza</b><br>
      <sub>NIM: K3525048</sub><br><br>
      <img src="https://img.shields.io/badge/File-butter__cookies.py-1ABC9C?style=flat-square" /><br>
      <sub>Implementasi produk Butter Cookies beserta proses produksinya</sub>
    </td>
    <td align="center" width="300">
      <img src="https://img.shields.io/badge/06-Anggota-E67E22?style=for-the-badge" /><br><br>
      <b>🧑‍💻 Faris Rafiuddin Hannan</b><br>
      <sub>NIM: K3525058</sub><br><br>
      <img src="https://img.shields.io/badge/File-muffin.py-E67E22?style=flat-square" /><br>
      <sub>Implementasi produk Muffin beserta proses produksinya</sub>
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

Semua produk (`RotiManis`, `Croissant`, `ButterCookies`, `Muffin`) mewarisi `BaseProduct`, sehingga tidak perlu mendefinisikan ulang atribut dan method yang sama (nama, kode, bahan baku, biaya, harga jual). Kode menjadi DRY *(Don't Repeat Yourself)*.

</details>

<details>
<summary><b>🔹 Interface</b></summary>

- `ProductionInterface` — kontrak wajib semua produk: `baking()`, `packaging()`, `labeling()`.
- `FermentationInterface` — kontrak khusus produk yang mengembang: `pengembangan()` (Roti Manis, Croissant, Muffin).
- `ToppingInterface` — kontrak khusus produk dengan topping: `topping()` (Butter Cookies, Muffin).

Pemecahan interface ini menerapkan **ISP** *(Interface Segregation Principle)* agar setiap subclass hanya mengimplementasikan method yang relevan bagi dirinya.

</details>

<details>
<summary><b>🔸 Encapsulation</b></summary>

Setiap produk menyimpan data bahan baku, biaya, dan harga jual di dalam kelasnya sendiri. Akses dikelola melalui method `tampilkan_info()` dan `hitung_profit()`, bukan akses langsung ke atribut dari luar kelas.

</details>

---

## 📋 Dokumentasi

- 📐 **Class Diagram** — Lihat `assets/class_diagram.png` (dibuat dengan [Draw.io](https://draw.io))
- 🖥️ **Screenshot Output** — Lihat folder `docs/screenshots/`

---

<div align="center">

*Dibuat dengan 🍞 untuk Tugas Proyek PBO*

**Kelompok 3 · Kelas B · 2026**

</div>
