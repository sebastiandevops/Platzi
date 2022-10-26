#!/bin/bash
# Programa para ejemplificar como escribir en un archivo. 
# Autor: Sebastián Valencia

echo "Escribir en un archivo"

echo "vaLores escritos con el argumento echo" >> "$1"

#Adición multilínea
cat <<EOM >> "$1"
$2
EOM
