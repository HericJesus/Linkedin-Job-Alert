# Import libraries and packages for the project 

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
from openpyxl import Workbook

def abrir_link_vagas(driver, cargo, local):
    
    #local = "Curitiba"
    #cargo = "Analista"

    query = f"{cargo} {local}".replace(" ", "%20")
    url = f"https://www.linkedin.com/jobs/search?keywords={query}"
    #print(url)

    driver.get(url)
    print('- Finish Task 2: open Job search page')

    sleep(3)

    titulos = driver.find_elements(By.CSS_SELECTOR, "a.job-card-list__title--link strong")

    for x in titulos:
        print(x.text)

    empresas = driver.find_elements(By.CSS_SELECTOR, "div.artdeco-entity-lockup__subtitle")

    for x in empresas:
        print(x.text)

    locais = driver.find_elements(By.CSS_SELECTOR, "div.artdeco-entity-lockup__caption")

    for x in locais:
        print(x.text)

    links = driver.find_elements(By.CSS_SELECTOR, "a.job-card-container__link")
    
    for x in links:
        print(x.get_attribute("href"))


    # Garantir que todas as listas tenham o mesmo tamanho
    titulos = [x.text for x in driver.find_elements(By.CSS_SELECTOR, "a.job-card-list__title--link strong")]
    empresas = [x.text for x in driver.find_elements(By.CSS_SELECTOR, "div.artdeco-entity-lockup__subtitle")]
    locais = [x.text for x in driver.find_elements(By.CSS_SELECTOR, "div.artdeco-entity-lockup__caption")]
    links = [x.get_attribute("href") for x in driver.find_elements(By.CSS_SELECTOR, "a.job-card-container__link")]
    min_len = min(len(titulos), len(empresas), len(locais), len(links))
    print(titulos)

    # Criar planilha Excel
    wb = Workbook()
    ws = wb.active
    ws.title = "Vagas"

    # Cabeçalho
    ws.append(["Título", "Empresa", "Local", "Link"])

    # Preencher linhas
    for t, e, l, link in zip(titulos, empresas, locais, links):
        ws.append([t, e, l, link])

    # Salvar planilha
    wb.save("vagas.xlsx")
    print("Planilha salva com sucesso!")


