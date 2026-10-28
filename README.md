# Pertemuan 15 — Implementasi, Pengujian, dan Dokumentasi Proyek
Nama: Azkiah Safira  
NIM: 2225250013  
Kelas: 3F

## Deskripsi Proyek
Program Rekap dan Analisis Nilai Matematika Kelas merupakan implementasi program sederhana untuk membantu guru mengelola dan menganalisis nilai matematika siswa secara terstruktur. Program dikembangkan berdasarkan rancangan pada Pertemuan 14 dengan menerapkan pembacaan dan validasi data, perhitungan statistik, penentuan ketuntasan berdasarkan Kriteria Ketuntasan Minimal (KKM), serta penyimpanan hasil analisis dalam bentuk laporan teks.

## Tujuan
1. Mengimplementasikan rancangan proyek menjadi program Python yang dapat dijalankan.
2. Menerapkan modularisasi program melalui pemisahan fungsi berdasarkan tanggung jawabnya.
3. Memvalidasi data nilai untuk menangani input yang tidak valid.
4. Menghitung statistik nilai dan menentukan ketuntasan siswa berdasarkan KKM.
5. Melakukan pengujian terhadap kondisi normal, batas, data tidak valid, data kosong, dan file yang tidak tersedia.
6. Mengidentifikasi dan memperbaiki kesalahan program berdasarkan hasil pengujian.
7. Melengkapi dokumentasi proyek serta mengelola perubahan kode menggunakan Git dan GitHub.

## Fitur Proyek
1. Membaca data nilai siswa dari file teks.
2. Memvalidasi nilai agar berada dalam rentang 0–100.
3. Melewati data kosong dan data yang tidak sesuai format dengan memberikan peringatan jika diperlukan.
4. Menghitung jumlah data, total nilai, rata-rata, nilai minimum, dan nilai maksimum.
5. Menghitung jumlah siswa tuntas dan belum tuntas berdasarkan KKM.
6. Menampilkan ringkasan hasil analisis melalui terminal.
7. Menyimpan hasil analisis ke dalam file laporan teks.
8. Menangani kesalahan seperti file tidak ditemukan dan data nilai kosong.

## Struktur Folder
```text
pertemuan 15 implementasi proyek/
├── README.md
├── .gitignore
├── main.py
├── src/
│   ├── __init__.py
│   ├── input_data.py
│   ├── proses.py
│   └── output.py
├── data/
│   └── contoh_data.txt
├── tests/
│   └── test_case.md
└── docs/
    └── screenshot/
```

## Kebutuhan Sistem
- Python 3
- Visual Studio Code
- Git
- Akun GitHub

## Spesifikasi Input, Proses, dan Output
| Komponen | Keterangan |
|---|---|
| Input | Data nilai siswa dari file `data/contoh_data.txt` |
| Proses | Membaca dan memvalidasi data, menghitung statistik nilai, serta menentukan ketuntasan berdasarkan KKM |
| Output | Ringkasan hasil analisis di terminal dan laporan teks pada `output/laporan_nilai.txt` |

## Implementasi Struktur Program
| File | Tanggung Jawab |
|---|---|
| `main.py` | Mengatur alur utama program dan menghubungkan setiap modul |
| `src/__init__.py` | Menandai folder `src` sebagai paket Python |
| `src/input_data.py` | Membaca dan memvalidasi data nilai dari file |
| `src/proses.py` | Menghitung statistik nilai dan ketuntasan siswa |
| `src/output.py` | Menampilkan dan menyimpan laporan hasil analisis |
| `data/contoh_data.txt` | Menyimpan data nilai siswa untuk diolah |
| `tests/test_case.md` | Mendokumentasikan skenario dan hasil pengujian |
| `docs/screenshot/` | Menyimpan tangkapan layar hasil implementasi dan pengujian |
| `.gitignore` | Menentukan file dan folder yang tidak perlu dilacak Git |

