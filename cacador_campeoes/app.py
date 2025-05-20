import streamlit as st
from braip_scraper import buscar_produtos_braip
from utils import gerar_anuncio, salvar_favorito, carregar_favoritos

st.set_page_config(page_title="Caçador de Campeões", layout="wide", page_icon="🕵️‍♂️")

import os

if os.path.exists("assets/style.css"):
    with open("assets/style.css") as f:
        st.markdown('<style>' + f.read() + '</style>', unsafe_allow_html=True)
else:
    st.warning("Arquivo de estilo (style.css) não encontrado.")

st.title("🕵️‍♂️ Caçador de Campeões")

st.sidebar.header("Filtros de busca")
palavra_chave = st.sidebar.text_input("🔍 Palavra-chave", "emagrecimento")
comissao_min = st.sidebar.slider("💸 Comissão mínima (%)", 0, 100, 50)
buscar = st.sidebar.button("Buscar Produtos")

if buscar:
    produtos = buscar_produtos_braip(palavra_chave, comissao_min)
    st.session_state['produtos'] = produtos
    st.success(f"{len(produtos)} produto(s) encontrado(s).")

if 'produtos' in st.session_state:
    for prod in st.session_state['produtos']:
        with st.container():
            st.image(prod['imagem'], width=150)
            st.subheader(prod['nome'])
            st.write(f"💰 Comissão: {prod['comissao']}%")
            st.markdown(f"[🌐 Ver Produto na Braip]({prod['link']})", unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"📌 Salvar", key=prod['id']):
                    salvar_favorito(prod)
                    st.success("Produto salvo nos favoritos!")
            with col2:
                if st.button(f"📄 Gerar Anúncio", key='a'+prod['id']):
                    anuncio = gerar_anuncio(prod['nome'])
                    st.code(anuncio)

st.markdown("---")
st.subheader("⭐ Favoritos")
favoritos = carregar_favoritos()
for fav in favoritos:
    st.write(f"📌 {fav['nome']} - {fav['comissao']}%")
    st.markdown(f"[Ver Produto]({fav['link']})")
