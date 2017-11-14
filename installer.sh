#!/bin/sh

echo "Instalando dependencias desde el repositorio de Ubuntu";
echo "Instalando python-dev & pip";
apt install python-dev python-pip

echo "Instalando las dependencias del API desde el fichero de requirements.txt con Pip";
pip install -r requirements.txt


echo "Iniciando el API para operación (Para cerrarla oprima CTRL + C)";
echo "Para visualizar el API por defecto se ha ubicado la dirección: http://ip.ip.ip.ip:5000/api/v1/ , lea el README para más detalles";
python app.py






