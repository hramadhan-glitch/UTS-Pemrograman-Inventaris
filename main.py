from pathlib import Path

from inventaris.file_manager import baca_data, simpan_data
from inventaris.operasi import (
    tambah_barang,
    cari_barang,
    filter_barang,
    hapus_barang,
    daftar_kategori
)
from inventaris.laporan import (
    hitung_total_stok,
    hitung_nilai_persediaan,
    rekap_kategori
)

FOLDER = Path(__file__).resolve().parent
FILE_DATA = FOLDER / "data" / "barang.csv"
FILE_OUTPUT = FOLDER / "output" / "hasil_barang.csv"


def tampilkan_barang(data):
    """Menampilkan daftar barang."""
    if not data:
        print("Tidak ada data barang.")
        return

    print("\n=== DAFTAR BARANG ===")

    for barang in data:
        print(
            f"{barang['kode']} | {barang['nama']} | "
            f"{barang['kategori']} | Stok: {barang['stok']} | "
            f"Harga: Rp{barang['harga']:,}"
        )


def input_angka(pesan):
    """Meminta input angka bulat yang valid."""
    while True:
        try:
            angka = int(input(pesan))

            if angka < 0:
                print("Angka tidak boleh negatif.")
                continue

            return angka

        except ValueError:
            print("Masukkan angka yang benar.")


def main():
    try:
        data = baca_data(FILE_DATA)

    except (FileNotFoundError, ValueError, OSError) as error:
        print("Gagal membaca data:", error)
        return

    while True:
        print("\n===== APLIKASI INVENTARIS BARANG =====")
        print("1. Tampilkan barang")
        print("2. Tambah barang")
        print("3. Cari barang")
        print("4. Filter barang")
        print("5. Hapus barang")
        print("6. Lihat rekapitulasi")
        print("7. Lihat kategori")
        print("8. Simpan hasil")
        print("9. Keluar")

        pilihan = input("Pilih menu: ").strip()

        try:
            if pilihan == "1":
                tampilkan_barang(data)

            elif pilihan == "2":
                print("\n=== TAMBAH BARANG ===")

                barang = {
                    "kode": input("Kode barang: ").strip(),
                    "nama": input("Nama barang: ").strip(),
                    "kategori": input("Kategori: ").strip(),
                    "stok": input_angka("Stok: "),
                    "harga": input_angka("Harga: ")
                }

                tambah_barang(data, barang)
                print("Barang berhasil ditambahkan.")

            elif pilihan == "3":
                kata = input("Masukkan kode atau nama: ")
                hasil = cari_barang(data, kata)
                tampilkan_barang(hasil)

            elif pilihan == "4":
                print("Kategori tersedia:", daftar_kategori(data))

                kategori = input(
                    "Masukkan kategori (kosongkan jika tidak digunakan): "
                ).strip()

                batas = input(
                    "Stok maksimum (kosongkan jika tidak digunakan): "
                ).strip()

                stok_maksimum = int(batas) if batas else None

                if stok_maksimum is not None and stok_maksimum < 0:
                    raise ValueError("Batas stok tidak boleh negatif.")

                hasil = filter_barang(
                    data,
                    kategori or None,
                    stok_maksimum
                )

                tampilkan_barang(hasil)

            elif pilihan == "5":
                kode = input("Masukkan kode barang yang dihapus: ")

                if hapus_barang(data, kode):
                    print("Barang berhasil dihapus.")
                else:
                    print("Kode barang tidak ditemukan.")

            elif pilihan == "6":
                print("\n=== REKAPITULASI ===")
                print("Jumlah jenis barang:", len(data))
                print("Total seluruh stok:", hitung_total_stok(data))
                print(
                    "Nilai persediaan: Rp",
                    f"{hitung_nilai_persediaan(data):,}"
                )

                print("\nStok berdasarkan kategori:")
                for kategori, jumlah in rekap_kategori(data).items():
                    print(f"{kategori}: {jumlah}")

            elif pilihan == "7":
                print("Kategori unik:", daftar_kategori(data))

            elif pilihan == "8":
                lokasi = simpan_data(data, FILE_OUTPUT)
                print("Data berhasil disimpan ke:", lokasi)

            elif pilihan == "9":
                print("Terima kasih. Program selesai.")
                break

            else:
                print("Pilihan menu tidak tersedia.")

        except (ValueError, OSError) as error:
            print("Terjadi kesalahan:", error)


if __name__ == "__main__":
    main()