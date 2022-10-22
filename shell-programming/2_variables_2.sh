#!/bin/bash
# Pragrama para revisar la declaración de variables

opcion=0
nombre=Sebastián

echo "Opción: $opcion y Nombre: $nombre"

# Exportar la variable nombre para que este disponible en los demás procesos
export nombre

./2_variables.sh
