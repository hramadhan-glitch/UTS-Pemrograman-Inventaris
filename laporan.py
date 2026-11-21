def hitung_total_stok(data):
    """Menghitung jumlah seluruh stok barang."""
    return sum(barang["stok"] for barang in data)


def hitung_nilai_persediaan(data):
    """Menghitung nilai seluruh persediaan."""
    return sum(
        barang["stok"] * barang["harga"]
        for barang in data
    )


def rekap_kategori(data):
    """Menghitung jumlah barang berdasarkan kategori."""
    kategori = {barang["kategori"] for barang in data}

    return {
        nama: sum(
            barang["stok"]
            for barang in data
            if barang["kategori"] == nama
        )
        for nama in kategori
    }