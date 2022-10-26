#!/bin/bash
# Programa que permite monitorear el sistema.
# Autor: Sebastián Valencia

opcion=0

while : 
do
  #Limpiar la pantalla
  clear
  #Desplegar el menú de opciones
  echo "____________________________________________"
  echo "PGUTIL - Programa de información del sistema"
  echo "____________________________________________"
  echo "               MENÚ PRINCIPAL               "
  echo "____________________________________________"
  echo -e "\n1. Procesos actuales"
  echo "2. Memoria disponible"
  echo "3. Espacio en disco"
  echo "4. Información de red"
  echo "5. Variables de entorno"
  echo "6. Información programa"
  echo "7. Hacer backup"
  echo "8. Salir"

  #Leer los datos del usuario
  read -p "Ingrese una opción (1-5):" opcion

  #Validar la opción ingresada
  case "$opcion" in
    1) 
      echo -e "\n Procesos actuales"
      ps aux --sort -rss | head -n 3
      sleep 3
      ;;
    2) 
      echo -e "\nMemoria Disponible"
      grep MemTotal /proc/meminfo
      sleep 3
      ;;
    3) 
      echo -e "\nEspacio en disco"
      df -h
      sleep 3
      ;;
    4)
      echo -e "\nInformación de red"
      ip link show
      sleep 3
      ;;
    5)
      echo -e "\nVariables de entorno"
      env
      sleep 3
      ;;
    6)
      echo -e "\nInformación programa"
      stat 21-informacion_sistema.sh
      sleep 3
      ;;
    7)
      echo -e "\nHaciendo backup"
      sleep 3
      ;;
    8)
      echo -e "\nSaliendo"
      exit 0
      ;;
  esac
done
