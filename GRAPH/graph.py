import os
import networkx as nx
import pandas as pd

G = nx.Graph()

# Otomatis baca folder tempat graph.py berada
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, 'jadwal.csv')

try:
    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        G.add_edge(row['Asal'], row['Tujuan'], weight=float(row['Menit']))
    print("[SISTEM] Database jadwal.csv berhasil dimuat!\n")
except FileNotFoundError:
    print(f"[ERROR] File tidak ditemukan di: {csv_path}")
    print("Pastikan jadwal.csv berada di satu folder dengan graph.py.")
    exit()

print("=" * 48)
print("     SIMULASI RUTE KRL JABODETABEK (DIJKSTRA)   ")
print("=" * 48)
print("*Tips: Untuk stasiun transit, sertakan nama peronnya")
print(" (contoh: Jakarta Kota_Red, TanahAbang_Bawah, Manggarai_Atas)\n")

stasiun_asal = input("Masukkan stasiun awal keberangkatan : ").strip()
stasiun_tujuan = input("Masukkan stasiun tujuan akhir      : ").strip()

if stasiun_asal in G.nodes and stasiun_tujuan in G.nodes:
    rute = nx.dijkstra_path(G, source=stasiun_asal, target=stasiun_tujuan, weight='weight')
    total_waktu = nx.dijkstra_path_length(G, source=stasiun_asal, target=stasiun_tujuan, weight='weight')

    print("\n" + "=" * 48)
    print("HASIL PENCARIAN RUTE TERCEPAT")
    print("=" * 48)
    print("Rute perjalanan:")
    print(" -> ".join(rute))
    print(f"\nTotal estimasi waktu tempuh : {int(total_waktu)} menit")
    print("*Sudah memperhitungkan penalti jalan kaki di stasiun transit.")
    print("=" * 48)
else:
    print("\n[ERROR] Stasiun tidak ditemukan dalam database.")
    print("Pastikan ejaan dan penamaan simpul sesuai dengan yang terdaftar di CSV.")