import nas
import lib_nas 

# @info:
# @estructura _bias_01_net: Clase -- 2 Bits : 4 pattern detected 

# @ciudadano72 
# @autor:Jose Luis Prado Seoane 
# https://github.com/ciudadano72
# https://joseluisprase.wixsite.com/jlps

class _bias_2_4(): 
    def __init__(self,_bias_):
      self.debug=1
      
      if self.debug==1:
        print ("Ejecutando " + self.__class__.__name__) + "...\n"
        
        self.__neuron=nas.neuron(_bias_)
        self.__bias=int(_bias_)
        self.__base_pattern=[]
        
        for base_pattern in range(4):
            self.__base_pattern.append(0)

    def _memory_pattern_(self,_dendrite_0_,_dendrite_1_,_pattern_):
        pattern=[]
        self._set_(pattern,_pattern_)
        lib_nas._layer_1_1_(self.__neuron,self.__bias,lib_nas._memory_(self.__bias))
        self.__neuron.ibn_(_dendrite_0_,_dendrite_1_)
        _rtn = lib_nas._pattern_nas(_dendrite_0_,_dendrite_1_,self.__neuron._out_,self.__base_pattern)
        lib_nas._layer_1_1_(self.__neuron,self.__bias,lib_nas._memory_(_rtn))
        self.__neuron.ibn_(_dendrite_0_,_dendrite_1_)
        
        return self.__neuron._out_

    def _mapper_(self,_pattern_):
        valores=[0,1];mapa=[];pattern=[]
        
        print ("<--mapper-->")
        print ("2 inputs:4 pattern")
        
        self._set_(pattern,_pattern_)
        
        for x in valores:
            for y in valores:
                mapa.append("%s %s" %(x,y))
        
        for x in range(len(mapa)):
            print ("--- %s:%s") %(mapa[x],self.__base_pattern[x])
       
    def _set_(self,pattern,_pattern_):
        for token in range(len(self.__base_pattern)):
            self.__base_pattern[token]=0
            
        for token in _pattern_:
            pattern.append(int(token))
            
        for token in pattern: 
            self.__base_pattern[token]=1

# apps()

# // struct_3_1
def _init_net_1_(_bias_):
    _pattern=[]
    n0 = _bias_2_4(_bias_)
    n1 = nas.neuron(_bias_)
    while True:
        _pattern=input ('PATRON DESEADO: ')
        
        print (_pattern)
        
        for x in range(8):
            den_0_io= int(input ('den_0: '))
            den_1_io= int(input ('den_1: '))
            den_2_io= int(input ('den_2: '))
            
            neuron_0_out=n0._memory_pattern_(den_0_io,den_1_io,_pattern)
            lib_nas._layer_1_1_(n1,_bias_,lib_nas._memory_(2))
            n1.ibn_(neuron_0_out,den_2_io)
            
            print (">> %s") %n1._out_

#_init_net_1_(0)

def _init_net_2_(_bias_):
    n0 = _bias_2_4(_bias_)
    while True:
        try:
            _pattern=input ('PATRON DESEADO: ')
            
            if len(_pattern)<=4:
                n0._mapper_(_pattern)
                
                for x in range(4):
                    den_0_io= int(input ('den_0: '))
                    den_1_io= int(input ('den_1: '))
                    neuron_out=n0._memory_pattern_(den_0_io,den_1_io,_pattern)
                    
                    print (">> %s") %neuron_out
            else:
                print ("Maximo patron de aprendizaje Bias : 4 tokens")
        except:
            print ("Parametro de aprendizaje incorrecto Bias:0123")

_init_net_2_(0)

