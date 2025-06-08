# API Pengelola Pengalaman Kerja

API sederhana yang dibuat dengan Flask untuk mengelola data pengalaman kerja.  
Mendukung operasi CRUD: membuat, membaca, memperbarui, dan menghapus data pengalaman kerja.

---

## Fitur

- Menambah pengalaman kerja baru (`POST /experiences`)
- Melihat semua pengalaman kerja (`GET /experiences`)
- Memperbarui pengalaman kerja berdasarkan ID (`PUT /experiences/<id>`)
- Menghapus pengalaman kerja berdasarkan ID (`DELETE /experiences/<id>`)

---

## Instalasi

1. Clone repo ini
   ```bash
   git clone git@github.com:Flaming-hell/Pengalaman-api.git
   cd pengalaman-api

2. Buat virtual environment dan aktifkan

python3 -m venv venv
source venv/bin/activate


3. Install dependencies

pip install flask




---

## Menjalankan aplikasi

python app.py

Aplikasi akan berjalan di http://localhost:5000


---

## Contoh Request API

GET semua pengalaman kerja

curl http://localhost:5000/experiences

POST pengalaman kerja baru

curl -X POST http://localhost:5000/experiences \
     -H "Content-Type: application/json" \
     -d '{"title":"Programmer","company":"ABC Corp","years":2}'

PUT update pengalaman kerja

curl -X PUT http://localhost:5000/experiences/1 \
     -H "Content-Type: application/json" \
     -d '{"title":"Senior Programmer","years":3}'

DELETE pengalaman kerja

curl -X DELETE http://localhost:5000/experiences/1



---


## Lisensi

Proyek ini menggunakan lisensi MIT. Silakan gunakan dan modifikasi sesuai kebutuhan.


---

## Kontak

Jika ada pertanyaan atau ingin berkontribusi, silakan hubungi:
nama@example.com

---
