# Simple Web Scraping README

Este guia fornece uma introdução rápida ao web scraping usando Python e a biblioteca BeautifulSoup. O web scraping é uma técnica que permite extrair dados de páginas da web para análise, visualização ou armazenamento.

## Pré-requisitos
- Python instalado (recomenda-se usar a versão 3.x)
- Biblioteca BeautifulSoup (instalável via pip)

## Instalação da Biblioteca
```bash
pip install beautifulsoup4
```
# Como Usar

```python
import requests
from bs4 import BeautifulSoup
```
# Defina a URL alvo
url = 'https://example.com'

# Envie uma solicitação HTTP e obtenha o conteúdo HTML
response = requests.get(url)
html = response.text

# Crie um objeto BeautifulSoup para analisar o HTML
soup = BeautifulSoup(html, 'html.parser')

# Selecione elementos HTML com base em classes, IDs ou tags
title = soup.select_one('.title-class')
paragraph = soup.select_one('#paragraph-id')

# Extraia dados dos elementos selecionados
title_text = title.text if title else 'N/A'
paragraph_text = paragraph.text if paragraph else 'N/A'

# Imprima ou utilize os dados extraídos conforme necessário
print(f'Title: {title_text}')
print(f'Paragraph: {paragraph_text}')
