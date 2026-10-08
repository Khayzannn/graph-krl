import os
import networkx as nx
import pandas as pd

G = nx.Graph()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, 'jadwal.csv')

try:
    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        G.add_edge(row['Asal'], row['Tujuan'], weight=float(row['Menit']))
    print("[SISTEM] Database jadwal.csv berhasil dimuat!\n")
except FileNotFoundError:
    print(f"[ERROR] Berkas tidak ditemukan di: {csv_path}")
    print("Pastikan jadwal.csv berada di satu folder dengan graph.py.")
    exit()

print("=" * 48)
print("     SIMULASI RUTE KRL JABODETABEK (DIJKSTRA)   ")
print("=" * 48)
print("*Tips: Untuk stasiun transit, sertakan nama jalurnya")
print(" (contoh: Jakarta Kota_Red, TanahAbang_Blue, Manggarai_Red)\n")

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
    print("*Sudah memperhitungkan penalti transit antar-peron.")
    print("=" * 48)
else:
    print("\n[ERROR] Stasiun tidak ditemukan dalam database.")
    print("Pastikan ejaan persis sama dengan yang ada di jadwal.csv.")