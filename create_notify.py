import os
import sys
from subprocess import Popen, check_output

from plyer import notification
from win10toast import ToastNotifier

icoDolar = '/home/fideo/proyectos/python/notifications/assets/images/dolar.ico'

cotizacionDolar = check_output(["./precioDolar.sh"]).decode('UTF-8').strip("\n")

# Chequeo que tipo de dato es cotizacionDolar
#print(type(cotizacionDolar))
# Convierto a string el tipo de dato byte
#print(cotizacionDolar.decode('UTF-8'))

#Popen("./precioDolar.sh", stdout=sys.stdout, stderr=sys.stderr).communicate()

valorArchivo = open('./valorDolar.txt', "r+")

#valorArchivo.write(cotizacionDolar.decode('UTF-8'))

cotizacionActual=valorArchivo.read(10).strip("\n")

print(cotizacionActual)
print(cotizacionDolar)

if (cotizacionDolar != cotizacionActual):
    notification.notify(
            title = 'Dolar',
            message = cotizacionDolar,
            timeout = 1,
            app_icon = icoDolar
    )
    #print(type(cotizacionActual))
    #print(cotizacionActual)
    #print(type(cotizacionDolar))
    #print(cotizacionDolar)
    
    toaster = ToastNotifier()
    toaster.show_toast("hola",
            "Python is 10 seconds awsm!",
            icon_path=icoDolar,
            duration=20)

    valorArchivo.seek(0, 0)
    valorArchivo.write(cotizacionDolar)


#print(os.popen("curl -s https://www.bna.com.ar/Personas | grep -A 2 'Dolar U.S.A  ' | head -3  | tail  -1 | sed  's/<//g' | sed 's/>//g' | sed 's/td//g' | sed '  s/,/./g' |  sed 's/ //g' | rev    | cut -b 5-|rev").read())

valorArchivo.close()
