#!/bin/bash
# Programa para revisar los tipos de operadores.
# Autor: Sebastián Valencia
#
numA=10
numB=4

echo "Operadores Aritméticos"
echo "Números: A=$numA y B=$numB"
echo "Sumar A + B = " $(( numA + numB ))
echo "Restar A - B = " $(( numA - numB ))
echo "Multiplicar A * B = " $(( numA * numB ))
echo "Dividir A / B = " $(( numA / numB ))
echo "Residuo A % B = " $(( numA % numB ))


echo -e "\nOperadores Relacionales"
echo "Números: A=$numA y B=$numB"
echo "A > B = " $(( numA > numB ))
echo "A < B = " $(( numA < numB ))
echo "A >= B = " $(( numA >= numB ))
echo "A <= B = " $(( numA <= numB ))
echo "A == B = " $(( numA == numB ))
echo "A != B = " $(( numA != numB ))


echo -e "\nOperadores de Asignación"
echo "Números: A=$numA y B=$numB"
echo "Sumar A += B" $(( numA += numB ))
echo "Restar A -= B" $(( numA -= numB ))
echo "Multiplicación A *= B" $(( numA *= numB ))
echo "Dividir A /= B" $(( numA /= numB ))
echo "Residuo A %= B" $(( numA %= numB ))
