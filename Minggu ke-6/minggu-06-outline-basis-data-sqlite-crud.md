# DRAFT OUTLINE MINGGU 6 — Basis Data SQLite dan Operasi Data Dasar (CRUD)

**Mata kuliah:** PEMOGRAMAN BISNIS & PERANCANGAN SISTEM ADMINISTRASI  
**Kelas:** ABT-3D, Administrasi Bisnis — Politeknik Negeri Semarang  
**Alokasi:** Senin 16.00–17.30 WIB (KAN 1) dan Selasa 14.00–15.30 WIB (KAN3), masing-masing 90 menit  
**Status:** ACC awal (4 Oktober 2026); revisi penjelasan ERD mandiri sesuai masukan dosen. Turunan: slide `minggu-06-slide-basis-data-sqlite-crud.pptx`, lembar kerja `minggu-06-lembar-kerja-sqlite-crud.docx/.pdf`, kode di `kode-praktik/` (dibagikan) dan `kode-dosen/` (kunci).

## Posisi dalam proyek

Minggu 3 menghasilkan rancangan basis data relasional (entitas, atribut, PK/FK, normalisasi). Minggu 4–5 membangun logika bisnis Python yang modular dan bersih (`main.py` + `logika_bisnis.py`). Minggu 6 menghubungkan keduanya: rancangan tabel diwujudkan menjadi database SQLite nyata, lalu program Python menyimpan, menampilkan, mengubah, dan menghapus data lewat modul baru `database.py`. Minggu 7 baru masuk antarmuka Streamlit penuh; **minggu ini tampilan utama masih lewat terminal/console**.

**Catatan jalur Streamlit Minggu 5:** kelas yang memakai modul alternatif Streamlit pada Minggu 5 tetap mengerjakan `database.py` yang sama persis. Bedanya hanya pada tampilan: fungsi database dipanggil dari `app.py` (Streamlit), bukan dari `main.py` (terminal). Lapisan database tidak bergantung pada tampilan.

**Acuan RPS minggu 6:** mahasiswa mampu membuat basis data SQLite dan melakukan operasi data dasar. Bahan kajian: SQLite, SQL DDL/DML, pembuatan tabel, koneksi Python, query berparameter, serta operasi CRUD dasar. Pengalaman belajar: membuat database dan tabel proyek, mengisi data awal, lalu menguji tambah, tampil, ubah, dan hapus data. Indikator: database dan tabel terbentuk; PK/FK sesuai rancangan; seluruh operasi CRUD berhasil dan data dapat dibaca kembali. Evaluasi: praktikum database dan CRUD.

## Capaian akhir minggu

Mahasiswa dapat:
1. Menjelaskan basis data sebagai “lemari arsip digital”: database = lemari, tabel = buku besar, baris = satu catatan, kolom = kolom formulir.
2. Menjelaskan ERD (entitas, atribut, relasi, kardinalitas, PK/FK) dari contoh di modul ini dan menerjemahkannya menjadi perintah SQL `CREATE TABLE` dengan tipe data, PRIMARY KEY, FOREIGN KEY, dan aturan isian (`CHECK`) yang benar.
3. Membuat file database SQLite (`.db`) dari skrip Python dan mengisi beberapa baris data awal sebagai contoh.
4. Menghubungkan Python ke SQLite (`sqlite3`) dan menjalankan operasi CRUD dasar dengan **query berparameter**, dikemas sebagai fungsi dalam modul `database.py`.
5. Memverifikasi hasil: data tersimpan dapat dibaca kembali, perubahan terlihat, dan database menolak penghapusan yang akan merusak data terkait.

## Persiapan alat (tanpa instalasi tambahan)

- Cukup Python + VS Code dari Minggu 2. **Tidak perlu memasang program `sqlite3` terpisah** — di Windows program itu biasanya tidak tersedia. Semua SQL dijalankan lewat skrip Python (`sqlite3` sudah bawaan Python) dengan `executescript()`.
- Opsional untuk melihat isi tabel secara visual: ekstensi VS Code “SQLite Viewer”. Bila tidak bisa dipasang, cukup lihat hasil `SELECT` di terminal.
- Dosen membagikan **skrip awal `buat_database.py`** berisi tabel `produk` yang sudah jadi; mahasiswa menambahkan tabel berelasi dari rancangan yang dibuat di lembar kerja Minggu 6. Ini menghemat waktu mengetik dan mengurangi salah ketik.
- Nama file database: `kasir.db` untuk tema kasir (contoh berjalan sejak Minggu 4). Kelompok dengan tema lain memakai `<nama_proyek>.db` dengan pola yang sama.

