#!/bin/bash
# Programa para ejemplificar el uso de los if anidados.
# Autor: Sebastián Valencia

notaClase=0

echo "Ejemplo sentencia If - Else"
read -n1 -p "Indique cúal es su nota (1-9):" notaClase
echo -e "\n"
if [ "$notaClase" -ge 7 ]; then
  echo "El alumno aprueba la materia"
  read -p "Continuará estudiando en el siguiente nivel: (s/n)" continua
  if [ "$continua" == "s" ]; then
    echo "Bienvenido al siguiente nivel"
  else
    echo "Greacias por trabajar con nosotros, mucha suerte!"
  fi
else
  echo "El alumno reprueba la materia"
fi
