# Aplikasi Manajemen Inventaris Barang

## Deskripsi
Aplikasi Manajemen Inventaris Barang merupakan program berbasis Python dengan antarmuka Command Line Interface (CLI). Aplikasi ini digunakan untuk mengelola data inventaris barang melalui terminal.

## Fitur
1. Menampilkan seluruh data barang.
2. Menambahkan barang baru.
3. Mencari barang.
4. Memfilter barang berdasarkan kategori.
5. Menghapus barang.
6. Menampilkan rekapitulasi stok dan nilai persediaan.
7. Menampilkan daftar kategori.
8. Menyimpan hasil pengolahan ke file CSV.

## Teknologi
- Bahasa pemrograman: Python
- Penyimpanan data: CSV
- Library: Python Standard Library

## Struktur Proyek
```text
UTS_PEMOGRAMAN/
├── main.py
├── README.md
├── requirements.txt
├── data/
│   └── barang.csv
├── output/
│   └── hasil_barang.csv
├── inventaris/
│   ├── __init__.py
│   ├── operasi.py
│   ├── laporan.py
│   └── file_manager.py
└── dokumentasi/
    └── laporan_uts.pdf
```

## Cara Menjalankan
1. Pastikan Python sudah terpasang.
2. Buka terminal pada folder proyek.
3. Jalankan perintah berikut:

```bash
py main.py
```

4. Pilih menu yang tersedia pada aplikasi.

## Data Input
Data awal inventaris disimpan dalam file `data/barang.csv`.

## Hasil Output
Hasil penyimpanan data dapat ditemukan pada folder `output/` dengan nama `hasil_barang.csv`.

## Referensi
- https://docs.python.org/3/
- https://docs.python.org/3/library/csv.html

## Keterangan Bantuan AI
ChatGPT digunakan sebagai alat bantu dalam memahami konsep pemrograman, menyusun rancangan awal, dan membantu proses debugging. Kode akhir diperiksa dan diuji kembali oleh penyusun.