## Bekal ERD — dibaca langsung di Minggu 6

Bagian ini menjelaskan kembali ERD dari awal. Mahasiswa tidak perlu membuka modul Minggu 3. Semua contoh, latihan, dan acuan tabel tersedia di bahan Minggu 6.

### 1. ERD itu apa?

**ERD (Entity Relationship Diagram)** adalah peta data: gambar yang memperlihatkan apa yang dicatat, informasi apa yang disimpan, dan bagaimana catatan saling terhubung. Bayangkan dua buku administrasi: buku daftar produk dan buku catatan penjualan. ERD adalah rancangan kedua buku itu sebelum dibuat di komputer. ERD bukan alur kerja; ERD tidak menunjukkan urutan klik atau langkah program.

- **Entitas** = jenis objek atau kejadian yang datanya perlu dicatat, misalnya produk dan transaksi. Dalam contoh relasional sederhana ini, masing-masing menjadi tabel.
- **Atribut** = keterangan tentang entitas, misalnya nama, harga, dan stok pada produk. Atribut menjadi kolom.
- **Baris/record** = satu catatan nyata, misalnya produk Buku Tulis. Buku Tulis adalah isi tabel produk, bukan nama entitas baru.
- **Relasi** = hubungan antarentitas, misalnya satu produk tercatat dalam beberapa transaksi. Garis penghubung pada ERD menggambarkan hubungan ini.

### 2. PK dan FK: nomor identitas dan nomor rujukan

**Primary Key (PK)** adalah penanda unik setiap baris di tabel. Ibarat nomor arsip, tidak boleh kembar atau kosong. `produk.id_produk` mengidentifikasi satu produk; nama tidak dijadikan PK karena nama dapat sama atau berubah.

**Foreign Key (FK)** adalah kolom rujukan ke kunci di tabel lain. `transaksi.id_produk` merujuk `produk.id_produk`. Nilai FK boleh berulang: beberapa transaksi dapat membeli produk yang sama. Pada contoh ini FK wajib terisi (`NOT NULL`), sehingga setiap transaksi harus menunjuk satu produk yang ada.

`id_produk` adalah PK di tabel produk, tetapi FK di tabel transaksi. Peran kunci ditentukan oleh tabelnya, bukan hanya nama kolomnya.

### 3. Membaca hubungan dan kardinalitas

Kardinalitas menjawab: satu catatan di sini berhubungan dengan berapa catatan di sana?

| Hubungan | Arti sederhana | Contoh aturan bisnis |
|---|---|---|
| 1:1 | Satu berhubungan dengan paling banyak satu | Satu pegawai memiliki paling banyak satu kartu akses aktif; satu kartu milik satu pegawai. |
| 1:N | Satu berhubungan dengan banyak | Satu produk dapat muncul dalam banyak catatan transaksi; setiap catatan transaksi merujuk satu produk. |
| M:N | Banyak berhubungan dengan banyak | Satu nota memuat banyak produk dan satu produk muncul di banyak nota. Gunakan tabel penghubung detail_transaksi. |

Untuk praktik minggu ini kita memakai **1:N**. Tentukan hubungan dari aturan bisnis, bukan dari banyaknya baris contoh.

```text
PRODUK                               TRANSAKSI
PK id_produk                         PK id_transaksi
   nama                                 tanggal
   harga                             FK id_produk
   stok                                 jumlah
                                        harga_satuan

produk.id_produk (PK) <--- transaksi.id_produk (FK)
Satu produk: 0..N catatan transaksi. Setiap transaksi: tepat 1 produk.
```

`1` berarti satu; `N` berarti banyak; `0..N` berarti boleh belum pernah terjual, atau sudah terjual berkali-kali. FK diletakkan di sisi banyak, yaitu transaksi. Jika produk belum pernah terjual, tabel transaksi tidak perlu diisi baris kosong untuk produk itu.

