
import nas
import lib_nas 

# _bias_4_16
# estructura 4 bits --16 patrones de adaptacion 

# @ciudadano72 
# @autor:Jose Luis Prado Seoane 
# https://github.com/ciudadano72
# https://joseluisprase.wixsite.com/jlps

# @estructura: Clase -- 4 Bits : 16 pattern detected 
class _bias_4_16(): # 
    def __init__(self,_bias_):
        self.__neuron_0=nas.neuron(_bias_)
        self.__neuron_1=nas.neuron(_bias_)
        self.__neuron_2=nas.neuron(_bias_)
        self.__bias=int(_bias_)
        self.__base_pattern=[]
        
        for base_pattern in range(16):
            self.__base_pattern.append(0)

    # @info: Pattern imputs --core
    def _memory_pattern_(
        self,_dendrite_0_,_dendrite_1_,
        _dendrite_2_,_dendrite_3_,_pattern_):
        pattern=[]
        self._set_(pattern,_pattern_)
        self._memory_init_0()
        self.__neuron_0.ibn_(_dendrite_0_,_dendrite_1_)
        self.__neuron_1.ibn_(_dendrite_2_,_dendrite_3_)
        
        self.__neuron_2.ibn_(self.__neuron_0._out_,self.__neuron_1._out_)
        _rtn = lib_nas._pattern_nas_16(
            _dendrite_0_,_dendrite_1_,
            _dendrite_2_,_dendrite_3_,
            self.__neuron_2._out_,
            self.__base_pattern)
        lib_nas._layer_1_1_(self.__neuron_2,self.__bias,lib_nas._memory_(_rtn))
        self.__neuron_2.ibn_(self.__neuron_0._out_,self.__neuron_1._out_)
        
        return self.__neuron_2._out_

    # @info: mapa de adaptacion
    def _mapper_(self,_pattern_):
        valores=[0,1]
        mapa=[]
        pattern=[]
        count=0
        
        print ("\n<--mapper-->")
        print ("2 inputs:4 pattern")
        
        self._set_(pattern,_pattern_)
        
        for x in valores:
            for y in valores:
                for z in valores:
                    for w in valores:
                        mapa.append("%s%s%s%s" %(x,y,z,w))
                        
        for x in range(len(mapa)):
            if count<=9:
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

