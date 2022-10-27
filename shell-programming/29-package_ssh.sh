#!/bin/bash
# Programa para ejemplificar como transferir por la red ustilizando el comando rsync y zip para optimizar la velocidad. 
# Autor: Sebastián Valencia

echo "Empaquetar todos los scripts del curso con zip y transferirlos a otro servidor."

read -p "Ingresar el host: " host
read -p "Ingresar el usuario: " usuario
echo -e "\nSe procederá a eempaquetar y transferir."

rsync -avz "$(pwd)" "$usuario"@"$host":/home/vagrant
