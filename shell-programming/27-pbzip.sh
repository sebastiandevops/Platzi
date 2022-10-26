#!/bin/bash
# Programa para ejemplificar el empaquetamiento con el comando pbzip
# Autor: Sebastián Valencia

echo "Empaquetar todos los scripts de la carpeta shell-programming"
tar -cvf "$1" ./*.sh
pbzip2 -f "$1"
# Cuando see empaqueta con gzip el empaquetamiento anterior se elimina.

echo "Empaquetar un solo archivo con tar y pbzip2"
tar -cf ./*.sh -c > "$1".bz2
