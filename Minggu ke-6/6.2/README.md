# Bahan Pertemuan 6.2 — CRUD lewat Aplikasi Streamlit

| File | Kegunaan |
|---|---|
| [Slide](minggu-06-pertemuan-2-slide-crud-streamlit.pptx) | Slide 18 halaman untuk pertemuan Selasa. |
| [Lembar kerja Word](minggu-06-pertemuan-2-lembar-kerja-crud-streamlit.docx) · [PDF](minggu-06-pertemuan-2-lembar-kerja-crud-streamlit.pdf) | Persiapan Selasa dan Bagian B (B1–B5). |
| [kode-praktik/database.py](kode-praktik/database.py) | Bahan awal mahasiswa: koneksi dan CRUD produk; `hapus_produk()` dilengkapi pada Latihan D. |
| [kode-praktik/app.py](kode-praktik/app.py) | Bahan awal mahasiswa: tampil dan tambah sudah jadi; ubah harga (E1) dan hapus (E2) dilengkapi. |

Kunci jawaban dan jalur cadangan menu terminal (`main.py`) disediakan oleh dosen secara terpisah.

## Cara memakai

1. Salin `database.py` dan `app.py` dari `kode-praktik` ke folder kerja `minggu-06`, satu folder dengan `kasir.db` hasil pertemuan Senin. Jika `kasir.db` belum ada, jalankan dulu `buat_database.py` dari [`../kode-praktik`](../kode-praktik).
2. Pasang Streamlit satu kali (jika belum):

```bash
python -m pip install streamlit
```

3. Jalankan aplikasi:

```bash
python -m streamlit run app.py
```

Panduan lengkap, latihan, dan skenario uji ada di [README Minggu 6](../README.md) bagian 6–10.
