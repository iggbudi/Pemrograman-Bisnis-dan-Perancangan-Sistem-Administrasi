# DRAFT OUTLINE MINGGU 6 — Basis Data SQLite dan Operasi Data Dasar (CRUD)

**Mata kuliah:** PEMOGRAMAN BISNIS & PERANCANGAN SISTEM ADMINISTRASI  
**Kelas:** ABT-3D, Administrasi Bisnis — Politeknik Negeri Semarang  
**Alokasi:** Senin 16.00–17.30 WIB (KAN 1) dan Selasa 14.00–15.30 WIB (KAN3), masing-masing 90 menit  
**Status:** ACC awal (4 Oktober 2026); revisi penjelasan ERD mandiri sesuai masukan dosen; revisi 6 Oktober 2026: Streamlit dimajukan ke Pertemuan 2 (perlu konfirmasi ulang dosen). Cadangan versi terminal di `cadangan-sebelum-streamlit-6-2/`. Turunan: slide `minggu-06-slide-basis-data-sqlite-crud.pptx`, lembar kerja `minggu-06-lembar-kerja-sqlite-crud.docx/.pdf`, kode Pertemuan 1 di `kode-praktik/`; seluruh kode Pertemuan 2 di `6.2/` (`6.2/kode-praktik/` dibagikan, `6.2/kode-dosen/` kunci). Slide dan lembar kerja khusus Pertemuan 2 juga di `6.2/` (`minggu-06-pertemuan-2-slide-crud-streamlit.pptx`, `minggu-06-pertemuan-2-lembar-kerja-crud-streamlit.docx/.pdf`).

## Posisi dalam proyek

Minggu 3 menghasilkan rancangan basis data relasional (entitas, atribut, PK/FK, normalisasi). Minggu 4–5 membangun logika bisnis Python yang modular dan bersih (`main.py` + `logika_bisnis.py`). Minggu 6 menghubungkan keduanya: rancangan tabel diwujudkan menjadi database SQLite nyata, lalu program Python menyimpan, menampilkan, mengubah, dan menghapus data lewat modul baru `database.py`. Pertemuan 1 masih lewat terminal (skrip pembuat database dan uji aturan); **Pertemuan 2 memakai antarmuka Streamlit (`app.py`)** untuk CRUD, sehingga Minggu 7 dapat dipakai untuk pendalaman Streamlit.

**Catatan jalur Minggu 5:** kelas jalur Streamlit Minggu 5 sudah memasang Streamlit. Kelas jalur terminal perlu memasangnya sebelum Selasa; bila gagal, jalur cadangan `main.py` (terminal) memakai `database.py` yang sama persis. Lapisan database tidak bergantung pada tampilan.

**Acuan RPS minggu 6:** mahasiswa mampu membuat basis data SQLite dan melakukan operasi data dasar. Bahan kajian: SQLite, SQL DDL/DML, pembuatan tabel, koneksi Python, query berparameter, serta operasi CRUD dasar. Pengalaman belajar: membuat database dan tabel proyek, mengisi data awal, lalu menguji tambah, tampil, ubah, dan hapus data. Indikator: database dan tabel terbentuk; PK/FK sesuai rancangan; seluruh operasi CRUD berhasil dan data dapat dibaca kembali. Evaluasi: praktikum database dan CRUD.

## Capaian akhir minggu

Mahasiswa dapat:
1. Menjelaskan basis data sebagai “lemari arsip digital”: database = lemari, tabel = buku besar, baris = satu catatan, kolom = kolom formulir.
2. Menjelaskan ERD (entitas, atribut, relasi, kardinalitas, PK/FK) dari contoh di modul ini dan menerjemahkannya menjadi perintah SQL `CREATE TABLE` dengan tipe data, PRIMARY KEY, FOREIGN KEY, dan aturan isian (`CHECK`) yang benar.
3. Membuat file database SQLite (`.db`) dari skrip Python dan mengisi beberapa baris data awal sebagai contoh.
4. Menghubungkan Python ke SQLite (`sqlite3`) dan menjalankan operasi CRUD dasar dengan **query berparameter**, dikemas sebagai fungsi dalam modul `database.py`, lalu memanggilnya dari aplikasi Streamlit `app.py` (formulir, tombol, pesan, dan tabel).
5. Memverifikasi hasil: data tersimpan dapat dibaca kembali, perubahan terlihat, dan database menolak penghapusan yang akan merusak data terkait.

## Persiapan alat

- Cukup Python + VS Code dari Minggu 2. **Tidak perlu memasang program `sqlite3` terpisah** — di Windows program itu biasanya tidak tersedia. Semua SQL dijalankan lewat skrip Python (`sqlite3` sudah bawaan Python) dengan `executescript()`.
- **Streamlit untuk Pertemuan 2:** `python -m pip install streamlit` dipasang sebelum kelas (perlu internet). Kelas jalur Streamlit Minggu 5 sudah memilikinya.
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
| 85–90 | Rangkuman: tabel menyimpan data meski program ditutup; simpan file untuk pertemuan Selasa. Ingatkan memasang Streamlit sebelum Selasa. | `kasir.db` dan `buat_database.py` tersimpan di folder proyek. |

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

