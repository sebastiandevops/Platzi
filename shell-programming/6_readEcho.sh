#!/bin/bash
# Programa para ejemplificar como capturar la información del usuario utilizando el comando echo, read y $REPLY.
# Autor: Sebastián Valencia

echo "Programa Utilidades Postgres"
echo -n "Ingresar una opción:"
read -r
option=$REPLY
echo -n "Ingresar el nombre del archivo del backup:"
read -r
backupName=$REPLY
echo "Opción: $option, bbackup: $backupName"
