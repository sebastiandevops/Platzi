#!/bin/bash
# Programa para ejemplificar el uso la sentencia case
# Autor: Sebastián Valencia

opcion=""

echo "Ejemplo sentencia case"
read -n1 -p "Indique una opcion de la A - Z:" opcion
echo -e "\n"

case "$opcion" in
  "A") echo -e "\nOperación Guardar Archivo";;
  "B") echo "Operacion Eliminar Archivo";;
  [C-E]) echo "No está implementada la operación";;
  "*") echo "Opción incorrecta"
esac  
