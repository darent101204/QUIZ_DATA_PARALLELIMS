# 📊 Data Parallelism - Analisis Nilai Siswa (Multiprocessing Python)

## 📌 Deskripsi Proyek

Proyek ini merupakan implementasi konsep **Data Parallelism** menggunakan bahasa Python dengan modul `multiprocessing`. Program ini bertujuan untuk menganalisis dataset besar berupa nilai siswa secara paralel agar proses menjadi lebih cepat dan efisien.

Pada program ini, satu fungsi yang sama dijalankan pada banyak data secara bersamaan dengan membagi pekerjaan ke beberapa proses (process).

---

## 🎯 Tujuan

* Memahami konsep **Data Parallelism**
* Mengimplementasikan multiprocessing di Python
* Menganalisis data dalam jumlah besar secara paralel
* Membuktikan eksekusi paralel melalui Process ID (PID)

---

## ⚙️ Konsep yang Digunakan

### 🔹 Data Parallelism

Data Parallelism adalah teknik di mana:

* Satu fungsi yang sama dijalankan
* Pada banyak data yang berbeda
* Secara bersamaan (paralel)

Pada proyek ini:

* Fungsi: `analyze_score()`
* Data: nilai siswa (150 data)
* Eksekusi: paralel menggunakan multiprocessing

---

## 🧠 Cara Kerja Program

1. Program membuat dataset berisi 150 nilai siswa secara acak
2. Program membuat beberapa process menggunakan `multiprocessing.Pool`
3. Setiap process mengambil satu data nilai
4. Fungsi `analyze_score()` dijalankan secara paralel
5. Setiap nilai dianalisis untuk menentukan:

   * Grade (A, B, C, D)
   * Status (LULUS / TIDAK LULUS)
6. Hasil dikumpulkan dan ditampilkan

---

## 🧩 Penjelasan Fungsi

### `analyze_score(score)`

Fungsi ini dijalankan oleh setiap process untuk menganalisis satu nilai siswa.

Langkah yang dilakukan:

* Mengambil Process ID (PID)
* Menampilkan proses mulai
* Mensimulasikan proses dengan `sleep`
* Menentukan grade
* Menentukan status kelulusan
* Mengembalikan hasil analisis

---

## 💻 Contoh Output

```
[Process 1234] START score: 80
[Process 5678] START score: 45
[Process 1234] DONE score: 80
[Process 5678] DONE score: 45
```

Hasil akhir:

```
{'score': 80, 'grade': 'B', 'status': 'LULUS'}
{'score': 45, 'grade': 'D', 'status': 'TIDAK LULUS'}
```

---

## 🔍 Analisis Output

* Output tidak berurutan → menunjukkan eksekusi paralel
* Process ID (PID) berbeda → menunjukkan banyak process berjalan
* Semua process menjalankan fungsi yang sama dengan data berbeda

---

## 🚀 Cara Menjalankan Program

1. Pastikan Python sudah terinstall
2. Jalankan file dengan perintah:

```
python nama_file.py
```

---

## 📦 Teknologi yang Digunakan

* Python 3
* multiprocessing
* os
* time
* random

---

## 📌 Kesimpulan

Program ini berhasil mengimplementasikan **Data Parallelism** dengan membagi dataset ke beberapa process yang berjalan secara bersamaan. Pendekatan ini meningkatkan efisiensi dalam pengolahan data dalam jumlah besar.

---

## 👨‍💻 Author

* Nama: (Isi Nama Kamu)
* NRP: (Isi NRP Kamu)

---

## 📎 Catatan

Output program menunjukkan PID yang berbeda dan urutan eksekusi yang tidak berurutan, yang membuktikan bahwa proses berjalan secara paralel.

---