**Batas contoh:** tabel `transaksi` di skrip minggu ini adalah catatan penjualan satu jenis produk, bukan satu nota lengkap berisi banyak produk. Untuk nota banyak produk, gunakan `transaksi` (kepala nota), `detail_transaksi` (baris barang), dan `produk`. Ini konteks M:N, bukan kewajiban menambah struktur pada praktik dasar ini.

### 4. Lihat hubungan melalui data kecil

| produk.id_produk (PK) | nama | harga | stok |
|---|---|---|---|
| 1 | Buku Tulis | 5000 | 20 |
| 2 | Pulpen | 3000 | 30 |

| id_transaksi (PK) | tanggal | id_produk (FK) | jumlah | harga_satuan |
|---|---|---|---|---|
| 1 | 2026-10-12 | 1 | 2 | 5000 |
| 2 | 2026-10-12 | 1 | 1 | 5000 |

Dua baris transaksi berbeda sama-sama merujuk produk ID 1; ini sah karena FK boleh berulang. Pulpen ID 2 belum mempunyai transaksi; ini juga sah. Transaksi dengan produk ID 999 ditolak jika produk itu tidak ada dan penjaga FK aktif.

Data di atas hanya ilustrasi hubungan, bukan instruksi menambah data awal skrip. Skrip praktik tetap mengisi tiga produk dan satu transaksi seperti semula.

### 5. Dari ERD ke SQLite

1. Tentukan dua entitas dan hubungan dengan satu kalimat bisnis.
2. Jadikan entitas sebagai tabel dan atribut sebagai kolom.
3. Pilih PK setiap tabel; untuk ID otomatis pakai `INTEGER PRIMARY KEY AUTOINCREMENT`.
4. Untuk hubungan 1:N, letakkan FK di tabel sisi N. Tipe ID PK dan FK pada contoh ini sama-sama `INTEGER`.
5. Tulis rujukannya: `FOREIGN KEY (id_produk) REFERENCES produk(id_produk)`.
6. Tambahkan aturan isian: `NOT NULL` untuk wajib terisi dan `CHECK` untuk nilai yang diperbolehkan. Aturan ini melengkapi ERD, bukan pengganti relasi.
7. Aktifkan `PRAGMA foreign_keys = ON` pada setiap koneksi SQLite agar rujukan benar-benar dijaga.

**Cek pemahaman sebelum mengetik:** (a) Buku Tulis termasuk entitas atau isi baris? (b) Mengapa `transaksi.id_produk` boleh berulang? (c) Di tabel mana FK diletakkan untuk hubungan produk–transaksi? (d) Bolehkah produk belum memiliki transaksi?

**Pegangan dosen:** (a) isi baris produk; (b) produk yang sama dapat terjual berkali-kali; (c) transaksi, sisi N; (d) boleh, kardinalitas minimalnya nol.

## Pertemuan 1 — Senin: dari rancangan ke tabel yang hidup (90 menit)

| Menit | Kegiatan | Bukti/cek cepat |
|---|---|---|
| 0–10 | Pemantik kebutuhan penyimpanan dan pengantar ERD sebagai peta data: di mana hasil input kita “tinggal” selama ini? | Mahasiswa menyadari data hilang saat program ditutup. |
| 10–25 | Bekal ERD mandiri: entitas vs isi baris, atribut, PK/FK, relasi 1:N dan 0..N dengan data kecil. Petakan ke tabel SQLite; kenalkan database satu file tanpa server. | Menjelaskan tabel `produk`/`transaksi` dengan istilah bisnis. |
| 25–40 | Dosen menjalankan `buat_database.py`: `CREATE TABLE IF NOT EXISTS produk(...)` dan `transaksi(...)` dengan FOREIGN KEY. Tunjukkan `PRAGMA foreign_keys = ON` dan aturan `CHECK`. Jalankan skrip dua kali untuk menunjukkan `IF NOT EXISTS` mencegah error “table already exists”. | Dua tabel terbentuk; tipe data dan kunci sesuai contoh ERD Minggu 6. |
| 40–65 | Praktik: unduh skrip awal, sesuaikan/tambahkan satu tabel berelasi dari rancangan sederhana yang dibuat di A1 Minggu 6, isi 2–3 baris data contoh (`INSERT`), jalankan. | File `.db` ada; tabel memuat data awal. |
| 65–85 | Uji aturan database (lihat “Tiga uji pelanggaran” di bawah) lalu periksa isi dengan `SELECT * FROM produk;`. | Mahasiswa melihat pesan error dan menjelaskan mengapa kunci/aturan wajib dijaga. |
| 85–90 | Rangkuman: tabel menyimpan data meski program ditutup; simpan file untuk pertemuan Selasa. | `kasir.db` dan `buat_database.py` tersimpan di folder proyek. |

