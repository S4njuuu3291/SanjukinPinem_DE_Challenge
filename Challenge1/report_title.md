# Perencanaan Anotasi Dataset untuk Deteksi PPE

## 1. Skema Labeling

Pada proyek ini, sistem deteksi bertujuan untuk mengenali penggunaan lima atribut Personal Protective Equipment (PPE) wajib dalam lingkungan kerja. Selain atribut PPE, saya juga menambahkan label **people** untuk mendeteksi individu/pekerja. Berikut adalah daftar label dan definisinya:

| Label              | Definisi                                                                                    |
| ------------------ | ------------------------------------------------------------------------------------------- |
| **people**         | Deteksi individu/pekerja di area kerja                                                      |
| **hard_hat**       | Helm pengaman yang melindungi kepala dari benturan atau benda jatuh                         |
| **safety_vest**    | Rompi keselamatan berwarna mencolok agar pekerja mudah terlihat                             |
| **gloves**         | Sarung tangan pelindung untuk mengurangi risiko cedera, panas, atau paparan bahan berbahaya |
| **safety_glasses** | Kacamata pelindung untuk mencegah debu, serpihan, atau bahan kimia masuk ke mata            |
| **steel_toe_boot** | Sepatu boot dengan pelindung baja yang melindungi kaki dari benda keras, berat, atau tajam  |

---

## 2. Pertimbangan Skema Labeling

- **Enam label ini dipilih agar sistem dapat mendeteksi tidak hanya atribut PPE yang dipakai, tapi juga mengasosiasikan setiap atribut dengan individu/pekerja yang ada dalam gambar.**
- Label **people** berfungsi sebagai anchor/rujukan agar pada tahap post-processing, deteksi pelanggaran PPE bisa dilakukan dengan mengecek apakah setiap orang di gambar sudah memakai atribut wajibnya.
- Lima label utama (`hard_hat`, `safety_vest`, `gloves`, `safety_glasses`, `steel_toe_boot`) adalah atribut yang memang diwajibkan dan harus selalu dicek kepatuhannya pada setiap pekerja.
- Dengan skema ini, sistem lebih mudah melakukan verifikasi, misal: apakah seorang pekerja sudah memakai helm atau belum, dan tidak sekadar mendeteksi ada helm di frame.
- Skema labeling ini juga lebih efisien dan sesuai praktik di berbagai dataset PPE open-source yang umum digunakan.

---

## 3. Panduan Anotasi

Panduan ini bertujuan untuk menjaga konsistensi dan kualitas hasil anotasi:

### A. Kriteria Inclusion (Layak Diberi Label)

- **Objek jelas & relevan**
  Anotasi hanya diberikan pada objek yang termasuk dalam daftar label di atas dan dapat diidentifikasi secara visual.

- **Ukuran mencukupi**
  Bounding box minimal mencakup 5% area gambar agar objek cukup informatif untuk model.

- **Orientasi beragam**
  Objek tetap layak diberi label meski dalam posisi miring/berputar, selama masih bisa dikenali.

- **Tertutup sebagian**
  Jika sebagian kecil objek tertutup, tetap beri label selama identitas utamanya masih tampak.

### B. Kriteria Exclusion (Tidak Layak Diberi Label)

- **Objek tidak sesuai skema**
  Contoh: helm yang tidak dikenakan (misal dibawa di tangan atau diletakkan di meja), tidak perlu diberi label.

- **Ukuran terlalu kecil**
  Jika bounding box < 5% area gambar, objek diabaikan.

- **Objek blur/low quality**
  Jika objek buram dan tidak bisa dipastikan, tidak perlu diberi label.

- **Objek tertutup mayoritas**
  Jika lebih dari 70% area objek tertutup, tidak dilabeli.

### C. Kasus Khusus (Special Cases)

- **Partial occlusion**
  Jika objek hanya tertutup sebagian dan bagian kunci masih bisa dikenali, tetap beri label.

- **Low resolution/gambar jauh**
  Jika PPE tetap bisa dikenali, diberi label. Jika ragu atau ambigu, lebih baik diabaikan.

- **Multi-person frame**
  Semua objek PPE yang terlihat pada setiap orang dalam satu frame dilabeli secara terpisah. Jika objek saling menutupi namun masih bisa dibedakan, masing-masing diberi bounding box tersendiri.
