# ai-tugas5-F1D02410095

## Nama : Siti Ananda Rahma
## NIM : F1D02410095

## Topik : Sistem Pakar Rekomendasi Metode Belajar
Program akan memberikan tujuh pertanyaan dengan jawaban Ya/Tidak mengenai tujuan belajar, karakteristik materi, latihan mengingat, pemantauan pemahaman, dan pengelolaan waktu/sumber belajar. Jawaban Ya akan menjadi fakta awal yang diproses menggunakan aturan yang terdapat pada `kb_belajar.json`.
    **Bahasa:** Python
    **Versi:** Python 3.8
    **Perintah:** contoh : python rekomendasi_belajar.py.


## Cara Menjalankan
1. Memastikan Python telah terpasang dan melakukan install jika Python belum terpasang.
2. Membuat file  `kb_belajar.json` dan `rekomendasi_belajar.py` di folder yang sama.
3. Setelah kode selesai, buka terminal.
4. Kemudian jalankan: `python rekomendasi_belajar.py`
5. Jawab setiap pertanyaan dengan `y` untuk Ya atau `t` untuk Tidak.


## Daftar Sumber
Sumber 1
Judul : Practicing Retrieval Facilitates Learning
Penerbit : Annual Reviews (Annual Review of Psychology, Volume 72)
URL : https://www.annualreviews.org/content/journals/10.1146/annurev-psych-010419-051019
Tanggal akses : 13 November 2026

Sumber 2
Judul : Efektivitas Peningkatan Memori pada Siswa
Penerbit : Fakultas Psikologi, Universitas Islam Negeri Sultan Syarif Kasim Riau (Psikobuletin: Buletin Ilmiah Psikologi)
URL : https://old-ejournal.uin-suska.ac.id/index.php/Psikobuletin/article/view/26438
Tanggal akses : 13 November 2026

Sumber 3
Judul : Strategi Pembelajaran dan Implikasinya pada Peningkatan Efektivitas Pembelajaran
Penerbit : Pustekkom, Departemen Pendidikan Nasional (Jurnal Teknodik, Volume 13, Nomor 1)
URL : https://jurnalteknodik.kemendikdasmen.go.id/index.php/jurnalteknodik/id/article/view/440
Tanggal akses : 13 November 2026

Sumber 4
Judul : Metacognition, Achievement Goals, Study Strategies and Academic Achievement: Pathways to Achievement
Penerbit : Springer Nature (Metacognition and Learning, Volume 3, Nomor 2)
URL : https://link.springer.com/article/10.1007/s11409-008-9022-4
Tanggal akses : 13 November 2026


## Tabel Aturan
Aturan-aturan yang terdapat dalam `kb_belajar.json`, dimana mode **dan** artinya seluruh syarat harus terpenuhi, sedangkan **atau** artinya minimal terdapat satu syarat yang terpenuhi.

| ID | Kondisi (JIKA) | Mode | Kesimpulan (MAKA) | Sumber |
|---|---|---|---|---|
| R1 | Tujuan mengingat materi; materi berupa tulisan | DAN | Metode Mnemonic | S2 |
| R2 | Tujuan mengingat materi; membutuhkan latihan mengingat | DAN | Retrieval Practice | S1 |
| R3 | Materi visual | DAN | Representasi Visual | S2 |
| R4 | Ingin memantau pemahaman | DAN | Metakognitif | S4 |
| R5 | Waktu belajar terbatas; perlu mengatur sumber belajar | DAN | Pengelolaan Sumber Daya Belajar | S3 |
| R6 | Retrieval Practice; Metakognitif | DAN | Retrieval Practice dengan Monitoring | S1 |
| R7 | Waktu belajar terbatas; perlu mengatur sumber belajar | ATAU | Pengelolaan Sumber Daya Belajar | S3 |


## Metode yang dipilih
Metode yang digunakan yaitu metode Forward Chaining (FC), dimana merupakan penalaran yang dimulai dari fakta awal yang didapatkan atau di ambil berdasarkan jawaban Ya dari pengguna yang kemudian sistem akan mencari aturan yang kondisinya terpenuhi untuk dapat menghasilkan kesimpulan baru. Fakta baru juga dapat menjadi syarat bagi aturan berikutnya. Proses akan berhenti saat tidak ada aturan baru yang dapat dijalankan.


