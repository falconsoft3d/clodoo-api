
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
Listado de funciones en la API implementadas y ejemplos de I/O de datos.

1- Autenticacion

Endpoint REST =  /auth

Método: POST
JSON entrada:

{
 "user": "tuodoo@gmail.com",
 "password": "odoo",
 "database": "odoo"
}


JSON salida:
{
    "id": 9    // Id del usuario en Odoo.
}
JSON error:
{
    "code": 406, 
    "message": "......"
} 

2- Creación de modelos

Endpoint = /create
Método: POST

JSON entrada:

{
"id_user": "1",
"password": "odoo",
"model": "res.partner",
"database": "odoo",
"fields": {
    "field1": "valuefield1",
    "field2": "valuefield2",
    "field3": "valuefield3"
}
}

JSON salida:
{
   "dataResult": 1           // Id del modelo creado.
}

JSON error:
{
    "code": 406, 
    "message": "..."
}      

3- Editar un registro aociado a un modelo a partir de su identificador

Endpoint = /update
Método: POST

JSON entrada:

{
"id_user": 1,
"password": "odoo",
"model": "res.partner",
"idRecord": 10,
"database": "odoo",
"fields": {
    "name": "Pepe",
    "comment": "Este es el partner Pepe",
    "country_id":50

}
}

JSON salida:
{
    "dataResult": true  // Si fue satisfactoria la operación
}

JSON error:
{
    "code": 406, 
    "message": "..."
} 

4- Eliminar un registro aociado a un modelo a partir de su identificador

Endpoint = /delete
Método: POST

JSON entrada:

{
 "id_user": 1,
 "password": "odoo",
 "model": "res.partner",
 "idRecord": [10,11],      // Identificadores de/los elementos a eliminar.
 "database": "odoo"
}

JSON salida:
{
    "dataResult": true
}
JSON error:
{
    "code": 406, 
    "message": "..."
} 

5- Devolver listado de registros asociados a un modelo que cumplan ciertas condiciones

Notas:

 1- En el filtro que tiene la forma:
  "campo": "!=valor"
   Se admiten los operadores: =,>=,<=,<,>,like,!=

 2- Las opciones son opcionales:
    - No las pones
    - Si las pones sería así: {}

 3- Dentro de las opciones si no especificas el campo "fields" solo se listan los id de los registros

Endpoint = /listar
Método: POST

JSON entrada:

{
"id_user": 1,
"password": "odoo",
"model": "res.partner",
"database": "odoo",
"filter": [{
    "name": "!=Jose"
}],
"options": {
    "offset": 0,
    "limit": 10,
    "order": "name",		 
    "fields": ["name", "country_id", "comment"]
}
}

JSON salida:
{
"dataResult": [
{
    "comment": false, 
    "country_id": [
    52, 
    "Cuba"
    ], 
    "id": 1, 
    "name": "Enterprise A1"
}, 
{
    "comment": false, 
    "country_id": false, 
    "id": 8, 
    "name": "sdf sdf"
}, 
{
    "comment": false, 
    "country_id": false, 
    "id": 9, 
    "name": "sdf sdf"
}, 
{
    "comment": false, 
    "country_id": false, 
    "id": 7, 
    "name": "sdf sdf"
}
]
}

JSON error:
{
    "code": 406, 
    "message": ".."
}

6- Devolver listado de ids asociados a un modelo que cumplan ciertas condiciones

Notas:

 1- En el filtro que tiene la forma:
  "campo": "!=valor"
   Se admiten los operadores: =,>=,<=,<,>,like,!=

 2- Las opciones son opcionales:
    - No las pones
    - Si las pones sería así: {}


Endpoint = /listIds
Método: POST

JSON entrada:

{
 "id_user": "1",
 "password": "odoo",
 "model": "res.partner",
 "database": "odoo",
 "filter": [{
            "field1": ">23"
            },
            {
            "field2": "=sdf sdf"
            }],
 "options": {
    "offset": 1,                 
    "limit": 10,                 
    "order": "fieldName",        
    "count": false               
}
}

JSON salida:
{
    "dataResult": [3,1,8,9,7]
}
JSON error:
{
    "code": 406, 
    "message": ".."
} 

7- Devolver cantidad de registros asociados a un modelo que cumplan ciertas condiciones
Notas:
 1- En el filtro que tiene la forma:
  "campo": "!=valor"
   Se admiten los operadores: =,>=,<=,<,>,like,!=
 
Endpoint = /count

Método: POST
JSON entrada:

{
"id_user": "1",
"password": "odoo",
"model": "res.partner",
"filter": [{
            "field1": ">23"
            }, {
            "field2": "like sdf sdf"
            }]
}

JSON salida:
{
    "dataResult": 123
}
JSON error:
{
    "code": 406, 
    "message": "..."
} 
