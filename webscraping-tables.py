import requests
from bs4 import BeautifulSoup
from plyer import notification

url = 'https://www.bna.com.ar/Personas'
icoDolar = '/home/fideo/proyectos/notifications/assets/images/dolar.ico'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

tabla_dolar = soup.find('table', class_= 'table cotizacion')

for cotizacion in tabla_dolar.find_all('tbody'):
  dolar = cotizacion.find_all('td')[2].text

valorArchivo = open('./valorDolar.txt', "r+")
cotizacionActual=valorArchivo.read(10).strip("\n")

if (dolar != cotizacionActual):
  notification.notify(
              title = 'Dolar',
              message = dolar,
              timeout = 20,
              app_icon = icoDolar
      )
  valorArchivo.seek(0, 0)
  valorArchivo.write(dolar)
