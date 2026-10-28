
# ============================================================
# MODUL INPUT DATA
# Rekap dan Analisis Nilai Matematika
# ============================================================

from pathlib import Path
from math import isfinite


def baca_data(lokasi_file):
    """Membaca dan memvalidasi data nilai dari file teks."""
    lokasi_file = Path(lokasi_file)
    daftar_nilai = []

    try:
        with lokasi_file.open("r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                teks = baris.strip()

                if not teks:
                    continue

                try:
                    nilai = float(teks)
                except ValueError:
                    print(
                        f"  [!] Baris {nomor}: "
                        "data bukan angka, dilewati."
                    )
                    continue

                if not isfinite(nilai):
                    print(
                        f"  [!] Baris {nomor}: "
                        "nilai harus berupa angka yang valid."
                    )
                    continue

                if not 0 <= nilai <= 100:
                    print(
                        f"  [!] Baris {nomor}: "
                        "nilai harus berada pada rentang 0–100."
                    )
                    continue

                daftar_nilai.append(nilai)

    except FileNotFoundError:
        print(f"\n  [!] File tidak ditemukan: {lokasi_file}")
    except OSError as error:
        print(f"\n  [!] File tidak dapat dibaca: {error}")

    return daftar_nilai