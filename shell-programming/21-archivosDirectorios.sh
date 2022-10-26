#!/bin/bash
# Programa para ejemplificar la creación de archivos y directorios.
# Autor: Sebastián Valencia

echo "Archivos - Directorios"
if [[ $# -ne 2 ]]; then
  echo "Número de parámetros incorretos"
  exit 1
fi

if [ "$1" = "d" ]; then
  mkdir -m 755 "$2"
  echo "Directorio creado correctamente"
  ls -la "$2"
elif [ "$1" = "f" ]; then
  touch "$2"
  echo "Archivo creado correctamente"
  ls -la "$2"
else
  echo "No existe esa opción: $1"
fi
