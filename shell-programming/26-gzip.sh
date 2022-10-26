#!/bin/bash
# Programa para ejemplificar el empaquetamiento con el comando tar y gzip
# Autor: Sebastián Valencia

echo "Empaquetar todos los scripts de la carpeta shell-programming"
tar -cvf "$1" ./*.sh

# Cuando see empaqueta con gzip el empaquetamiento anterior se elimina.
gzip "$1"

echo "Empaquetar un solo archivo con un ratio 9"
gzip -9 9-options.sh