## Pertemuan 2 — Selasa: CRUD lewat aplikasi Streamlit (90 menit)

**Prasyarat:** Streamlit sudah terpasang sebelum kelas (`python -m pip install streamlit`). Dosen mengingatkan di akhir pertemuan Senin. Kelas yang belum bisa memasang memakai jalur cadangan menu terminal (`6.2/kode-dosen/main.py`) dengan `database.py` yang sama.

**Bahan awal yang dibagikan:** `6.2/kode-praktik/database.py` (lengkap kecuali `hapus_produk()`) dan `6.2/kode-praktik/app.py` (tampil dan tambah sudah jadi; ubah harga dan hapus diberi komentar `# LATIHAN E1/E2`). Kunci ada di `6.2/kode-dosen/`. Bahan awal dibuat hampir jadi agar 90 menit dipakai untuk memahami alur Streamlit–database, bukan mengetik ulang fungsi SQL.

| Menit | Kegiatan | Bukti/cek cepat |
|---|---|---|
| 0–10 | Ulas tabel Senin. Perkenalkan pembagian file: `app.py` (tampilan) → `database.py` (simpan); `logika_bisnis.py` Minggu 5 menyusul untuk perhitungan. | Mahasiswa bisa menyebut tugas tiap file. |
| 10–20 | Dosen menelusuri `database.py`: `buka_koneksi()` dengan `PRAGMA`, query berparameter `?`, `commit()`, `rowcount`, `try/finally`. Mengapa jangan menyusun query lewat rangkaian teks. | Mahasiswa menunjuk baris `?` dan `commit()`. |
| 20–35 | **Latihan D:** lengkapi `hapus_produk()` di `database.py`. | Fungsi mengembalikan `rowcount`; koneksi ditutup di `finally`. |
| 35–50 | Jalankan `python -m streamlit run app.py`. Jelaskan model *rerun* (seluruh skrip dijalankan ulang setiap tombol ditekan), `st.form`, `st.number_input(step=1)`, `st.success/warning/error`, dan mengapa tabel diletakkan paling bawah. Coba tambah produk. | Halaman Kelola Produk terbuka; produk baru tampil di tabel. |
| 50–70 | **Latihan E1/E2:** lengkapi bagian ubah harga dan hapus di `app.py`, termasuk konfirmasi `st.checkbox` dan penanganan `IntegrityError`. | Empat operasi CRUD berjalan dari halaman web. |
| 70–85 | Uji delapan skenario (tabel di bawah); catat hasil aktual dan satu perbaikan; uji penyimpanan dengan menghentikan dan menjalankan ulang aplikasi. | Tabel uji B4 terisi; data tetap ada setelah aplikasi dijalankan ulang. |
| 85–90 | Refleksi dan jembatan ke Minggu 7: `database.py` dipakai ulang; Minggu 7 menambah catat penjualan, laporan, pencarian, dan tata letak. | File kerja dan catatan pengujian tersimpan. |

**Contoh pola `database.py` (dibagikan; `hapus_produk()` dilengkapi mahasiswa):**

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

**Contoh pemanggilan dari `app.py` (bagian tambah produk, sudah jadi di bahan awal):**

```python
import sqlite3

import streamlit as st

import database

st.title("Kelola Produk")

st.subheader("Tambah produk")
with st.form("form_tambah", clear_on_submit=True):
    nama = st.text_input("Nama produk")
    harga = st.number_input("Harga (Rp, angka bulat)", step=1, value=0)
    stok = st.number_input("Stok awal", min_value=0, step=1, value=0)
    tombol_tambah = st.form_submit_button("Simpan produk")

if tombol_tambah:
    if nama.strip() == "":
        st.error("Nama produk wajib diisi.")          # validasi Python (lapis depan)
    else:
        try:
            database.tambah_produk(nama.strip(), harga, stok)
            st.success(f"Produk {nama.strip()} tersimpan.")
        except sqlite3.IntegrityError as e:
            st.error(f"Database menolak data: {e}")  # aturan database (lapis belakang)

# ... bagian ubah harga dan hapus (Latihan E1/E2) ...

st.subheader("Daftar produk")   # dibaca paling akhir agar selalu terbaru
st.dataframe(
    [
        {"ID": id_produk, "Nama": nama, "Harga": harga, "Stok": stok}
        for id_produk, nama, harga, stok in database.daftar_produk()
    ],
    hide_index=True,
)
```

Kolom harga sengaja **tanpa** `min_value` agar mahasiswa dapat membuktikan bahwa aturan `CHECK` di database tetap menjaga data. Kolom stok memakai `min_value=0` sebagai contoh validasi di tampilan.

