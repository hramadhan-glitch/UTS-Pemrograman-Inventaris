
def tambah_barang(data, barang):
    """Menambahkan barang baru."""
    wajib = ["kode", "nama", "kategori"]

    if not all(barang.get(kolom) for kolom in wajib):
        raise ValueError("Kode, nama, dan kategori wajib diisi.")

    if any(item["kode"] == barang["kode"] for item in data):
        raise ValueError("Kode barang sudah digunakan.")

    if not isinstance(barang["stok"], int) or barang["stok"] < 0:
        raise ValueError("Stok harus berupa angka nol atau lebih.")

    if not isinstance(barang["harga"], int) or barang["harga"] < 0:
        raise ValueError("Harga harus berupa angka nol atau lebih.")

    data.append(barang)
    return True


def cari_barang(data, kata_kunci):
    """Mencari barang berdasarkan kode atau nama."""
    kata_kunci = kata_kunci.lower()

    return [
        barang for barang in data
        if kata_kunci in barang["kode"].lower()
        or kata_kunci in barang["nama"].lower()
    ]


def filter_barang(data, kategori=None, stok_maksimum=None):
    """Memfilter barang berdasarkan kategori atau stok."""
    hasil = data

    if kategori:
        hasil = [
            barang for barang in hasil
            if barang["kategori"].lower() == kategori.lower()
        ]

    if stok_maksimum is not None:
        hasil = [
            barang for barang in hasil
            if barang["stok"] <= stok_maksimum
        ]

    return hasil


def hapus_barang(data, kode):
    """Menghapus barang berdasarkan kode."""
    for barang in data:
        if barang["kode"] == kode:
            data.remove(barang)
            return True

    return False


def daftar_kategori(data):
    """Menghasilkan kategori unik."""
    return {barang["kategori"] for barang in data}
