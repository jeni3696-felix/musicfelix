import streamlit as st
import pandas as pd

### 1. Leia o Arquivo Dados_Artistas.csv e o Transforme em dataframe
df = pd.read_parquet('Dados_Artistas.parquet')

### 2. Coloque um titulo na pagina
st.title("🎶 Top Músicas por Artista")

### 3. Coloque subtitulo titulo na pagina
st.write("Escolha um artista no menu lateral para ver suas músicas mais tocadas.")

### 4. Coloque uma logo na sidebar(barra lateral)
st.sidebar.image('logo.png', width=150)

### 5. Não mexa abaixo, estamos criando uma selectbox, para selecionar o artista
artistas = st.sidebar.selectbox('Selecione o Artista', df['Artist'].unique())
df_artista = df[df['Artist'] == artistas]

### 6. Coloque Mais um subtitulo que mostre o artista que foi selecionado
st.subheader(f"Músicas mais tocadas de **{artistas}**")

### 7. Não mexa aqui, pois esse é o for que vai percorrer o dataframe
st.write('Aqui estão as músicas mais tocadas:')
for index, row in df_artista.iterrows():
    with st.container():
        st.markdown(f"### 🎵 **{row['Track']}**")

        col1, col2 = st.columns(2)
        col1.metric("🎧 Spotify Streams", f"{row['Stream']:,}")
        col2.metric("📺 YouTube Views", f"{row['Views']:,}")

        st.video(row['Url_youtube'])
        st.markdown("---")
        st.link_button('Ouça no Spotify', url=row['Url_spotify'], type='primary')