**Tabel uji Selasa (delapan skenario):**

| No | Skenario | Langkah | Hasil yang diharapkan |
|---|---|---|---|
| 1 | Tambah normal | Tambah “Penghapus”, 2000, stok 15 | `st.success`; muncul di tabel dengan ID baru |
| 2 | Ubah harga | Ubah harga ID 2 (Pulpen) menjadi 3500 | `rowcount` = 1; harga baru tampil |
| 3 | Ubah ID yang tidak ada | Ubah harga ID 999 | `rowcount` = 0; `st.warning` “ID tidak ditemukan” |
| 4a | Hapus produk yang punya transaksi | Hapus ID 1 (Buku Tulis), konfirmasi dicentang | Ditolak `FOREIGN KEY constraint failed`; data utuh |
| 4b | Hapus produk tanpa transaksi | Hapus ID 3 (Map Plastik), konfirmasi dicentang | Berhasil; hilang dari tabel |
| 5 | Nama kosong | Tambah produk dengan nama kosong/spasi | Ditolak validasi Python: “Nama produk wajib diisi” |
| 6 | Harga negatif | Tambah produk dengan harga -5 | Ditolak `CHECK constraint failed`; aplikasi tetap berjalan |
| 7 | Hapus tanpa konfirmasi | Hapus ID 2 tanpa mencentang | `st.warning`; tidak ada data terhapus |

Data awal (diisi `buat_database.py`): Buku Tulis (ID 1, punya satu transaksi), Pulpen (ID 2), Map Plastik (ID 3). Skenario versi terminal (isian `abc` → `ValueError`) tidak dipakai lagi karena `st.number_input` tidak menerima teks; skenario 5 menggantikannya untuk melatih validasi Python.

Catatan praktik: gunakan selalu `?` (parameter) alih-alih menyisipkan nilai langsung ke string SQL; panggil `commit()` setelah `INSERT`/`UPDATE`/`DELETE`; tutup koneksi dengan `try/finally` (catatan: `with sqlite3.connect(...)` hanya mengurus commit, **tidak** menutup koneksi). Jalankan Streamlit dengan `python -m streamlit run app.py` agar tidak bergantung pada PATH Windows. Setelah mengedit kode, simpan lalu tekan **R** atau **Rerun** di browser.

**Dicadangkan untuk Minggu 7 (pendalaman Streamlit):** catat penjualan yang mengambil `harga_satuan` dari produk dan mengurangi stok dalam satu `commit`; laporan omzet per produk dengan `LEFT JOIN` dan `st.bar_chart`; pencarian produk dengan `LIKE ?`; tata letak `st.sidebar`/`st.tabs`; serta `st.session_state`.

## Luaran dan pemeriksaan

- **File:** `kasir.db` (atau `<nama_proyek>.db`) berisi minimal dua tabel berelasi sesuai ERD; `buat_database.py`; `database.py` berisi fungsi CRUD berparameter; `app.py` Streamlit yang memanggilnya (atau `main.py` untuk jalur cadangan terminal).
- **Bukti:** skrip yang bisa dijalankan, hasil `SELECT` sebelum/sesudah perubahan, hasil tiga uji pelanggaran Senin, tabel pengujian delapan skenario Selasa, dan tangkapan layar halaman Streamlit untuk skenario 1, 4a, dan 6.
- **Kriteria selesai:** tabel terbentuk dengan PK/FK/CHECK sesuai rancangan di lembar kerja Minggu 6; `PRAGMA foreign_keys = ON` aktif di setiap koneksi; data awal terisi; operasi CRUD berhasil dari aplikasi Streamlit dan data dapat dibaca kembali setelah aplikasi dijalankan ulang; penghapusan yang melanggar relasi ditolak; penghapusan tanpa konfirmasi tidak dijalankan; input salah ditangani dengan pesan tanpa membuat aplikasi berhenti.
- **Catatan pengajaran non-IT:** analogi lemari arsip/buku besar/nota, demonstrasi lebih dulu, skrip awal dibagikan agar waktu praktik dipakai untuk memahami bukan mengetik, gunakan data kecil (2–3 baris) agar mudah diperiksa manual, dan hindari istilah teknis tanpa contoh. Ingatkan untuk tidak menaruh data pribadi nyata — pakai data simulasi.

**Sumber internal:** `rps/matriks-rps-pemograman-bisnis-perancangan-sistem-administrasi-python-streamlit-vscode.csv` (baris minggu 6); `bahan-ajar/modul/minggu-03-perancangan-basis-data-relasional.md`; `Minggu ke-5/minggu-05-modul-praktik-fungsi-modul-error-handling.docx` dan versi Streamlit-nya; `pengajaran/jadwal/jadwal-mengajar-polines-2026-2027.csv`.
