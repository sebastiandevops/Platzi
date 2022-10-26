#!/bin/bash
# Programa para ejemplificar el empaquetamiento con el comando tar
# Autor: Sebastián Valencia

echo "Empaquetar todos los scripts de la carpeta shell-programming"
tar -cvf "$1" ./*.sh
