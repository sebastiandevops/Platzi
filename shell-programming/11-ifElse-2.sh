#!/bin/bash
# Programa para ejemplificar el uso de la sentencia de decisión if, else. 
# Autor: Sebastián Valencia

edad=0

echo "Ejemplo sentencia If - Else"
read -p "Indique cúal es su edad:" edad
if [ "$edad" -le 18 ]; then
  echo "La persona es adolecente"
elif [ "$edad" -ge 19 ] && [ $edad -le 64 ]; then
  echo "La persona es adulta"  
else
  echo "La persona es adulto mayor"
fi
