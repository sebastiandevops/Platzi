#!/bin/bash
# Programa para ejemplificar el uso de la sentencia de iteración for
# Autor: Sebastián Valencia

arregloNumeros=(1 2 3 4 5 6)

echo "Iterar en la lista de números"
for num in ${arregloNumeros[*]}
do
  echo "Número:$num"
done

echo "Iterar en la lista de cadenas"
for nom in "Marco" "Pedro" "Luis" "Daniela"
do
  echo "nombres:$nom"
done

echo "Iterar en archivos"
for fil in *
do
  echo "Nombre archivo:$fil"
done

echo "Iterar utilizando un comando"
for fil in *.sh
do
  echo "Nombre archivo:$fil"
done

echo "Iterar utilizando el formato tradicional"
for ((i=1; i<10; i++))
do
  echo "Número:$i"
done
