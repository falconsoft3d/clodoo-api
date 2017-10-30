

def translateFilter(filter_):
    
    if len(filter_)>0:
        filterArray=[]
        for item in filter_:
            filterField=[] 
            for key, value in item.iteritems():                               
                value=value.strip()

                if not value[:4] == "like" and not value[:2] == "!=" and not value[:1] == "=" and not value[:1] == "<=" and not value[:1] == ">=" and not value[:1] == ">" and not value[:1] == "<":
                    raise OperatorInFilterNoExistError("Operador incorrecto en los filtros de campos.")
                
                if value[:4] == "like":
                    sign = value[:4]
                    value = value[4:]
                
                if value[:2] == "!=" or value[:2] == "<=" or value[:2] == ">=":
                    sign = value[:2]
                    value = value[2:]
                
                if value[:1] == "=" or value[:1] == "<" or value[:1] == ">":
                    sign = value[:1]
                    value = value[1:]
                 
                filterField.append(key.strip())
                filterField.append(sign.strip())
                filterField.append(value.strip())
            filterArray.append(filterField)
        return filterArray
    else:
        return []            


class OperatorInFilterNoExistError(Exception):
    def __init__(self, message):       
        super(OperatorInFilterNoExistError, self).__init__(message) 