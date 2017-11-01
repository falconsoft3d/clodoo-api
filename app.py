#!flask/bin/python
from flask import Flask
from flask import request
from flask import jsonify
from flask import abort
from flask import make_response
from flask_cors import CORS
import conf
from apiTraductor import *
from apiController import ApiController

app = Flask(__name__)
cors = CORS(app, resources={r""+conf.urlApi+"*": {"origins": "*"}})

@app.route(conf.urlApi)
def index():    
    return "Hello, World!"


@app.route(conf.urlApi+"auth", methods=['POST'])
def autenticate():
    
    if not request.json or not 'user' in request.json or not 'password' in request.json or not 'database' in request.json:
        return make_response(handleError(406,"Faltan atributos en el JSON de entrada. Campos requeridos: user, password."), 406)
    user = request.json['user']
    password = request.json['password']
    database = request.json['database']
    api =  ApiController()
    id = api.auth(user,password,database);
    if not id:
        return make_response(handleError(406,"Credenciales incorrectas."), 401)
    return make_response(jsonify({'id': id}), 200) 

@app.route(conf.urlApi+"create", methods=['POST'])
def create():
      
    if not request.json or not 'id_user' in request.json or not 'password' in request.json or not 'model' in request.json or not 'fields' in request.json or not 'database' in request.json:
        return make_response(handleError(406,"Faltan atributos en el JSON de entrada. Campos requeridos: id_user, model,fields ,password."), 406)
    
    id_user = request.json['id_user']
    password = request.json['password']
    model =  request.json['model']
    fields =  request.json['fields']
    database = request.json['database']

    parameters = []
    parameters.append(fields)  

    api =  ApiController()
    try:
        id = api.createRecord(database,id_user,password,model,parameters);
    except Exception,e:
        return make_response(handleError(e.faultCode,e.faultString), e.faultCode)
    return make_response(jsonify({'dataResult': id}), 200) 

@app.route(conf.urlApi+"update", methods=['POST'])
def update():
      
    if not request.json or not 'id_user' in request.json or not 'password' in request.json or not 'model' in request.json or not 'fields' in request.json or not 'idRecord' in request.json or not 'database' in request.json:
        return make_response(handleError(406,"Faltan atributos en el JSON de entrada. Campos requeridos: id_user, model,fields ,password, idRecord."), 406)
        
    id_user = request.json['id_user']
    password = request.json['password']
    model =  request.json['model']
    fields =  request.json['fields']
    idRecord =  request.json['idRecord']
    database = request.json['database']


    parameters = []
    parameters.append([idRecord]) 
    parameters.append(fields)  

    api =  ApiController()
    try:
        data = api.writeRecord(database,id_user,password,model,parameters);
    except Exception,e:
        return make_response(handleError(e.faultCode,e.faultString), e.faultCode)
    return make_response(jsonify({'dataResult': data}), 200) 

@app.route(conf.urlApi+"delete", methods=['POST'])
def delete():
      
    if not request.json or not 'id_user' in request.json or not 'password' in request.json or not 'model' in request.json or not 'idRecord' in request.json or not 'database' in request.json:
         return make_response(handleError(406,"Faltan atributos en el JSON de entrada. Campos requeridos: id_user, model, password, idRecord."), 406)
       
    
    id_user = request.json['id_user']
    password = request.json['password']
    model =  request.json['model']
    idRecord =  request.json['idRecord']
    database = request.json['database']


    parameters = []
    parameters.append(idRecord)

    api =  ApiController()
    try:
        data = api.unlinkRecord(database,id_user,password,model,parameters);
    except Exception,e:
        return make_response(handleError(e.faultCode,e.faultString), e.faultCode) 
    return make_response(jsonify({'dataResult': data}), 200) 


@app.route(conf.urlApi+"listIds", methods=['POST'])
def listIdsRecord():
    
    if not request.json or not 'id_user' in request.json or not 'password' in request.json or not 'model' in request.json or not 'database' in request.json:
         return make_response(handleError(406,"Faltan atributos en el JSON de entrada. Campos requeridos: id_user, model, password."), 406)
       
    
    id_user = request.json['id_user']
    password = request.json['password']
    model =  request.json['model']
    database = request.json['database']

    filter_ = None
    parameters = []
    if not 'filter' in request.json:
        parameters.append([])
    else:
        filter_ = request.json['filter']
        filters=[]
        try:
            filters=translateFilter(filter_)
        except Exception,e:
            return make_response(handleError(406,"Error al conformar los filtros. Se admiten los operadores: =,>=,<=,<,>,like,!="), 406)
       
        
        parameters.append(filters)
    
    if not 'options' in request.json:
        options={}
    else:
        options = request.json['options']    

    api =  ApiController()
    try:
        data = api.listRecord(database,id_user,password,model,parameters,options)
    except Exception,e:
        return make_response(handleError(e.faultCode,e.faultString), e.faultCode)
    return make_response(jsonify({'dataResult': data}), 200) 


@app.route(conf.urlApi+"count", methods=['POST'])
def countRecord():
     
    if not request.json or not 'id_user' in request.json or not 'password' in request.json or not 'model' in request.json or not 'database' in request.json:
        return make_response(handleError(406,"Faltan atributos en el JSON de entrada. Campos requeridos: id_user, model, password."), 406)
       
    
    id_user = request.json['id_user']
    password = request.json['password']
    model =  request.json['model']
    database = request.json['database']

    filter_ = None
    parameters = []
    filters=[]
    if not 'filter' in request.json:
        parameters.append([])
    else:
        filter_ = request.json['filter']
        try:
            filters=translateFilter(filter_)
        except Exception,e:
            return make_response(handleError(406,"Error al conformar los filtros. Se admiten los operadores: =,>=,<=,<,>,like,!="), 406)
       
        
        parameters.append(filters)
    
    if not 'options' in request.json:
        options={}
    else:
        options = request.json['options']    

    api =  ApiController()
    try:
        data = api.countRecord(database,id_user,password,model,parameters,options)
    except Exception,e:
        return make_response(handleError(e.faultCode,e.faultString), e.faultCode) 
    return make_response(jsonify({'dataResult': data}), 200) 


@app.route(conf.urlApi+"listar", methods=['POST'])
def listarRecord():
    
    if not request.json or not 'id_user' in request.json or not 'password' in request.json or not 'model' in request.json or not 'database' in request.json:
        return make_response(handleError(406,"Faltan atributos en el JSON de entrada. Campos requeridos: id_user, model, password."), 406)
          
    id_user = request.json['id_user']
    password = request.json['password']
    model =  request.json['model']
    database = request.json['database']

    filter_ = None
    parameters = []
    filters=[]
    if not 'filter' in request.json:
        parameters.append([])
    else:
        filter_ = request.json['filter']
        try:
            filters=translateFilter(filter_)
        except Exception,e:
            return make_response(handleError(406,"Error al conformar los filtros. Se admiten los operadores: =,>=,<=,<,>,like,!="), 406)
       
        parameters.append(filters)
    
    if not 'options' in request.json:
        options={}
    else:
        options = request.json['options']    

    api =  ApiController()
    try:
        data = api.readAndSearchRecord(database,id_user,password,model,parameters,options)
    except Exception,e:
        return make_response(handleError(e.faultCode,e.faultString), e.faultCode) 
    
    return make_response(jsonify({'dataResult': data}), 200) 

def handleError(code,msg):
    return jsonify({"code":code,"message":msg})

if __name__ == '__main__':
    app.run(debug=True)
