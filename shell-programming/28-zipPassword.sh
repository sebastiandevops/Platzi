#!/bin/bash
# Programa para ejemplificar el empaquetamiento con clave utilizando zip.
# Autor: Sebastián Valencia

echo "Empaquetar todos los scripts del curso con zip y asignarles clave de seguridad"

zip -e shell-programming.zip ./*.sh