**Skrip awal `buat_database.py` (ilustrasi, bukan jawaban lengkap praktikum):**

```python
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
koneksi.close()
print("Database dan tabel siap.")
```

Mengapa `transaksi` menyimpan `harga_satuan` sendiri? Jika harga produk nanti diubah, nilai transaksi lama tidak boleh ikut berubah — sama seperti nota lama tidak diganti saat daftar harga toko diperbarui. Ini contoh nyata keputusan rancangan dalam administrasi bisnis.

**Tiga uji pelanggaran (menit 65–85):**

| Uji | Perintah | Hasil yang diharapkan |
|---|---|---|
| A. Harga berupa teks | `INSERT INTO produk (nama, harga) VALUES ('Pensil', 'seribu')` | Ditolak: `CHECK constraint failed` |
| B. Transaksi untuk produk yang tidak ada | `INSERT INTO transaksi (tanggal, id_produk, jumlah, harga_satuan) VALUES ('2026-10-12', 999, 1, 5000)` | Ditolak: `FOREIGN KEY constraint failed` |
| C. Sama seperti B, tetapi **tanpa** baris `PRAGMA foreign_keys = ON` | (jalankan di koneksi baru tanpa pragma) | **Diterima** — tunjukkan bahwa tanpa pragma database tidak menjaga relasi |

Pertanyaan pengarah: tanpa aturan `CHECK`, SQLite sebenarnya **mau** menyimpan teks “seribu” di kolom angka (SQLite longgar soal tipe data). Siapa yang harus menjaga pintu masuk data? Jawaban: dua lapis — validasi Python Minggu 5 di depan, aturan database di belakang. Hapus baris uji C setelah demo.

## Pertemuan 2 — Selasa: Python menyimpan dan mengelola data (90 menit)

| Menit | Kegiatan | Bukti/cek cepat |
|---|---|---|
| 0–10 | Ulas tabel Senin; tunjuk fungsi Minggu 5 di `logika_bisnis.py` yang akan memakai data dari database. Perkenalkan rencana file: `main.py` (tampilan) → `logika_bisnis.py` (hitung) + `database.py` (simpan). | Mahasiswa bisa menyebut tugas tiap file. |
| 10–25 | Dosen contohkan fungsi `buka_koneksi()`, `tambah_produk()`, dan `daftar_produk()` di `database.py` dengan query berparameter `?`. Jelaskan mengapa jangan menyusun query lewat rangkaian teks. | Program menyimpan satu baris dan membacanya kembali. |
| 25–45 | Praktik INSERT dari `main.py`: minta input pengguna, ubah harga dengan `int()` (Minggu 5 memakai `float`; rupiah disimpan bulat), tangani input salah dengan `try/except`, lalu panggil `tambah_produk()`. | Data baru tampil saat `daftar_produk()` dipanggil ulang. |
| 45–70 | Praktik `ubah_harga()` dan `hapus_produk()` berdasarkan `id`: tampilkan `rowcount` agar terlihat apakah ID ada; dosen contohkan konfirmasi “yakin hapus? (y/n)”. | Empat operasi CRUD berhasil pada data contoh. |
| 70–85 | Uji silang empat skenario (lihat tabel uji di bawah); catat hasil aktual dan satu perbaikan. | Tabel uji terisi; data konsisten setelah setiap operasi. |
| 85–90 | Refleksi dan jembatan ke Minggu 7: `database.py` tidak perlu diubah; Minggu 7 hanya mengganti `main.py` dengan form Streamlit. | File kerja dan catatan pengujian tersimpan. |

**Contoh pola `database.py` (ilustrasi):**