## Alasan Pemilihan
Mekanisme kerja sistem yaitu sistem akan memperoleh informasi dari setiap jawaban pengguna terlebih dahulu, kemudian menentukan kesimpulan yang dapat diambil dari fakta yang ada. Sehingga pendekatan berbasis FC ini sesuai untuk menghasilkan rekomendasi untuk topik yang diambil.


## Contoh perhitungan/penelusuran manual:
Contoh jawaban Ya sebagai fakta awal:
- `tujuan mengingat materi`
- `membutuhkan latihan mengingat`
- `materi visual`
- `ingin memantau pemahaman`

Penelusuran:
- R2: `tujuan mengingat materi` DAN `membutuhkan latihan mengingat` → **retrieval practice**.
- R3: `materi visual` → **representasi visual**.
- R4: `ingin memantau pemahaman` → **metakognitif**.
- R6: `retrieval practice` DAN `metakognitif` → **retrieval practice dengan monitoring**.

Tidak ada aturan baru yang dapat dijalankan setelah itu. Kesimpulan akhir yang ditampilkan adalah **Representasi Visual** dan **Retrieval Practice dengan Monitoring**. `Retrieval Practice` dan `Metakognitif` menjadi fakta yang dipakai untuk membentuk kesimpulan R6.


## Kasus Uji dan Screenshot
### Kasus Uji 1 — Mnemonic dan Retrieval Practice
**Input :** Ya untuk tujuan mengingat materi, materi berupa tulisan, dan kebutuhan latihan mengingat. Jawaban pertanyaan lainnya Tidak.

**Hasil :** R1 dan R2 aktif. Program merekomendasikan Metode Mnemonic dan Retrieval Practice.

![Screenshot Kasus Uji 1](screenshot/kasus%201.png)


### Kasus Uji 2 — Representasi Visual dan Retrieval Practice dengan Monitoring
**Input :** Ya untuk tujuan mengingat materi, kebutuhan latihan mengingat, materi visual, dan keinginan memantau pemahaman. Jawaban pertanyaan lainnya Tidak.

**Hasil :** R2, R3, R4, dan R6 aktif. Kesimpulan akhir adalah Representasi Visual dan Retrieval Practice dengan Monitoring.

![Screenshot Kasus Uji 2](screenshot/kasus%202.png)


### Kasus Uji 3 — Tidak ada rekomendasi
**Input :** Hanya pertanyaan tujuan mengingat materi dijawab Ya, enam pertanyaan lainnya Tidak.

**Hasil :** Tidak ada aturan yang terpenuhi, sehingga program menampilkan “Tidak ada rekomendasi metode belajar”.

![Screenshot Kasus Uji 3](screenshot/kasus%203%20tidak%20ada%20kesimpulan.png)


## Batas Keberlakuan
Pengetahuan atau hasil sistem disusun berdasarkan empat artikel yang tercantum pada daftar sumber, yaitu terdapat pengetahuan tentang retrieval practice, peningkatan memori, strategi pembelajaran, serta metakognisi dan strategi belajar. Aturan digunakan untuk memberi rekomendasi awal kepada pengguna yang sedang bingung memilih metode belajar berdasarkan tujuan mengingat materi, bentuk materi, kebutuhan latihan, pemantauan pemahaman, dan pengelolaan waktu atau sumber pembelajaran. Rekomendasi terbatas pada fakta dan aturan yang dimasukkan ke basis pengetahuan, sistem belum mempertimbangkan seluruh faktor pribadi maupun situasi belajar setiap pengguna. Oleh karena itu, hasil program merupakan **saran awal dan bukan keputusan akhir**. Pengguna juga tetap harus menilai kesesuaian rekomendasi yang di dapatkan dengan kebutuhan sendiri.


## Penggunaan Alat Bantu AI
Digunakan dalam kode, membantu memahami algoritma Forward Chaining yang di implementasikan ke dalam kode dan membantu merapikan dokumentasi pada README agar tiap judul utama sebagai heading dan anakannya sebagai subheading sehingga terlihat rapi dan mudah di pahami.
