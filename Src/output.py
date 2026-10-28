
# ============================================================
# MODUL OUTPUT LAPORAN
# Rekap dan Analisis Nilai Matematika
# ============================================================

from pathlib import Path
from datetime import datetime


GARIS = "=" * 58


def buat_laporan(hasil):
    """Menyusun hasil analisis menjadi laporan teks."""

    tertinggi = hasil["nilai_tertinggi"]
    terendah = hasil["nilai_terendah"]

    tertinggi = "-" if tertinggi is None else f"{tertinggi:g}"
    terendah = "-" if terendah is None else f"{terendah:g}"

    return (
        f"{GARIS}\n"
        "             LAPORAN ANALISIS NILAI\n"
        "                 MATEMATIKA KELAS\n"
        f"{GARIS}\n"
        f"Tanggal laporan       : {datetime.now():%d-%m-%Y %H:%M}\n"
        f"{'-' * 58}\n"
        f"Jumlah data           : {hasil['jumlah_data']}\n"
        f"Total nilai           : {hasil['total_nilai']:g}\n"
        f"Rata-rata nilai       : {hasil['rata_rata']:.2f}\n"
        f"Nilai tertinggi       : {tertinggi}\n"
        f"Nilai terendah        : {terendah}\n"
        f"{'-' * 58}\n"
        f"KKM                   : {hasil['kkm']}\n"
        f"Jumlah siswa tuntas   : {hasil['jumlah_tuntas']}\n"
        f"Jumlah belum tuntas   : {hasil['jumlah_belum_tuntas']}\n"
        f"{GARIS}\n"
    )


def tampilkan_laporan(hasil):
    """Menampilkan laporan ke terminal."""
    print()
    print(buat_laporan(hasil))


def simpan_laporan(hasil, lokasi_file):
    """Menyimpan laporan dan membuat folder jika belum tersedia."""
    lokasi_file = Path(lokasi_file)

    try:
        lokasi_file.parent.mkdir(parents=True, exist_ok=True)
        lokasi_file.write_text(
            buat_laporan(hasil),
            encoding="utf-8",
        )
        return True

    except OSError as error:
        print(f"  [!] Terjadi kesalahan saat menyimpan laporan: {error}")
        return False