#!/bin/sh

python3 conversion.py $1 $2
glpsol --lp $2 --output solution.txt
echo "Conversion terminée"
