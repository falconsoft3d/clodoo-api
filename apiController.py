import xmlrpclib
from apiModel import ApiModel
import conf as _
class ApiController:
     
    def __init__(self):
        self.user, self.password = "", ""
        self.service, self.database = _.service, _.database       
        self.common = xmlrpclib.ServerProxy(_.commonEndPoint)
        self.api = xmlrpclib.ServerProxy(_.objectEndPoint)
        
    
    def auth(self,user,password):
        self.user, self.password = user, password
        self.idUser = self.common.authenticate(self.database, self.user, self.password, {})
        return self.idUser
    

   

class ModelNotMethodAvailableError(Exception):
    def __init__(self, message):       
        super(ModelNotMethodAvailableError, self).__init__(message)       
