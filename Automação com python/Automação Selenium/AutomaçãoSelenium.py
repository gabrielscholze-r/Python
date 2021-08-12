import pandas as pd
base = pd.read_excel("Produtos.xlsx")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


nav = webdriver.Chrome() #inicia uma versão do edge com o webdriver do edge

nav.get("https://www.google.com/") #entra em google.com
nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar") # PESQUISA NO CAMPO DESEJADO AS KEYS DESCRITAS
nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER) # APERTA ENTER
#coleta a cota do dolar com base em um atributo achado no inpecionar
cotadolar = nav.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print("Cotação do dólar: ",cotadolar)

# cotação do euro
nav.get("https://www.google.com/")
nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
nav.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotaeuro = nav.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print("Cotação do euro: ",cotaeuro)

# cotação do ouro
nav.get("https://www.melhorcambio.com/ouro-hoje")
cotaouro = nav.find_element_by_xpath('//*[@id="comercial"]').get_attribute('value')
cotaouro = cotaouro.replace(',','.')
print("Cotação do ouro: ",cotaouro)
nav.quit()
#-----------
#Atualiza a cotação, preço de venda e preço de compra da cotação
#cotação
base.loc[base["Moeda"]=="Dólar", "Cotação"] =  float(cotadolar)
base.loc[base["Moeda"]=="Euro","Cotação"] =  float(cotaeuro)
base.loc[base["Moeda"]=="Ouro","Cotação"] =  float(cotaouro)
#preço de compra = preço original * cotação
base["Preço de Compra"] = base["Preço Base Original"] * base["Cotação"]
#preço de venda = preço de compra * margem
base["Preço de Venda"] = base["Preço de Compra"] * base["Margem"]


base.to_excel("ProdutosNovos.xlsx", index=False) # exporta base de dados sem o index

