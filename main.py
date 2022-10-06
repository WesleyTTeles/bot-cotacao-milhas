import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

mail = '//*[@id="quotation-form"]/div[1]/div[1]/input'
select_program_milhas = '//*[@id="quotation-form"]/div[1]/div[2]/div'
select_type_smiles = '//*[@id="quotation-form"]/div[1]/div[2]/div/div/div[2]/div/ul/li[3]'
options_qtd_milhas = '//*[@id="select_points_1"]'
select_qtd_milhas = '//*[@id="select_points_1"]/div[2]/div[2]/ul/li[81]'
btn_cotar = '//*[@id="quotation-form"]/div[2]/div/div/button'

def price():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    wait = WebDriverWait(driver, 10)
    driver.get("https://hotmilhas.com.br/")

    try:
        
        insert_email = driver.find_element_by_xpath(mail).send_keys("wesley.teles@gmail.com")
        print("E-mail Colocado com Sucesso!")
        time.sleep(5)

        insert_opt_program = driver.find_element_by_xpath(select_program_milhas)
        insert_opt_program.click()
        print("Opções do Programa Selecionado!")

        insert_select_smiles = driver.find_element_by_xpath(select_type_smiles)
        insert_select_smiles.click()
        print("Smiles Selecionado!")

        insert_options_qtd = driver.find_element_by_xpath(options_qtd_milhas)
        insert_options_qtd.click()
        print("Opções de Quantidade Selecionada!")

        insert_select_qtd_select = driver.find_element_by_xpath(select_qtd_milhas)
        insert_select_qtd_select.click()
        print("100mil Milhas Selecionada!")

        insert_btn_cotar = driver.find_element_by_xpath(btn_cotar)
        insert_btn_cotar.click()
        print(" ")
        print("Cotação Realizada com Sucesso!")
    except:
        print("Nao foi possivel realizar Sua Cotação!")
    
    driver.close()
    
price()

# # Tipos de Agendamentos
# # schedule.every(3).seconds.do(price)
# schedule.every(1).minutes.do(price)
# # schedule.every(5).hour.do(price)
# # schedule.every().day.at("21:35").do(price)
# # schedule.every(3).to(10).do(price)
# # schedule.every(3).monday.do(price)
# # schedule.every(3).wednesday.at("10:00").do(price)

# while True:
#     schedule.run_pending()
#     print("Bot Trabalhando...")
#     print(" ")
#     time.sleep(5)




