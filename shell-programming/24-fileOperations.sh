#!/bin/bash
# Programa para ejemplificar las operacionees de un archivo
# Autor: Sebastián Valencia

echo "Operaciones de un archivo"
mkdir -m 755 backupScripts

echo -e "\nCopiar los scrpts del directorio actual al nuevo directorio backupScripts"
cp ./*.* backupScripts/
ls -la backupScripts/

echo -e "\nMover el directorio backupScripts a otra ubicación: $HOME"

mv backupScripts "$HOME/"

echo -e "\nEliminar los archivos test"
rm test
