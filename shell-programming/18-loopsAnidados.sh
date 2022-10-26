#!/bin/bash
# Programa para ejemplificar el uso de los loops anidados.
# Autor: Sebastián Valencia

echo "Loops Anidados"
for fil in *.sh; do
  for nombre in {1..4}; do
    echo "Nombre archivo:$fil _ $nombre"
  done
done