```python
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
        koneksi.close()   # tetap ditutup walau terjadi error, agar file .db tidak terkunci


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
```

`hapus_produk(id_produk)` dibuat mahasiswa dengan pola yang sama (`DELETE ... WHERE id_produk = ?`).

**Contoh pemanggilan dari `main.py`:**

```python
import sqlite3
import database

try:
    nama = input("Nama produk: ")
    harga = int(input("Harga (angka bulat, tanpa Rp/titik): "))
    stok = int(input("Stok awal: "))
    database.tambah_produk(nama, harga, stok)
    print("Produk tersimpan.")
except ValueError:
    print("Harga dan stok harus angka bulat.")
except sqlite3.IntegrityError as e:
    print("Database menolak data:", e)

for baris in database.daftar_produk():
    print(baris)
```

**Tabel uji Selasa (minimal empat skenario):**

| No | Skenario | Langkah | Hasil yang diharapkan |
|---|---|---|---|
| 1 | Tambah normal | Tambah “Penghapus”, 2000, stok 15 | Muncul di daftar dengan ID baru |
| 2 | Ubah harga | Ubah harga ID 2 (Pulpen) menjadi 3500 | `rowcount` = 1; harga baru tampil |
| 3 | Ubah/hapus ID yang tidak ada | Ubah harga ID 999 | `rowcount` = 0; pesan “ID tidak ditemukan” |
| 4 | Hapus produk yang sudah punya transaksi | Hapus ID 1 (Buku Tulis, dirujuk tabel `transaksi`) | Ditolak `FOREIGN KEY constraint failed`; data lain utuh. Hapus ID 3 (Map Plastik, tanpa transaksi) → berhasil dan hilang dari daftar |

Data awal (diisi `buat_database.py`): Buku Tulis (ID 1, punya satu transaksi), Pulpen (ID 2), Map Plastik (ID 3). Lembar kerja menambah skenario 5–6 untuk input salah (`abc` dan harga negatif).

Catatan praktik: gunakan selalu `?` (parameter) alih-alih menyisipkan nilai langsung ke string SQL; panggil `commit()` setelah `INSERT`/`UPDATE`/`DELETE`; tutup koneksi dengan `try/finally` (catatan: `with sqlite3.connect(...)` hanya mengurus commit, **tidak** menutup koneksi). Untuk pemula non-IT, tampilkan data dengan `print` dulu; tabel rapi menyusul di Streamlit Minggu 7.

## Luaran dan pemeriksaan

- **File:** `kasir.db` (atau `<nama_proyek>.db`) berisi minimal dua tabel berelasi sesuai ERD; `buat_database.py`; `database.py` berisi fungsi CRUD berparameter; `main.py` (atau `app.py` untuk jalur Streamlit) yang memanggilnya.
- **Bukti:** skrip yang bisa dijalankan, hasil `SELECT` sebelum/sesudah perubahan, hasil tiga uji pelanggaran Senin, dan tabel pengujian empat skenario Selasa.
- **Kriteria selesai:** tabel terbentuk dengan PK/FK/CHECK sesuai rancangan di lembar kerja Minggu 6; `PRAGMA foreign_keys = ON` aktif di setiap koneksi; data awal terisi; operasi CRUD berhasil dan data dapat dibaca kembali; penghapusan yang melanggar relasi ditolak; input salah ditangani tanpa membuat program berhenti.
- **Catatan pengajaran non-IT:** analogi lemari arsip/buku besar/nota, demonstrasi lebih dulu, skrip awal dibagikan agar waktu praktik dipakai untuk memahami bukan mengetik, gunakan data kecil (2–3 baris) agar mudah diperiksa manual, dan hindari istilah teknis tanpa contoh. Ingatkan untuk tidak menaruh data pribadi nyata — pakai data simulasi.

**Sumber internal:** `rps/matriks-rps-pemograman-bisnis-perancangan-sistem-administrasi-python-streamlit-vscode.csv` (baris minggu 6); `bahan-ajar/modul/minggu-03-perancangan-basis-data-relasional.md`; `Minggu ke-5/minggu-05-modul-praktik-fungsi-modul-error-handling.docx` dan versi Streamlit-nya; `pengajaran/jadwal/jadwal-mengajar-polines-2026-2027.csv`.
