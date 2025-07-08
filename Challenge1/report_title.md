# Perencanaan Anotasi Dataset untuk Deteksi PPE

## 1. Skema Labeling

Pada proyek ini, sistem deteksi bertujuan untuk mengenali penggunaan lima atribut Personal Protective Equipment (PPE) yang diwajibkan dalam lingkungan kerja, yaitu:

| Label          | Definisi                                                                                    |
| -------------- | ------------------------------------------------------------------------------------------- |
| hard_hat       | Helm pengaman yang melindungi kepala dari benturan atau benda jatuh                         |
| safety_vest    | Rompi keselamatan berwarna mencolok agar pekerja mudah terlihat                             |
| gloves         | Sarung tangan pelindung untuk mengurangi risiko cedera, panas, atau paparan bahan berbahaya |
| safety_glasses | Kacamata pelindung untuk mencegah debu, serpihan, atau bahan kimia masuk ke mata            |
| steel_toe_boot | Sepatu boot dengan pelindung baja yang melindungi kaki dari benda keras, berat, atau tajam  |

---

## 2. Pertimbangan Skema Labeling

- Kelima label di atas dipilih karena merupakan atribut wajib yang diperlukan untuk dipantau keberadaannya pada pekerja, agar sistem deteksi dapat bekerja dan mengenali atribut yang diperlukan.
- Penamaan label sudah representatif untuk tiap atribut PPE, sehingga dapat langsung dipetakan pada dataset open-source atau kebutuhan pengembangan ke depan.
- Ground-truth yang akurat sangat penting agar model deteksi dapat belajar membedakan keberadaan masing-masing atribut PPE di setiap frame gambar.

---

## 3. Panduan Anotasi

Panduan berikut bertujuan untuk menjaga konsistensi dan reproducibility hasil anotasi antar annotator serta menjaga kualitas dataset.

### A. Kriteria Inclusion (Layak Diberi Label)

- **Objek jelas & relevan**

  Hanya anotasi objek yang termasuk dalam daftar label PPE di atas, dan dapat diidentifikasi secara visual.

- **Ukuran mencukupi**

  Bounding box minimal mencakup 5% area gambar, agar objek cukup informatif untuk model.

- **Orientasi beragam**

  Objek tetap layak diberi label meski dalam posisi miring/berputar, selama masih dapat dikenali.

- **Tertutup sebagian**

  Jika sebagian kecil objek tertutup (misal, tali helm tertutup jaket), tetap boleh diberi label selama identitas utamanya tampak.

### B. Kriteria Exclusion (Tidak Layak Diberi Label)

- **Objek tidak sesuai skema**

  Contoh: helm yang tidak dikenakan (misal dibawa di tangan/tergeletak di meja), tidak perlu diberi label.

- **Ukuran terlalu kecil**

  Jika bounding box < 5% area gambar, objek diabaikan.

- **Objek blur/low quality**

  Jika objek buram dan tidak dapat diidentifikasi dengan keyakinan tinggi, tidak perlu diberi label.

- **Objek tertutup mayoritas**

  Jika lebih dari 70% area objek tertutup, tidak dilabeli.

### C. Kasus Khusus (Special Cases)

- **Partial occlusion**

  Jika objek hanya tertutup sebagian dan bagian kunci masih bisa dikenali, tetap beri label.

- **Low resolution/gambar jauh**

  Jika PPE tetap bisa dikenali, diberi label. Jika ragu/ambigu, lebih baik diabaikan.

- **Multi-person frame**

  Semua objek PPE yang terlihat pada setiap orang dalam satu frame dilabeli secara terpisah. Jika objek saling menutupi namun masih bisa dibedakan, masing-masing diberi bounding box tersendiri.
