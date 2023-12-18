import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/questions/tagged/python?tab=Frequent'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for pergunta in html.select('.s-post-summary--content'):
    titulo = pergunta.select_one('.s-link')
    data = pergunta.select_one(".relativetime")
    votos = pergunta.select_one(".s-post-summary--stats-item-number")

    if titulo and data:
        print(data.text if data else 'N/A', titulo.text if titulo else 'N/A', votos.text if votos else 'N/A', sep='\t')
    else:
        print("Incomplete information for this question.")
