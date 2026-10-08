import os
import networkx as nx
import pandas as pd
import streamlit as st

st.set_page_config(page_title="KRL Route Finder", page_icon="🚆", layout="centered")

G = nx.Graph()

# Otomatis baca folder tempat app.py berada
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, 'jadwal.csv')

if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        G.add_edge(row['Asal'], row['Tujuan'], weight=float(row['Menit']))
else:
    st.error(f"File jadwal.csv tidak ditemukan di: {csv_path}")
    st.stop()

st.title("🚆 Simulasi Rute KRL Jabodetabek")
st.caption("Pencarian Rute Tercepat Berbasis Algoritma Dijkstra & Teori Graf")
st.write("---")

daftar_stasiun = sorted(list(G.nodes()))

col1, col2 = st.columns(2)
with col1:
    stasiun_asal = st.selectbox("Stasiun Asal", daftar_stasiun, index=0)
with col2:
    stasiun_tujuan = st.selectbox("Stasiun Tujuan", daftar_stasiun, index=len(daftar_stasiun) - 1)

if st.button("Cari Rute Tercepat", use_container_width=True, type="primary"):
    if stasiun_asal == stasiun_tujuan:
        st.warning("Stasiun asal dan tujuan tidak boleh sama.")
    else:
        try:
            rute = nx.dijkstra_path(G, source=stasiun_asal, target=stasiun_tujuan, weight='weight')
            total_waktu = nx.dijkstra_path_length(G, source=stasiun_asal, target=stasiun_tujuan, weight='weight')

            st.success("Rute Berhasil Ditemukan!")
            
            st.metric(label="Total Estimasi Waktu", value=f"{int(total_waktu)} Menit")
            st.caption("*Sudah termasuk penalti waktu transit jalan kaki antar-peron.")

            st.write("### Detail Jalur Perjalanan:")
            alur_teks = " ➔ ".join(rute)
            st.info(alur_teks)

            with st.expander("Lihat Rincian Perhentian"):
                for idx, sta in enumerate(rute, 1):
                    st.write(f"{idx}. {sta}")

        except nx.NetworkXNoPath:
            st.error("Tidak ditemukan rute penghubung antara kedua stasiun tersebut.")