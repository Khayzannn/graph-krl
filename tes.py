import networkx as nx
import pandas as pd

# ==========================================
# 1. MEMBACA PETA DARI CSV (Ini yang butuh CSV)
# ==========================================
# Misal Anda punya file 'data_krl.csv' berisi 3 kolom: Asal, Tujuan, Menit
# df = pd.read_csv('data_krl.csv')
G = nx.Graph()

# (Simulasi memasukkan data ke graf)
G.add_edge('Tangerang', 'Batu Ceper', weight=4)
G.add_edge('Batu Ceper', 'Duri_Tangerang', weight=20)
G.add_edge('Duri_Tangerang', 'Duri_Loop', weight=7) # Virtual Node
G.add_edge('Duri_Loop', 'Tanah Abang', weight=5)

# ==========================================
# 2. FITUR INPUT PENGGUNA (Ini tidak butuh CSV)
# ==========================================
print("=== APLIKASI RUTE KRL JABODETABEK ===")
# Program akan berhenti sejenak dan meminta Anda mengetik nama stasiun
stasiun_asal = input("Masukkan stasiun awal keberangkatan: ")
stasiun_tujuan = input("Masukkan stasiun tujuan akhir: ")

# ==========================================
# 3. VALIDASI DAN EKSEKUSI DIJKSTRA
# ==========================================
# Komputer mengecek apakah stasiun yang diketik ada di dalam database
if stasiun_asal in G.nodes and stasiun_tujuan in G.nodes:
    
    # Jika stasiun valid, hitung rute tercepat
    rute_tercepat = nx.dijkstra_path(G, source=stasiun_asal, target=stasiun_tujuan, weight='weight')
    waktu_total = nx.dijkstra_path_length(G, source=stasiun_asal, target=stasiun_tujuan, weight='weight')
    
    print("\n=== HASIL PENCARIAN ===")
    print(f"Rute Tercepat dari {stasiun_asal} ke {stasiun_tujuan}:")
    print(" -> ".join(rute_tercepat))
    print(f"Total Waktu Perjalanan: {waktu_total} menit")

else:
    # Jika user salah ketik (typo)
    print("\n[ERROR] Nama stasiun tidak ditemukan! Pastikan ejaan sesuai dengan database.")