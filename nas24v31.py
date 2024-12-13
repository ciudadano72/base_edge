
import re
import nas
import lib_nas

# Base: _bias_2_4 : (neuron _neuron_24v3.1) --naspy modf.
# estructura 2 bits --4 patrones de adaptacion + I/O Grid:RNA    

# @ciudadano72 
# @autor:Jose Luis Prado Seoane 
# https://github.com/ciudadano72
# https://joseluisprase.wixsite.com/jlps

class _neuron_24v31():
    #CONSTRUCTOR:
    def __init__(self,_bias_,_grid_=" Here ---path to RnA_GRID -- "):
        self.__neuron=nas.neuron(_bias_)
        self.__bias=int(_bias_)
        self.__base_pattern=[]
        self.__grid=_grid_.strip()
        self.__mute=0
        self.__ref_class = "neuron_" + str(self.__bias)  
            
        for base_pattern in range(4):
            self.__base_pattern.append(0)
            
        rnl_grid = open(self.__grid,"a")
        rnl_grid.write(self.__ref_class+":0000\n")
        rnl_grid.close()

    # @info: imputs
    def _pattern_grid(self,_pattern_):
        pattern=[];dump_pattern="";neuron_id=0;_patterns=[]
        self._set_(pattern,_pattern_)

        for token in self.__base_pattern:
            dump_pattern+=str(token)

        rnl_grid = open(self.__grid,"r")
        
        for neuron_pattern in rnl_grid.readlines():
            _patterns.append(neuron_pattern)
        rnl_grid.close()
        
        for i in range(len(_patterns)-1,-1,-1):
            neuron_pattern=_patterns[i]
            neuron_id=neuron_pattern[:neuron_pattern.find(":")]
            token_id=int(neuron_id[neuron_id.find("_")+1:])
            
            if int(token_id)==self.__bias:
                _patterns.pop(_patterns.index(neuron_pattern))
                rnl_grid = open(self.__grid,"w")
                rnl_grid.write(self.__ref_class+":"+dump_pattern+'\n')
                
                for token in _patterns:
                    rnl_grid.write(token)
                rnl_grid.close()
                
        for token in range(len(self.__base_pattern)):
            self.__base_pattern[token]=0

    # @info: imputs
    def _memory_pattern_(self,_dendrite_0_,_dendrite_1_):
        rtn_pattern="";pattern=[];cadena="";binary=""
        rnl_grid = open(self.__grid,"r")
        
        for neuron_pattern in rnl_grid.readlines():
            pattern_match=re.match('neuron_'+str(self.__bias),neuron_pattern)
            
            if pattern_match is not None:
                rtn_pattern=neuron_pattern[(neuron_pattern.find(":"))+1:]
                learning=lib_nas._correlator(rtn_pattern[:-1])
                self._set_(pattern,learning)
        rnl_grid.close()

        lib_nas._layer_1_2_(self.__neuron,self.__bias,lib_nas._memory_(0))
        self.__neuron.ibn_(_dendrite_0_,_dendrite_1_)
        _rtn = lib_nas._pattern_nas(_dendrite_0_,_dendrite_1_,self.__neuron._out_,self.__base_pattern)
        lib_nas._layer_1_2_(self.__neuron,self.__bias,lib_nas._memory_(_rtn))
        self.__neuron.ibn_(_dendrite_0_,_dendrite_1_)
        
        if self.__mute==0:
            return self.__neuron._out_
        else:
            return 0

    # #info: inhibidor --outs
    def _mute_(self,_sign_):
        self.__mute=int(_sign_)

    def _set_(self,pattern,_pattern_):
        for token in range(len(self.__base_pattern)):self.__base_pattern[token]=0
        for token in _pattern_:pattern.append(int(token))
        for token in pattern: self.__base_pattern[token]=1
