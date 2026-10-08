import os
import networkx as nx
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="KRL Jabodetabek Route Finder",
    page_icon="🚆",
    layout="centered"
)

G = nx.Graph()

# Penanganan path direktori otomatis
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, 'jadwal.csv')

# Validasi pembacaan berkas dataset
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        G.add_edge(row['Asal'], row['Tujuan'], weight=float(row['Menit']))
else:
    st.error(f"Berkas jadwal.csv tidak ditemukan di direktori: {csv_path}")
    st.stop()

# Header Antarmuka
st.title("🚆 Simulasi Rute KRL Jabodetabek")
st.caption("Pencarian Rute Tercepat Berbasis Algoritma Dijkstra & Pemodelan Virtual Node")
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
            st.metric(label="Total Estimasi Waktu Tempuh", value=f"{int(total_waktu)} Menit")
            st.caption("*Sudah memperhitungkan penalti jalan kaki dan pindah peron di stasiun transit.")

            st.write("### Jalur yang Dilewati:")
            st.info(" ➔ ".join(rute))

            with st.expander("Lihat Rincian Langkah Perjalanan"):
                for idx in range(len(rute) - 1):
                    asal_step = rute[idx]
                    tujuan_step = rute[idx + 1]
                    waktu_step = G[asal_step][tujuan_step]['weight']
                    
                    if "_" in asal_step and "_" in tujuan_step and asal_step.split("_")[0] == tujuan_step.split("_")[0]:
                        st.write(f"🔄 **Transit / Pindah Peron** di {asal_step.split('_')[0]} ({int(waktu_step)} menit)")
                    else:
                        st.write(f"• {asal_step} ➔ {tujuan_step} ({int(waktu_step)} menit)")

        except nx.NetworkXNoPath:
            st.error("Tidak ditemukan rute penghubung antara kedua stasiun yang dipilih.")