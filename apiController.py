import xmlrpclib
from apiModel import ApiModel
import conf as _
class ApiController:
     
    def __init__(self):
        self.user, self.password = "", ""
        self.service = _.service       
        self.common = xmlrpclib.ServerProxy(_.commonEndPoint)
        self.api = xmlrpclib.ServerProxy(_.objectEndPoint)
        
    
    def auth(self,user,password,database):
        self.user, self.password = user, password
        self.idUser = self.common.authenticate(database, self.user, self.password, {})
        return self.idUser
    

    def checkModelAccessMethod(self,idUser,password,model,methodReview,database):
        method = "check_access_rights"
         
        call = ApiModel(self.api,database,idUser,password,model,method,[methodReview],{'raise_exception': False})
        
        result = call.execute()
        
        return result


    def listRecord(self,database,idUser,password,model,parameter,option={}):
         method = "search"
         if not self.checkModelAccessMethod(idUser,password,model,"read",database):
            raise ModelNotMethodAvailableError("El modelo '"+model+"' no tiene habilitado el metodo de consulta 'read'.")
         
	 
         call = ApiModel(self.api,database,idUser,password,model,method,parameter,option)
         result = call.execute()
         return result
    
    def countRecord(self,database,idUser,password,model,parameter,option={}):
         method = "search_count"
         if not self.checkModelAccessMethod(idUser,password,model,"read",database):
            raise ModelNotMethodAvailableError("El modelo '"+model+"' no tiene habilitado el metodo de consulta 'read'.")
         
         call = ApiModel(self.api,database,idUser,password,model,method,parameter,option)
         result = call.execute()
         return result
    
     
    
    def readAndSearchRecord(self,database,idUser,password,model,parameter,option={}):
         method = "search_read"
         if not self.checkModelAccessMethod(idUser,password,model,"read",database):
            raise ModelNotMethodAvailableError("El modelo '"+model+"' no tiene habilitado el metodo de consulta 'read'.")
         
         call = ApiModel(self.api,database,idUser,password,model,method,parameter,option)
         result = call.execute()
         return result

    def createRecord(self,database,idUser,password,model,fieldsAndValues):
         method = "create"          
         if not self.checkModelAccessMethod(idUser,password,model,"write",database):
            raise ModelNotMethodAvailableError("El modelo '"+model+"' no tiene habilitado el metodo de consulta 'create'.")
         
         call = ApiModel(self.api,database,idUser,password,model,method,fieldsAndValues,{})
         result = call.execute()
         return result
    
    def writeRecord(self,database,idUser,password,model,fieldsAndValues):
         method = "write"    
            
         if not self.checkModelAccessMethod(idUser,password,model,"write",database):
            raise ModelNotMethodAvailableError("El modelo '"+model+"' no tiene habilitado el metodo de consulta 'create'.")
        
         call = ApiModel(self.api,database,idUser,password,model,method,fieldsAndValues,{})
         result = call.execute()
         return result
    def unlinkRecord(self,database,idUser,password,model,fieldsAndValues):
         method = "unlink"
            
         if not self.checkModelAccessMethod(idUser,password,model,"unlink",database):
            raise ModelNotMethodAvailableError("El modelo '"+model+"' no tiene habilitado el metodo de consulta 'create'.")
        
         call = ApiModel(self.api,database,idUser,password,model,method,fieldsAndValues,{})
         result = call.execute()
         return result    

class ModelNotMethodAvailableError(Exception):
    def __init__(self, message):       
        super(ModelNotMethodAvailableError, self).__init__(message)       
