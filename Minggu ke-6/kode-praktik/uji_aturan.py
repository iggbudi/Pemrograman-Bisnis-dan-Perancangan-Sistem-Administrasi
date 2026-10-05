import sqlite3


def coba(judul, koneksi, perintah_sql):
    try:
        koneksi.execute(perintah_sql)
        print(judul, "-> DITERIMA")
    except sqlite3.IntegrityError as e:
        print(judul, "-> DITOLAK:", e)


# Koneksi dengan penjaga relasi aktif
koneksi = sqlite3.connect("kasir.db")
koneksi.execute("PRAGMA foreign_keys = ON")
coba("A. Harga berupa teks", koneksi,
     "INSERT INTO produk (nama, harga) VALUES ('Pensil', 'seribu')")
coba("B. Produk tidak ada", koneksi,
     "INSERT INTO transaksi (tanggal, id_produk, jumlah, harga_satuan) "
     "VALUES ('2026-10-12', 999, 1, 5000)")
koneksi.rollback()   # batalkan apa pun yang sempat masuk
koneksi.close()

# Koneksi TANPA baris PRAGMA: lihat bedanya
koneksi = sqlite3.connect("kasir.db")
coba("C. Produk tidak ada, tanpa PRAGMA", koneksi,
     "INSERT INTO transaksi (tanggal, id_produk, jumlah, harga_satuan) "
     "VALUES ('2026-10-12', 999, 1, 5000)")
koneksi.rollback()   # jangan simpan data yatim hasil uji C
koneksi.close()
