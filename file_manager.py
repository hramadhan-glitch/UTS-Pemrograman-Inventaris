
import csv
from pathlib import Path

KOLOM = ["kode", "nama", "kategori", "stok", "harga"]


def baca_data(lokasi_file):
    """Membaca data barang dari CSV."""
    path = Path(lokasi_file)

    if not path.exists():
        raise FileNotFoundError(f"File tidak ditemukan: {path}")

    data = []

    with path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames != KOLOM:
            raise ValueError("Format kolom CSV tidak sesuai.")

        for nomor, baris in enumerate(reader, start=2):
            try:
                barang = {
                    "kode": baris["kode"].strip(),
                    "nama": baris["nama"].strip(),
                    "kategori": baris["kategori"].strip(),
                    "stok": int(baris["stok"]),
                    "harga": int(baris["harga"])
                }

                if not all([
                    barang["kode"],
                    barang["nama"],
                    barang["kategori"]
                ]):
                    raise ValueError("Kolom teks tidak boleh kosong.")

                if barang["stok"] < 0 or barang["harga"] < 0:
                    raise ValueError("Stok dan harga tidak boleh negatif.")

                data.append(barang)

            except (ValueError, TypeError) as error:
                raise ValueError(
                    f"Data tidak valid pada baris {nomor}: {error}"
                ) from error

    return data


def simpan_data(data, lokasi_file):
    """Menyimpan data barang ke CSV."""
    path = Path(lokasi_file)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=KOLOM)
        writer.writeheader()
        writer.writerows(data)

    return str(path)
