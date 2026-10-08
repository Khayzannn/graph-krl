# 🚆 Simulasi Rute KRL Jabodetabek Berbasis Algoritma Dijkstra

Aplikasi simulasi pencarian rute perjalanan tercepat untuk jaringan KRL Commuter Line Jabodetabek menggunakan **Algoritma Dijkstra** dan pemodelan **Virtual Node** untuk memperhitungkan waktu transit jalan kaki antar-peron secara realistis.

---

## 📌 Fitur Utama

* **Kalkulasi Rute Tercepat:** Menghitung jalur optimal dan total akumulasi waktu tempuh menggunakan pustaka `networkx`.
* **Pemodelan *Virtual Node*:** Memisahkan peron stasiun transit besar (seperti Manggarai, Tanah Abang, Duri, Kampung Bandan, Jakarta Kota, Jatinegara, dan Citayam) guna mengakomodasi penalti waktu transfer fisik penumpang.
* **Cakupan Lintas Operasional:**
  * Lin Bogor (*Red Line*)
  * Lin Cikarang Lingkar (*Blue Line*)
  * Lin Rangkasbitung (*Green Line*) hingga Rangkasbitung
  * Lin Tangerang (*Brown Line*)
  * Lin Tanjung Priok (*Pink Line*)
  * Percabangan Nambo
* **Antarmuka Interaktif:** Tersedia dalam versi web interaktif berbasis **Streamlit** serta versi Command Line Interface (CLI).

---

## 🛠️ Teknologi yang Digunakan

* **Bahasa Pemrograman:** Python 3.10+
* **Graf & Algoritma:** NetworkX
* **Pengolahan Data:** Pandas
* **Antarmuka Web (UI/UX):** Streamlit

---

## 📂 Struktur Berkas

```text
├── app.py            # Aplikasi web antarmuka berbasis Streamlit
├── graph.py          # Program simulasi versi terminal (CLI)
├── jadwal.csv        # Dataset matriks konektivitas dan bobot waktu stasiun
├── requirements.txt  # Daftar dependensi modul Python
└── README.md         # Dokumentasi proyek
