
# ============================================================
# NAMA  : Azkiah Safira
# NIM   : 2225250013
# KELAS : 3F
# ============================================================
# PROYEK : Rekap dan Analisis Nilai Matematika
# PERTEMUAN 15 - IMPLEMENTASI, PENGUJIAN, DAN DOKUMENTASI
# ============================================================

from pathlib import Path

from src.input_data import baca_data
from src.proses import analisis_nilai
from src.output import tampilkan_laporan, simpan_laporan


BASE_DIR = Path(__file__).resolve().parent
FILE_INPUT = BASE_DIR / "data" / "contoh_data.txt"
FILE_OUTPUT = BASE_DIR / "output" / "laporan_nilai.txt"
KKM = 75


def main():
    """Menjalankan alur utama program."""
    print("\n" + "=" * 58)
    print("       REKAP DAN ANALISIS NILAI MATEMATIKA")
    print("=" * 58)
    print("  Sistem pengolahan nilai siswa")
    print("-" * 58)

    daftar_nilai = baca_data(FILE_INPUT)

    if not daftar_nilai:
        print("\n  [!] Data nilai tidak tersedia atau tidak valid.")
        print("=" * 58)
        return

    hasil = analisis_nilai(daftar_nilai, KKM)
    tampilkan_laporan(hasil)

    if simpan_laporan(hasil, FILE_OUTPUT):
        print("\n  [OK] Laporan berhasil disimpan.")
        print(f"  Lokasi: {FILE_OUTPUT.relative_to(BASE_DIR)}")
    else:
        print("\n  [!] Laporan gagal disimpan.")

    print("=" * 58)
    print("  Proses analisis selesai.")
    print("=" * 58 + "\n")


if __name__ == "__main__":
    main()