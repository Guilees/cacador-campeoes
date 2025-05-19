import json
import os
import csv

def gerar_anuncio(nome_produto):
    return f"🔥 {nome_produto.upper()} chegou! Acesse agora e aproveite: [link]"

def salvar_favorito(produto):
    path = "data/favoritos.csv"
    file_exists = os.path.isfile(path)

    with open(path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=produto.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(produto)

def carregar_favoritos():
    path = "data/favoritos.csv"
    if not os.path.exists(path):
        return []

    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)
