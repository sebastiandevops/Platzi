#!/bin/bash
# Programa para ejemplificar el uso expresiones condicionales.
# Autor: Sebastián Valencia

edad=-o
pais=""
pathArchivo=""

read -p "Ingrese su edad:" edad
read -p "Ingrese su país:" pais
read -p "Ingrese el path de su archivo:" pathArchivo

echo -e "\nExpresiones Condicionales con números"
if [ "$edad" -lt 10 ]; then
  echo "La persona es un niño o niña"
elif [ "$edad" -ge 10 ] && [ "$edad" -le 17 ]; then
  echo "La persona se trata de un adolecente"
else
  echo "La persona es mayor de edad"
fi

echo -e "\nExpresiones Condicionales con cadenas"
if [ "$pais" = "EEUU" ]; then
  echo "La persona es Estadounidense"
elif [ "$pais" = "Ecuador" ] || [ "$pais" = "Colombia" ]; then
  echo "La persona es sudamericana"
else
  echo "Se desconoce la nacionalidad"
fi

echo -e "\nExpresiones Condicionales con archivos"
if [ -d "$pathArchivo" ]; then
  echo "El directorio $pathArchivo existe"
else
  echo "El directorio $pathArchivo no existe"
fi
