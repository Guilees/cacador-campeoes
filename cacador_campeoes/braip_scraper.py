import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def buscar_produtos_braip(palavra_chave, comissao_minima):
    url_vitrine = f"https://ev.braip.com/search?q={palavra_chave}"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url_vitrine)
    time.sleep(3)

    produtos = []
    itens = driver.find_elements(By.CLASS_NAME, "vitrine__item")

    for item in itens:
        try:
            nome = item.find_element(By.CLASS_NAME, "vitrine__title").text
            comissao_texto = item.find_element(By.CLASS_NAME, "vitrine__commission").text
            comissao = int(comissao_texto.replace('%', '').strip())

            if comissao >= comissao_minima:
                imagem = item.find_element(By.TAG_NAME, "img").get_attribute("src")
                link = item.find_element(By.TAG_NAME, "a").get_attribute("href")

                produtos.append({
                    'id': link.split('/')[-1],
                    'nome': nome,
                    'comissao': comissao,
                    'imagem': imagem,
                    'link': link
                })
        except:
            continue

    driver.quit()
    return produtos
