import sqlite3

import streamlit as st

import database

st.title("Kelola Produk")
st.caption("Data tersimpan di kasir.db dan tetap ada walau aplikasi ditutup.")

# ---------- CREATE: tambah produk (CONTOH SUDAH JADI) ----------
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

# ---------- UPDATE: ubah harga (LATIHAN E1) ----------
st.subheader("Ubah harga")
with st.form("form_ubah"):
    id_ubah = st.number_input("ID produk", min_value=1, step=1)
    harga_baru = st.number_input("Harga baru (Rp)", step=1, value=0)
    tombol_ubah = st.form_submit_button("Ubah harga")

if tombol_ubah:
    # LATIHAN E1: ganti baris st.info di bawah dengan:
    # - try: panggil database.ubah_harga(id_ubah, harga_baru)
    #   * hasil 0  -> st.warning("ID ... tidak ditemukan.")
    #   * selainnya -> st.success("Harga ... diubah ...")
    # - except sqlite3.IntegrityError as e: st.error(...)
    st.info("Fitur ubah harga belum dilengkapi.")

# ---------- DELETE: hapus produk (LATIHAN E2) ----------
st.subheader("Hapus produk")
with st.form("form_hapus"):
    id_hapus = st.number_input("ID produk yang dihapus", min_value=1, step=1)
    yakin = st.checkbox("Saya yakin ingin menghapus produk ini")
    tombol_hapus = st.form_submit_button("Hapus")

if tombol_hapus:
    # LATIHAN E2: ganti baris st.info di bawah dengan:
    # - jika kotak "yakin" belum dicentang -> st.warning, JANGAN hapus apa pun
    # - jika sudah dicentang -> panggil database.hapus_produk(id_hapus)
    #   * hasil 0  -> st.warning("ID ... tidak ditemukan.")
    #   * selainnya -> st.success("Produk ... dihapus.")
    # - tangkap sqlite3.IntegrityError: produk masih dirujuk transaksi
    st.info("Fitur hapus belum dilengkapi.")

# ---------- READ: daftar produk (CONTOH SUDAH JADI) ----------
# Dibaca paling akhir agar tabel selalu menampilkan hasil perubahan di atas.
st.subheader("Daftar produk")
st.dataframe(
    [
        {"ID": id_produk, "Nama": nama, "Harga": harga, "Stok": stok}
        for id_produk, nama, harga, stok in database.daftar_produk()
    ],
    hide_index=True,
)
