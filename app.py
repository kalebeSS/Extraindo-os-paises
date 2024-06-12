from bs4 import BeautifulSoup
import requests

#Url do site que faremos a pesquisa
url = 'https://www.scrapethissite.com/pages/simple/'

#Solicitando a requisição por meio de um Método
requisicao = requests.get(url)

#Printa o tipo de resposta a esperada que seja [200]
#print(requisicao)

#Pegando o Html do Site
html_content = requisicao.text
soup = BeautifulSoup(html_content, 'html.parser')

#metodo que retorna os 'h3' da class_ = "country-name" do site para ter os paises 
div = soup.findAll('h3', class_ = "country-name")

for divs in div:
	#removendo os espaços em branco que viriam junto.
	paises = divs.text.strip()
	print(paises)