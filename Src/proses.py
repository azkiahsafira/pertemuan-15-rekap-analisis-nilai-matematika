
# ============================================================
# MODUL PROSES DAN ANALISIS
# Rekap dan Analisis Nilai Matematika
# ============================================================


def analisis_nilai(daftar_nilai, kkm=75):
    """Menghasilkan statistik dan rekap ketuntasan nilai."""

    jumlah_data = len(daftar_nilai)
    total_nilai = sum(daftar_nilai)

    if jumlah_data == 0:
        return {
            "jumlah_data": 0,
            "total_nilai": 0,
            "rata_rata": 0,
            "nilai_tertinggi": None,
            "nilai_terendah": None,
            "jumlah_tuntas": 0,
            "jumlah_belum_tuntas": 0,
            "kkm": kkm,
        }

    jumlah_tuntas = sum(nilai >= kkm for nilai in daftar_nilai)

    return {
        "jumlah_data": jumlah_data,
        "total_nilai": total_nilai,
        "rata_rata": total_nilai / jumlah_data,
        "nilai_tertinggi": max(daftar_nilai),
        "nilai_terendah": min(daftar_nilai),
        "jumlah_tuntas": jumlah_tuntas,
        "jumlah_belum_tuntas": jumlah_data - jumlah_tuntas,
        "kkm": kkm,
    }