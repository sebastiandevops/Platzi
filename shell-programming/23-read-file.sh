#!/bin/bash
# Programa para ejemplificar como se lee un archivo
# Autor: Sebastián Valencia

echo "Leer un archivo"
cat "$1"
echo -e "\nAlamacenar los valores en una variable"
valorCat=$(cat "$1")
echo "$valorCat"

# Se utiliza la variable IFS (internal fiel separator) para evitar que los espacios en blanco al incio y al final se recorten
echo -e "\nLeer archivos línea por línea utilizando while"
while IFS= read linea; do
  echo "$linea"
done < "$1"
