import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def cadastraCarro():
    driver = webdriver.Firefox()
    driver.get("http://weka.inf.ufes.br/IFESTP/login.php")

    time.sleep(2)

    txtLogin = driver.find_element(By.ID, "username")
    txtSenha = driver.find_element(By.ID, "password")

    txtLogin.send_keys("wesleyfilho")
    txtSenha.send_keys("picapauben10")

    btnOK = driver.find_element(By.NAME, "submit")
    btnOK.click()

    time.sleep(2)
    btnInserir = driver.find_element(By.XPATH, "/html/body/div/div/div/button")
    btnInserir.click()
    time.sleep(2)

    marca = driver.find_element(By.ID, "marca")
    modelo = driver.find_element(By.ID, "modelo")
    municipio = driver.find_element(By.ID, "municipio")
    valor = driver.find_element(By.ID, "valor")
    ano = driver.find_element(By.ID, "ano")
    tipo = driver.find_element(By.ID, "c_hatch")
    cambio = driver.find_element(By.ID, "cambioAutomatico")
    cor = Select(driver.find_element(By.ID, "cor"))

    marca.send_keys("Ferrari")
    modelo.send_keys("F50")
    municipio.send_keys("Alegre")
    valor.send_keys("200000")
    ano.send_keys("2020")
    tipo.click()
    cambio.click()
    cor.select_by_visible_text("Vermelho")

    btnOK = driver.find_element(By.NAME, "insert")
    btnOK.click()
    time.sleep(2)
    
    driver.close()

cadastraCarro()