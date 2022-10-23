#!/bin/bash
# Programa para ejemplificar como capturar la información del usuario utilizando el comando read.
# Autor: Sebastián Valencia

echo "Programa Utilidades Postgres"
read -p "Ingresar una opción:" option
read -p "Ingresar el nombre del archivo del backup:" backupName
echo "Opción: $option, bbackupName: $backupName"
