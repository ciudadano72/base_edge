
# @info: estructura data_neural

# @ciudadano72 
# @autor:Jose Luis Prado Seoane 
# https://github.com/ciudadano72
# https://joseluisprase.wixsite.com/jlps

def join_ (_id_,_object_id):
    data_object=[]
    index_tokens=[]
    
    for token in range(len(_object_id)):
        pos_0=_object_id[token][3].find("@002-")
        pos_1=_object_id[token][3].find("@002-")
        id_object=_object_id[token][3][pos_0+1:pos_1]
        
        if int(id_object)==_id_:
            data_object=([_object_id[token][0],
                _object_id[token][1],
                _object_id[token][3][:pos_0]])
            
            return data_object
        
        for mem in data_object[:]:
            (data_object.remove(mem))

def tokens_ (__brain__,_object_id,_obj_4):
    index_tokens=[]
    index_=[]
    data_tmp=[]
    data_tokens=[]
    _Object=[]
    
    for token in range(len(_object_id)):
        for itoken in range(len(_object_id[token][3])):
            if _object_id[token][3][itoken]==":":
                index_tokens.append(itoken)
                
    index_= (list(index_tokens[i:i+4] 
        for i in range(0,len(index_tokens),4)))

    for token in range(len(_object_id)):
        data_tmp=([
            _object_id[token][2],
            (_object_id[token][0]+
                int(_object_id[token][3][index_[token][1]+
                    1:index_[token][2]])/3),
            _object_id[token][3][index_[token][1]+
            1:index_[token][2]],
            (_object_id[token][1]+
                int(_object_id[token][3][index_[token][2]+
                    1:index_[token][3]])/3),
            _object_id[token][3][index_[token][2]+
            1:index_[token][3]],
            (_object_id[token][1]+
                int(_object_id[token][3][index_[token][3]+
                    1:])/2),
            _object_id[token][3][index_[token][3]+1:]])
        
        data_tokens.append(data_tmp)

        print (data_tokens)
        
    _Object=[_object_id,data_tokens,_obj_4]
    
    return _Object




    








   

