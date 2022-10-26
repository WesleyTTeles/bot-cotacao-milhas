from datetime import datetime
import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


# 1- Latam Pass 
# 2- LP Platinum/Black 
# 3- Smiles 
# 4- Tudo Azul
# Escolher um numero para que altera na opcao do Programa de Milhas
opt_programa = 3

# -----------------------------

# 1- Smiles 
# 2- Latam Pass 
# 3- Tudo Azul 
# 8- LP Platinum/Black
# Escolher um numero para que altera na opcao do tipo do Programa de Milhas
opt_type_prog = 1

# -----------------------------

# COLOQUE SEU E-MAIL ENTRE AS ASPAS ''
email = 'meuemail@.....'
selecte_mail = '//*[@id="quotation-form"]/div[1]/div[1]/input'
select_program_milhas = '//*[@id="quotation-form"]/div[1]/div[2]/div'
select_type_program = f'//*[@id="quotation-form"]/div[1]/div[2]/div/div/div[2]/div/ul/li[{opt_programa}]' 
options_qtd_milhas = f'//*[@id="select_points_{opt_type_prog}"]'
select_qtd_milhas = f'//*[@id="select_points_{opt_type_prog}"]/div[2]/div[2]/ul/li[51]'
btn_cotar = '//*[@id="quotation-form"]/div[2]/div/div/button'

def price():

    chrome_options = webdriver.ChromeOptions()
    # Se quiser ver o bot trabalhando, comente a linha 42 ou onde tem o "--headless"
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)
    driver.get("https://hotmilhas.com.br/")

    try:
        insert_email = driver.find_element(by=By.XPATH, value=selecte_mail).send_keys(email)
        print("E-mail Colocado com Sucesso!")
        time.sleep(3)

        insert_opt_program = driver.find_element(by=By.XPATH, value=select_program_milhas).click()
        print("Opções do Programa Selecionado!")

        insert_select_smiles = driver.find_element(by=By.XPATH, value=select_type_program).click()
        print("Programa Selecionado!")
        time.sleep(3)

        insert_options_qtd = driver.find_element(by=By.XPATH, value=options_qtd_milhas).click()
        print("Opções de Quantidade Selecionada!")
        time.sleep(3)

        insert_select_qtd_select = driver.find_element(by=By.XPATH, value=select_qtd_milhas).click()
        print("Milhas Selecionada!")

        insert_btn_cotar = driver.find_element(by=By.XPATH, value=btn_cotar).click()
        print("Cotacao Realizada com Sucesso!")
    except:
        print("Nao foi possivel realizar Sua Cotação!")

    driver.close()

#Caso nao queria execultar com o agendamento descomente a linha 74 e comente ou apague as linhas 76 a 88
#price()

# Tipos de Agendamentos
# Por segundo, minutos ou hora.
#schedule.every(1).seconds.do(price)
schedule.every(1).minutes.do(price)
# schedule.every(5).hours.do(price)

while True:
    schedule.run_pending()
    data_e_hora = datetime.now()
    hora = data_e_hora.strftime('%d/%m/%Y %H:%M')
    # enquanto o Bot estiver rodando ele vai esta printando essa mensagem a cada x segundos que voce quiser.
    print(hora,"- Bot Trabalhando...")
    time.sleep(10)




