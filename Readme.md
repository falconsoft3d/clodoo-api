
*****************************************************************************************
Esta es la documentación básica de API-Odoo, un middleware genérico de comunicación XML-RPC a JSON para Odoo, ofrecerá un API REST de varias funciones que se detallan debajo. 

*****************************************************************************************
Requerimentos de instalación:
 Python 2.7 o superior
 Paquete: python-dev
 Servidor con la aplicacion Odoo

El desarrollo se está realizando Ubuntu v16.04.3 LTS

*******************************************************************************************

Instalación: (Tener instalado y configurado gestor de dependencias de python pypi)

1-Crear un entorno virtual (Opcional pero recomendado)
	1- sudo apt-get install virtualenvwrapper
	2- source /etc/bash_completion.d/virtualenvwrapper
	3- mkvirtualenv odoo_env
    4- Para activar el entorno virtual: workon oddo_env, 
    5- Para desactivar en el entorno virtual: deactivate

2- Estar situado dentro de la carpeta del proyecto desde la terminal.
3- Ejecutar pip install -r requirements.txt
4- python app.py

*******************************************************************************************
Configuración
La configuracion se realiza en el fichero conf.py

Base de la URL del api rest que se consumirá.
    urlApi = "/api/v1/"

Dirección del servidor Odoo
    service = 'http://192.168.56.101:8069'

Nombre de la base de datos Odoo
    database = 'odoo'

Endpoint comun del servicio xml-rpc de Odoo (No requiere autenticación)
    commonEndPoint =  service+"/xmlrpc/2/common"
Endpoint servicio de objetos del servicio xml-rpc de Odoo (Requiere autenticación)
    objectEndPoint =  service+"/xmlrpc/2/object" 

*****************************************************************************************

TODO: 
 - Crear los endPoint REST.
 - Implementar las funciones genéricas: autenticar, crear, editar, eliminar, listar, contar

 - Implementados 31.10/, crear, listar y contar, además de funciones puntos de entradas de app.py
 - Falta implementar editar, eliminar y cambiar para incluir la BD en el proceso de autenticación desde el API.
