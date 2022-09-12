#!/usr/bin/env python3 #Esta linea no se debe borrar
#  -*- coding: utf-8 -*-
import requests
import time
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
from winotify import Notification, audio

# Obtengo la url del sitio a obtener los datos
url = 'https://www.bna.com.ar/Personas'

# Declaro el path a un icono de dolar
icoDolar = './assets/images/dolar.ico'

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
if (dolar != cotizacionActual):
  """ toaster = ToastNotifier()
  toaster.show_toast("La cotizacion del Dolar es:",
            dolar,
            icon_path=icoDolar,
            duration=10)
  """
  toast = Notification(app_id="winotify test",
                             title="Winotify Test Toast",
                             msg="New Notification with actions!")
  toast.add_actions("go to github", "https://github.com/versa-syahptr/winotify")
 
  toast.show()
  '''
  toast.set_audio(audio.Mail, loop=False)
  valorArchivo.seek(0, 0)
  valorArchivo.write(dolar) '''