## Pengujian Program
Pengujian dilakukan untuk memeriksa kesesuaian hasil program dengan hasil yang diharapkan. Skenario pengujian didokumentasikan dalam `tests/test_case.md`.
| ID | Kondisi Pengujian | Expected Result |
|---|---|---|
| TC01 | Nilai 70, 80, 90 | Rata-rata 80 |
| TC02 | Nilai sama dengan KKM, yaitu 75 | Dihitung sebagai nilai tuntas |
| TC03 | Terdapat data berupa teks, seperti `abc` | Data dilewati dan peringatan ditampilkan |
| TC04 | File data kosong | Program tidak mengalami pembagian dengan nol |
| TC05 | File tidak ditemukan | Program menampilkan pesan kesalahan yang jelas |
| TC06 | Nilai di luar rentang 0–100 | Nilai ditolak dan peringatan ditampilkan |
| TC07 | Data nilai valid | Laporan hasil analisis berhasil disimpan |
Hasil aktual dan status pengujian diisi setelah setiap skenario dijalankan. Pengujian dinyatakan lulus apabila hasil aktual sesuai dengan hasil yang diharapkan.

## Penanganan Bug
Perbaikan program difokuskan pada beberapa kondisi yang berpotensi menyebabkan kesalahan, yaitu:
1. Data kosong yang dapat menyebabkan pembagian dengan nol.
2. Data nonnumerik yang tidak dapat dikonversi menjadi angka.
3. Nilai yang berada di luar rentang 0–100.
4. File input yang tidak ditemukan atau tidak dapat dibaca.
5. Folder output yang belum tersedia ketika laporan akan disimpan.

Setelah perbaikan dilakukan, pengujian ulang diperlukan untuk memastikan bahwa program berjalan sesuai dengan rancangan.

## Cara Menjalankan
1. Buka folder proyek melalui Visual Studio Code.
2. Pastikan Python 3 telah terpasang.
3. Periksa data pada file `data/contoh_data.txt`.
4. Buka terminal pada direktori utama proyek.
5. Jalankan perintah berikut:

```bash
python main.py
```
Program akan membaca data nilai, melakukan analisis, menampilkan laporan di terminal, dan menyimpan laporan ke `output/laporan_nilai.txt`.
Folder `output` dibuat secara otomatis ketika laporan disimpan. Jika folder tersebut belum tersedia sebelumnya, folder akan terbentuk saat program dijalankan dengan data yang valid.

## Dokumentasi dan GitHub
Dokumentasi proyek mencakup README, skenario pengujian, serta tangkapan layar hasil implementasi. Perubahan program dikelola menggunakan Git melalui commit yang menggambarkan tahapan pengembangan, pengujian, dan penyelesaian dokumentasi.

Proyek kemudian diunggah ke repositori GitHub agar kode program, dokumentasi, dan riwayat perubahan dapat diperiksa kembali.

## Rencana Milestone
1. Pertemuan 14: menyelesaikan rancangan proyek, algoritma, struktur folder, dan test case awal.
2. Antara Pertemuan 14–15: mengembangkan fitur utama berdasarkan rancangan.
3. Pertemuan 15: mengintegrasikan modul, menjalankan pengujian, memperbaiki bug, dan melengkapi dokumentasi proyek.
4. Pertemuan 16: mempersiapkan demonstrasi dan presentasi hasil proyek.

## Refleksi
Melalui implementasi proyek ini, saya mempelajari proses mengembangkan rancangan menjadi program Python yang dapat dijalankan. Pemisahan program ke dalam beberapa modul membantu membuat kode lebih terstruktur dan mudah dipelihara. Pengujian pada berbagai kondisi input juga membantu menemukan potensi kesalahan dan memastikan hasil program sesuai dengan yang diharapkan. Selain itu, dokumentasi serta penggunaan Git dan GitHub membantu menjaga keteraturan pengembangan dan memudahkan evaluasi proyek.
