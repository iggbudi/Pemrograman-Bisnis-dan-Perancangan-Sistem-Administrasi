import sqlite3

NAMA_DB = "kasir.db"


def buka_koneksi():
    koneksi = sqlite3.connect(NAMA_DB)
    koneksi.execute("PRAGMA foreign_keys = ON")   # ulangi di setiap koneksi
    return koneksi


def tambah_produk(nama, harga, stok):
    koneksi = buka_koneksi()
    try:
        koneksi.execute(
            "INSERT INTO produk (nama, harga, stok) VALUES (?, ?, ?)",
            (nama, harga, stok),
        )
        koneksi.commit()
    finally:
        koneksi.close()   # tetap ditutup walau terjadi error


def daftar_produk():
    koneksi = buka_koneksi()
    try:
        return koneksi.execute(
            "SELECT id_produk, nama, harga, stok FROM produk"
        ).fetchall()
    finally:
        koneksi.close()


def ubah_harga(id_produk, harga_baru):
    koneksi = buka_koneksi()
    try:
        cursor = koneksi.execute(
            "UPDATE produk SET harga = ? WHERE id_produk = ?",
            (harga_baru, id_produk),
        )
        koneksi.commit()
        return cursor.rowcount   # 0 berarti ID tidak ditemukan
    finally:
        koneksi.close()


def hapus_produk(id_produk):
    # LATIHAN D: lengkapi fungsi ini dengan pola yang sama seperti ubah_harga().
    # 1. buka koneksi dengan buka_koneksi()
    # 2. jalankan "DELETE FROM produk WHERE id_produk = ?" dengan parameter (id_produk,)
    # 3. commit(), lalu kembalikan cursor.rowcount (0 berarti ID tidak ditemukan)
    # 4. tutup koneksi di dalam finally
    raise NotImplementedError("hapus_produk() belum dilengkapi (Latihan D)")
