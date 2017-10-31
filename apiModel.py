class ApiModel:
    #Objeto de la api
    api=None
    #La base de datos a usar (String)
    database=""
    #El ID de usuario (recuperado mediante autenticacion) (Integer)
    userID=""
    #La clave del  usuario (String)
    password=""
    #El nombre del modelo (String)
    model=""
    #El nombre del metodo (String)
    method=""
    #Lista de parametros pasados por posicion (list/array)
    parameter = []
    #Undiccionario de opciones (dict) (Opcional)
    options = {}

    
    def __init__(self,api,database,userID,password,model,method,parameter,options={}):
        self.api=api;
        self.database=database
        self.userID=userID
        self.password=password
        self.model=model
        self.method=method
        self.parameter=parameter
        self.options=options           
        self.validate()


    def validate(self):
        methods = [
            'check_access_rights',
            'search',
            'search_count',
            'read',
            'fields_get',
            'search_read',
            'create',
            'write',
            'unlink'        
            ]
        if not self.method in methods:
            raise CallMethodIsInvalidError("El metodo usado no es correcto.")

        
    def execute(self):       
       return self.api.execute_kw(self.database, self.userID, self.password,self.model, self.method,self.parameter,self.options)
    
        
class CallMethodIsInvalidError(Exception):
    def __init__(self, message):       
        super(CallMethodIsInvalidError, self).__init__(message)       

class CallMethodError(Exception):
    def __init__(self, message):       
        super(CallMethodError, self).__init__(message)              