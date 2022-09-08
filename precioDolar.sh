#!/bin/bash                                                                                                                                                                               
precioDolar=$(curl -s https://www.bna.com.ar/Personas | grep -A 2 'Dolar U.S.A' | head -3  | tail  -1 | sed  's/<//g' | sed 's/>//g' | sed 's/td//g' | sed 's/,/./g' |  sed 's/ //g' | rev    | cut -b 5- | rev )

#horaActualizacion=$(curl -s https://www.bna.com.ar/Personas | grep -A 2 'Hora Actualización' | sed  's/<//g' | sed 's/>//g' | sed 's/div class=\"legal\"//g'  | sed 's/\/div//g' | head -1     | sed 's/Actualización//g' | sed 's/         //g')

echo $precioDolar $horaActualizacion

