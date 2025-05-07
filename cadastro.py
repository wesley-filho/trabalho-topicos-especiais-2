from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

# Lista de anúncios (não alterada)
anuncios = [['VOLKSWAGEN', 'VOLKSWAGEN VOYAGE 1.6 MSI FLEX 16V 4P AUT', '2019', 'Manual', 'Sedã',
'Prata', '49999', 'Vila Velha'], ['FORD', 'FORD KA+ SEDAN 1.0 TIVCT FLEX 4P', '2019', 'Manual', 'Sedã',
'Prata', '55000', 'Vila Velha'], ['VOLKSWAGEN', 'VOLKSWAGEN VOYAGE TRENDLINE 1.6 T.FLEX 8V 4P', '2018',
'Manual', 'Sedã', 'Branco', '53900', 'Vitória'], ['CHEVROLET', 'CHEVROLET PRISMA SED. LT 1.4 8V FLEXPOWER 4P AUT.', '2019', 'Automático', 'Sedã', 'Preto', '49990', 'Serra'], ['FORD', 'FORD KA 1.5 SEDAN SE 12V FLEX 4P MEC.', '2020', 'Manual', 'Sedã', 'Cinza', '56900', 'Vila Velha'], ['HYUNDAI', 'HYUNDAI HB20 COMFORT PLUS 1.0 TB FLEX 12V MEC.', '2017', 'Manual', 'Sedã', 'Branco', '55000', 'Colatina'], ['RENAULT',
'RENAULT LOGAN ZEN FLEX 1.0 12V 4P MEC.', '2020', 'Manual', 'Sedã', 'Branco', '51990', 'Vitória'],
['VOLKSWAGEN', 'VOLKSWAGEN VOYAGE 1.6 MSI FLEX 8V 4P', '2020', 'Manual', 'Sedã', 'Branco', '59500', 'Vila Velha'], ['FIAT', 'FIAT CRONOS DRIVE 1.8 16V FLEX AUT', '2020', 'Automático', 'Sedã', 'Cinza', '60000',
'Serra'], ['CHEVROLET', 'CHEVROLET ONIX SED. PLUS PREM. 1.0 12V TB FLEX AUT', '2020', 'Automático',
'Sedã', '4 portas', '600', 'Cariacica'], ['FORD', 'FORD KA+ SEDAN 1.0 SEL TICVT FLEX 4P', '2018',
'Manual', 'Sedã', 'Preto', '50000', 'Jaguaré']]


# Chaves para converter em dicionário
chaves = ['marca', 'modelo', 'ano', 'cambio', 'tipo', 'cor', 'preco', 'cidade']

# Acessando o site
url = "https://weka.inf.ufes.br/IFESTP/login.php"
driver = webdriver.Firefox()
driver.get(url)

# Preenchendo login
nickname = driver.find_element(By.NAME, "username")
nickname.send_keys("Lucas")

senha = driver.find_element(By.NAME, "password")
senha.send_keys("minuendo10")
senha.send_keys(Keys.RETURN)

# Espera a página carregar
sleep(2)

# Clicando no botão "Inserir novo" com segurança
try:
    inserir_novo_click = driver.find_element(By.CLASS_NAME, "btn")
    inserir_novo_click.click()
    print("Botão 'Inserir novo' clicado com sucesso!")
except Exception as e:
    print("Erro ao clicar no botão:", e)

# Iterando sobre os anúncios e convertendo para dicionário
print("Começando a iterar os anúncios...")

for anuncio in anuncios:
    # Convertendo cada anúncio para dicionário
    carro = dict(zip(chaves, anuncio))  # Criando o dicionário a partir do anúncio
    
    marca = driver.find_element(By.NAME,"marca")
    marca.send_keys(carro['marca'])
    
    ano = driver.find_element(By.NAME, "ano")
    ano.send_keys(carro['ano'])
 
    
    valor = driver.find_element(By.NAME,"valor")
    valor.send_keys(carro['preco'])

    cambio = driver.find_element(By.ID,"cambioAutomatico")
    if(carro['cambio'] == "Automático"):
        cambio.click()
    
    tiposedan = driver.find_element(By.ID,"c_sedan")
    tipohatch = driver.find_element(By.ID,"c_hatch")

    if(carro ['tipo'] == "Hatch"):
       tipohatch.click()
    elif (carro ['tipo'] == "Sedã"):
       tiposedan.click()
    
    modelo = driver.find_element(By.NAME,"modelo")
    modelo.send_keys(carro['modelo'])

    municipio = driver.find_element(By.NAME,"municipio")
    municipio.send_keys(carro['cidade'])

    cor_select = Select(driver.find_element(By.NAME, "cor"))

    # Definindo o valor a ser selecionado, por exemplo, 'preto' ou 'branco' ou outro valor do vetor
    valor_cor = carro['cor'].lower()  # Ajuste para garantir que a cor seja em minúsculo, já que os valores do select estão em minúsculo

    # Verificando se o valor existe nas opções do select
    valores_validos = [opcao.get_attribute("value") for opcao in cor_select.options]

    # Se o valor da cor não estiver disponível, escolher um valor alternativo
    if valor_cor in valores_validos:
        cor_select.select_by_value(valor_cor)
    else:
        # Selecionando o primeiro valor disponível, como alternativa
        cor_select.select_by_value(valores_validos[0])  



    # Printando os dados do carro
    print("Marca:", carro['marca'])
    print("Modelo:", carro['modelo'])
    print("Ano:", carro['ano'])
    print("Câmbio:", carro['cambio'])
    print("Tipo:", carro['tipo'])
    print("Cor:", carro['cor'])
    print("Preço:", carro['preco'])
    print("Cidade:", carro['cidade'])
    print("-" * 40)

    inserir_novo_click = driver.find_element(By.CLASS_NAME, "btn")
    inserir_novo_click.click()

    inserir_novo_click = driver.find_element(By.CLASS_NAME, "btn")
    inserir_novo_click.click()

    sleep(3)
driver.quit()

