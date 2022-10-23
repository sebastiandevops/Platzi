#!/bin/bash
# programa que valida la siguiente información:
# Número de Identificación de un tamaño de 10 números. Ejemplo: 1717836520
# País de Origen denotado por dos letras en un rango específico. Ejemplo: EC, CO, US
# Fecha de Nacimiento en el formato yyyyMMDD. Ejemplo: 20181222

identificacionRegex='^[0-9]{10}$'
paisRegex='^EC|COL|US$'
fechaNacimientoRegex='^(19|20)[0-9]{2}((0[1-9])|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])$'

echo "Expresiones Regulares"
read -p "Ingresar una identificación:" identificacion
read -p "Ingresar las iniciales de un país [EC, COL, US]:" pais
read -p "Ingresar la fecha de nacimiento [yyyyMMDD]:" fechaNacimiento

# Validación Identificación
if [[ $identificacion =~ $identificacionRegex ]]; then
    echo "Identificación $identificacion válida"
else
    echo "Identificación $identificacion inválida"
fi

# Validación País
if [[ $pais =~ $paisRegex ]]; then
    echo "País $pais válido"
else                     
    echo "Paín $pais inválido"
fi

# Validación Fecha de Nacimiento
if [[ $fechaNacimiento =~ $fechaNacimientoRegex ]]; then
    echo "Fecha de nacimiento $fechaNacimiento válida"
else                     
    echo "Fecha de Nacimiento $fechaNacimiento inválida"
fi
