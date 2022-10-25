#!/bin/bash
# Programa para ejemplificar el uso de los arreglos
# Autor: Sebastián Valencia

arregloNumeros=(1 2 3 4 5 6)
arregloCadenas=(Sebastian Marco Antonio Susana)
arregloRangos=({A..Z} {10..20})

# Imprimir todos los valores
echo "Arreglo de números:${arregloNumeros[*]}"
echo "Arreglo de cadenas:${arregloCadenas[*]}"
echo "Arreglo de Números:${arregloRangos[*]}"

# Imprimir los tamaños de los arreglos
echo "Tamaño Arreglo de números:${#arregloNumeros[*]}"
echo "Tamaño Arreglo de cadenas:${#arregloCadenas[*]}"
echo "Tamaño Arreglo de Números:${#arregloRangos[*]}"

# Imprimir los tamaños de los arreglos
echo "Posición 3 Arreglo de números:${arregloNumeros[3]}"
echo "Posición 3 Arreglo de cadenas:${arregloCadenas[3]}"
echo "Posición 3 Arreglo de rangos:${arregloRangos[3]}"

# Añadir y eliminar valores en un arreglo
arregloNumeros[7]=20
unset "arregloNumeros[0]"
echo "Arreglo de números: ${arregloNumeros[*]}"
echo "Tamaño arreglo de Números ${#arregloNumeros[*]}"
