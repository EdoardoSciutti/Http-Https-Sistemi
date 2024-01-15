import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver

# Richiedi all'utente di inserire un URL
url = "http://"+ input("Inserisci un URL: ")

# Stampa la directory di lavoro corrente
print("Directory di lavoro corrente:", os.getcwd())

# Se i file output.html e cookie.txt esistono, eliminali
if os.path.exists('output.html'):
    os.remove('output.html')
if os.path.exists('cookie.txt'):
    os.remove('cookie.txt')

# Crea una nuova istanza del driver Firefox
driver = webdriver.Firefox()

# Vai al sito web
driver.get(url)

# Ottieni l'HTML della pagina
html = driver.page_source

# Scrivi l'HTML in un file
with open('output.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Prova a salvare i cookie della sessione in un file
try:
    cookies = driver.get_cookies()
    if cookies:
        # Se ci sono dei cookie, scrivili in un file
        with open('cookie.txt', 'w') as f:
            for cookie in cookies:
                f.write(str(cookie) + "\n")
        print("File 'cookie.txt' creato con successo.")
    else:
        print("Nessun cookie trovato")
except Exception as e:
    print("Errore nella creazione del file dei cookie:", str(e))

# Chiudi il browser
driver.quit()

# Aspetta l'input dell'utente prima di chiudere
input("Premi Invio per chiudere...")