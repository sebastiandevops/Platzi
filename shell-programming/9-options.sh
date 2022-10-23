#!/bin/bash
# Programa para ejemplificar como se realiza el paso de opciones sin parámetros
# Autor: Sebastián Valencia
# Te amo Mariana Arboleda, gracias por ser tan Arboleda

echo "Programa Opciones"
echo "Opción 1 enviada: $1"
echo "Opción 2 enviada: $2"
echo "Opciones enviadas: $*"
echo -e "\n"
echo "Recuperar valores"
while [ -n "$1" ]
do
case "$1" in
-a) echo "-a opción utilizada";;
-b) echo "-b opción utilizada";;
-c) echo "-c opción utilizada";;
*)echo "$! no es una opción";;
esac
shift
done

