#!/bin/bash
# Programa que permite manejar las utilidades de Postres
# Autor: Sebastián Valencia

opcion=0

while : 
do
  #Limpiar la pantalla
  clear
  #Desplegar el menú de opciones
  echo "___________________________________________"
  echo "-PGUTIL - Programa de Utilidad de Postgres-"
  echo "___________________________________________"
  echo "               MENÚ PRINCIPAL              "
  echo "___________________________________________"
  echo "1. Instalar Postgres"
  echo "2. Desinstalar Postgres"
  echo "3. Hacer un respaldo"
  echo "4. Restaurar"
  echo "5. Salir"

  #Leer los datos del usuario
  read -p "Ingrese una opción (1-5):" opcion

  #Validar la opción ingresada
  case "$opcion" in
    1) 
      echo "Instalando postgres....."
      sleep 3
      ;;
    2) 
      echo "Desinstalando postgres....."
      sleep 3
      ;;
    3) 
      echo "Haciendo un respaldo....."
      sleep 3
      ;;
    4)
      echo "Restaurando....."
      sleep 3
      ;;
    5)
      echo "Saliendo....."
      exit 0
      ;;
  esac
done
