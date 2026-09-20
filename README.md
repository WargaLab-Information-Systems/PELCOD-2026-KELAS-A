# PELCOD-2026-KELAS-A

# Git & GitHub — Clone to Push

Panduan singkat untuk mengambil (**clone**) repository dari GitHub, melakukan perubahan pada project, kemudian meng-upload (**push**) perubahan tersebut kembali ke GitHub.

## 1. Clone Repository

### A. Copy URL Repository

1. Buka repository yang ingin digunakan di GitHub.
2. Klik tombol **Code**.
3. Pilih **HTTPS**.
4. Copy URL repository.

Contoh:

```bash
https://github.com/username/nama-repository.git
```

### B. Clone ke Komputer

Buka **Git Bash** pada folder tempat project ingin disimpan, kemudian jalankan:

```bash
git clone https://github.com/username/nama-repository.git
```

Masuk ke folder repository:

```bash
cd nama-repository
```

---

## 2. Membuat atau Mengubah File

Setelah repository berhasil di-clone, buat file baru atau lakukan perubahan pada project.

Contoh:

```text
nama-repository/
├── README.md
├── index.php
├── style.css
└── script.js
```

---

## 3. Git Add

Tambahkan file yang ingin di-upload:

```bash
git add nama-file
```

Contoh:

```bash
git add index.php
```

Jika ingin menambahkan **semua file yang berubah**:

```bash
git add .
```

---

## 4. Cek Status

Sebelum melakukan upload, cek perubahan menggunakan:

```bash
git status
```

Perintah ini digunakan untuk melihat file yang mengalami perubahan atau file baru yang belum dimasukkan ke staging area.

---

## 5. Git Commit

Setelah melakukan `git add`, buat commit dengan pesan yang menjelaskan perubahan:

```bash
git commit -m "pesan commit"
```

Contoh:

```bash
git commit -m "Menambahkan halaman login"
```

Commit merupakan rekaman perubahan pada repository pada suatu titik waktu tertentu.

---

## 6. Git Push

Setelah commit selesai, upload perubahan ke repository GitHub menggunakan:

```bash
git push
```

Jika diminta menentukan branch:

```bash
git push origin main
```

Setelah berhasil, perubahan yang sebelumnya ada di komputer lokal akan dikirim ke repository GitHub.

---

# Alur Singkat

```text
GitHub Repository
       │
       │ git clone
       ▼
Folder Lokal
       │
       │ Membuat / mengubah file
       ▼
   git status
       │
       │ git add .
       ▼
   Staging Area
       │
       │ git commit -m "..."
       ▼
   Git Lokal
       │
       │ git push
       ▼
GitHub Repository
```

## Perintah Utama

```bash
# Clone repository
git clone https://github.com/username/nama-repository.git

# Masuk ke folder
cd nama-repository

# Cek perubahan
git status

# Tambahkan perubahan
git add .

# Commit perubahan
git commit -m "Menambahkan perubahan"

# Push ke GitHub
git push
```

## Jika Ada Perubahan dari Teman

Jika repository sudah mengalami perubahan dari anggota tim lain, gunakan:

```bash
git pull
```

`git pull` digunakan untuk mengambil dan menyinkronkan perubahan dari repository GitHub ke folder project lokal.

Alur kerja bersama dapat dilakukan seperti berikut:

```bash
git pull
git add .
git commit -m "Pesan perubahan"
git push
```

> **Tips:** Biasakan menjalankan `git pull` sebelum mulai mengerjakan project bersama agar repository lokal mendapatkan perubahan terbaru dari anggota tim.
