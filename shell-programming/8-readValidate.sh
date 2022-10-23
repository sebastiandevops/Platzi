#!/bin/bash
# Programa para ejemplificar como capturar la información del usuarioy validarla. 
# Autor: Sebastián Valencia

option=0
backupName=""
clave=""

echo "Programa Utilidades Postgres"

# Acapta el ingreso de información de sólo un caracter.
read -n1 -p "Ingresar una opción:" option
echo -e "\n"
read -n10 -p "Ingresar el nombre del archivo del backup:" backupName
echo -e "\n"
echo "Opción: $option, bbackupName: $backupName"
read -s -p "Clave:" clave
echo "Clave: $clave"
