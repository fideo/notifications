#!/usr/bin/env python3 #Esta linea no se debe borrar
#  -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from winotify import Notification, audio

# Obtengo la url del sitio a obtener los datos
url = 'https://www.bna.com.ar/Personas'

# Declaro el path a un icono de dolar
icoDolar = './dolar.ico'

# A traves de request obtengo todo el codigo de la url pasada
r = requests.get(url)
# Paso a BeautifulSoup lo obtenido como texto y lo parseo como HTML
soup = BeautifulSoup(r.text, 'html.parser')

# Busco el tag table con class table cotizacion
tabla_dolar = soup.find('table', class_= 'table cotizacion')

# Recorro la tabla encontrando los tags tbody
for cotizacion in tabla_dolar.find_all('tbody'):
  dolar = cotizacion.find_all('td')[2].text

# Abro el archivo valorDolar.txt donde almaceno el valor dolar.
valorArchivo = open('./valorDolar.txt', "r+")
cotizacionActual=valorArchivo.read(10).strip("\n")

# Pregunto si la cotizacionActual es distinta a la del dolar obtenido del sitio.
# Si es distinta muestro la notificacion con el nuevo valor del dolar.
if (dolar != cotizacionActual):
  toast = Notification(app_id="Cambio la Cotizacion del Dolar",
                       title="Nueva Cotizacion del Dolar",
                       msg=dolar)
  toast.set_audio(audio.SMS, loop=False)
  toast.build().show()
  valorArchivo.seek(0, 0)
  valorArchivo.write(dolar)

valorArchivo.close()