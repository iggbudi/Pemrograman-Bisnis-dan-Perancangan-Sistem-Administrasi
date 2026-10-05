import sqlite3

koneksi = sqlite3.connect("kasir.db")
koneksi.execute("PRAGMA foreign_keys = ON")   # wajib: di SQLite FK mati secara bawaan

koneksi.executescript("""
CREATE TABLE IF NOT EXISTS produk (
    id_produk   INTEGER PRIMARY KEY AUTOINCREMENT,
    nama        TEXT    NOT NULL,
    harga       INTEGER NOT NULL CHECK (typeof(harga) = 'integer' AND harga > 0),
    stok        INTEGER NOT NULL DEFAULT 0 CHECK (stok >= 0)
);

CREATE TABLE IF NOT EXISTS transaksi (
    id_transaksi  INTEGER PRIMARY KEY AUTOINCREMENT,
    tanggal       TEXT    NOT NULL,              -- format 'YYYY-MM-DD'
    id_produk     INTEGER NOT NULL,
    jumlah        INTEGER NOT NULL CHECK (jumlah > 0),
    harga_satuan  INTEGER NOT NULL,              -- harga saat transaksi terjadi
    FOREIGN KEY (id_produk) REFERENCES produk(id_produk)
);
""")

# Data awal hanya diisi bila tabel produk masih kosong,
# sehingga skrip aman dijalankan berkali-kali.
jumlah_produk = koneksi.execute("SELECT COUNT(*) FROM produk").fetchone()[0]
if jumlah_produk == 0:
    koneksi.executemany(
        "INSERT INTO produk (nama, harga, stok) VALUES (?, ?, ?)",
        [
            ("Buku Tulis", 5000, 20),
            ("Pulpen", 3000, 30),
            ("Map Plastik", 2500, 10),
        ],
    )
    koneksi.execute(
        "INSERT INTO transaksi (tanggal, id_produk, jumlah, harga_satuan) "
        "VALUES (?, ?, ?, ?)",
        ("2026-10-12", 1, 2, 5000),
    )
    koneksi.commit()

koneksi.close()
print("Database dan tabel siap.")
