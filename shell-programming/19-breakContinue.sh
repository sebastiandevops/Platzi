#!/bin/bash
# Programa para ejemplificar el uso de break y continue
# Autor: Sebastián Valencia

echo "Sentencias break y continue"
for fil in *.sh; do
  for nombre in {1..4}; do
    if [ "$fil" = "10*" ]; then
      break;
    elif [[ "$fil" == 4* ]]; then
      continue;
    else
      echo "Nombre archivo:$fil _ $nombre"
    fi
  done
done
