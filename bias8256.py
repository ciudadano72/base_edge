
import nas
import lib_nas 

# _bias_8_256
# estructura 8 bits (1 byte) --256 patrones de adaptacion 

# @ciudadano72 
# @autor:Jose Luis Prado Seoane 
# https://github.com/ciudadano72
# https://joseluisprase.wixsite.com/jlps

# @estructura: Clase -- 8 Bits : 256 pattern detected 
class _bias_8_256(): # @estructura _bias_03_net
    def __init__(self,_bias_):
      self.debug=1
      if self.debug==1:
        print ("\nEjecutando " + self.__class__.__name__) + "...\n"
        
        self.__neuron_0=nas.neuron(_bias_);self.__neuron_1=nas.neuron(_bias_)
        self.__neuron_2=nas.neuron(_bias_);self.__neuron_3=nas.neuron(_bias_)
        self.__neuron_4=nas.neuron(_bias_);self.__neuron_5=nas.neuron(_bias_)
        self.__neuron_6=nas.neuron(_bias_)
        self.__bias=int(_bias_)
        self.__base_pattern=[]
        
        for base_pattern in range(256):
            self.__base_pattern.append(0)

    # @info: Pattern imputs --core
    # @info: adaptacion--> _den_(x)_ se substityue por _dendrite_(x)_
    def _memory_pattern_(
        self,_den_0_,_den_1_,
        _den_2_,_den_3_,_den_4_,
        _den_5_,_den_6_,_den_7_,_pattern_):
        pattern=[]
        self._set_(pattern,_pattern_)
        self._memory_init_0()
        self.__neuron_0.ibn_(_den_0_,_den_1_);self.__neuron_1.ibn_(_den_2_,_den_3_)
        self.__neuron_2.ibn_(_den_4_,_den_5_);self.__neuron_3.ibn_(_den_6_,_den_7_)
        self.__neuron_4.ibn_(self.__neuron_0._out_,self.__neuron_1._out_)
        self.__neuron_5.ibn_(self.__neuron_2._out_,self.__neuron_3._out_)
        self.__neuron_6.ibn_(self.__neuron_4._out_,self.__neuron_5._out_)
        
        _rtn = lib_nas._pattern_nas_256(
            _den_0_,_den_1_,_den_2_,
            _den_3_,_den_4_,_den_5_,
            _den_6_,_den_7_,self.__neuron_6._out_,
            self.__base_pattern)
        lib_nas._layer_1_1_(
            self.__neuron_6,self.__bias,
            lib_nas._memory_(_rtn))
        self.__neuron_6.ibn_(
            self.__neuron_4._out_,
            self.__neuron_5._out_)
        return self.__neuron_6._out_
        self._memory_init_0()
    
    # @info: mapa de adaptacion
    def _mapper_(self,_pattern_):
        valores=[0,1];mapa=[];pattern=[];count=0
        print ("<--mapper-->")
        print ("8 inputs:256 pattern")
        
        self._set_(pattern,_pattern_)
        for x in valores:
            for y in valores:
                for z in valores:
                    for w in valores:
                        for x1 in valores:
                            for y1 in valores:
                                for z1 in valores:
                                    for w1 in valores:
                                        mapa.append("%s%s%s%s%s%s%s%s" %(x,y,z,w,x1,y1,z1,w1))
        for x in range(len(mapa)):
            if count<=9:
                print ("(%s  )---%s:->%s") %(x,mapa[x],self.__base_pattern[x])
            elif count<=99:
                print ("(%s )---%s:->%s") %(x,mapa[x],self.__base_pattern[x])
            else:
                print ("(%s)---%s:->%s") %(x,mapa[x],self.__base_pattern[x])
            count+=1

    # @info: Inicializador 
    def _memory_init_0(self):
        lib_nas._layer_1_1_(self.__neuron_0,self.__bias,lib_nas._memory_(self.__bias))
        lib_nas._layer_1_1_(self.__neuron_1,self.__bias,lib_nas._memory_(self.__bias))
        lib_nas._layer_1_1_(self.__neuron_2,self.__bias,lib_nas._memory_(self.__bias))

    # @info: Reseat volcados y _memory_pattern
    def _set_(self,pattern,_pattern_):
        for token in range(len(self.__base_pattern)):
            self.__base_pattern[token]=0
            
        for token in _pattern_:
            pattern.append(int(token))
            
        for token in pattern: 
            self.__base_pattern[token]=1

#app()

# @info: app_local
def _init_net_2_(_bias_):
    n0 = _bias_8_256(_bias_)
    while True:
        try:
            _pattern=input ('PATRON DESEADO: ')
            if _pattern==":q":
                break
                sys.exit(-1)
            if len(_pattern)==256:
                learning=lib_nas._correlator(_pattern)
                n0._mapper_(learning)
                for x in range(256):
                    den_0_io= int(input ('den_0: '))
                    den_1_io= int(input ('den_1: '))
                    den_2_io= int(input ('den_2: '))
                    den_3_io= int(input ('den_3: '))
                    den_4_io= int(input ('den_4: '))
                    den_5_io= int(input ('den_5: '))
                    den_6_io= int(input ('den_6: '))
                    den_7_io= int(input ('den_7: '))
                    
                    neuron_out=n0._memory_pattern_(
                        den_0_io,den_1_io,den_2_io,
                        den_3_io,den_4_io,den_5_io,
                        den_6_io,den_7_io,learning)
                    
                    print (">> %s") %neuron_out
            else:
                print ("Maximo patron de aprendizaje Bias : 256 tokens")
        except:
            print ("Parametro de aprendizaje incorrecto Bias:0123456789(10)(11)..")

_init_net_2_(0)


