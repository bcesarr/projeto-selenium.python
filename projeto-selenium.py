# Selenium é uma biblioteca que nos permite contorlar o nosso navegador por meio de códigos com Python, para automação de tarefas.

# Importando o webdriver da biblioteca Selenium.
from time import sleep
from selenium import webdriver

# Importando o webdriver do Chrome da bibliteoca do webdriver_manager para gerenciar o "driver manager".
from webdriver_manager.chrome import ChromeDriverManager

# Importando o serviço para poder passar e utilizar o "webdriver do chrome" que importamos logo acima.
from selenium.webdriver.chrome.service import Service

# Aqui chamamos a biblioteca do "selenium.webdriver.chrome.service" para poder instalar o "ChromeDriverManager" e utiliza-lo.
servico = Service(ChromeDriverManager().install())

# *Todas estás importações vieram com a nova atualização da biblioteca do Selenium e, para ajudar com o download manual que havia do webdriver de antigamente.

# Abrindo o navegador - Google Chrome e passando o parametro do "Service" e indicando a variavel onde ele está = servico.
navegador = webdriver.Chrome(service=servico)

# O comando ".get" serve para navegarmos/irmos até uma página especifica.
navegador.get("https://ri.magazineluiza.com.br/")

# Passando o comando para o código ir até o caminho de onde quero que ele clique no site.
# No "xpath" sempre colocamos aspas simples (''), por que geralmente temos aspas duplas ("") dentro dele.

sleep(1)

# Comando para clicar no "Ok" do pop up que aparece na página.
navegador.find_element("xpath",'//*[@id="Form1"]/div[7]/a').click()

# Comando para encontrar esta div na página
link = navegador.find_element("xpath",'//*[@id="mainContent"]/div[2]/div/div/div[2]/div')

sleep(1.5)

# Comando para rolar a pagina até a div / elemento encontrado com o código acima (armazenado na variavel "link")
navegador.execute_script("arguments[0].scrollIntoView();", link)

# Espere 2 segundos
sleep(2)

# Clicando no link dentro da pagina e acessando a pagina desejada.
navegador.find_element("xpath",'//*[@id="ContentInternal_linkCentral"]').click()

sleep(3)

# Clicando no icone e abrindo uma aba para mostrar a apresentação
navegador.find_element("xpath",'//*[@id="ContentInternal_ContentPlaceHolderConteudo_rptResultados_linkArq_Apresentacao1T_0"]').click()

# // ----------- Faltou Controlar a Nova aba que se abre ----------- \\

# Comando para deixar o navegador aberto, por que sem ele, o navegador fecha ao terminar de executar o programa.
while True:
    pass
