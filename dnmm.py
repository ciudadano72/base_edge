

import random
import bias416
import nas24v31
import Lib_NAS_Rnas_IA_

# Base: Struct_memory241_DNMM
# Virtual Dynamic Neural Modeling Memory

# @ciudadano72 
# @autor:Jose Luis Prado Seoane 
# https://github.com/ciudadano72
# https://joseluisprase.wixsite.com/jlps

class _DNMM_neural_(): 
    def __init__(self,id_0=0,id_1=1,id_2=2,id_3=3,
        _grid_=Lib_NAS_Rnas_IA_._path_files('grid')):
        self.__n0=nas24v31._neuron_24v31(id_0)
        self.__n1=nas24v31._neuron_24v31(id_1)
        self.__n2=nas24v31._neuron_24v31(id_2)
        self.__n3=nas24v31._neuron_24v31(id_3)
        self.__DNMM_STRUCT=0
        self.__n4=(bias416.
            _bias_4_16(self.__DNMM_STRUCT))
        
        self.__tmp_neuron_patterns=[]
        self.__source_bin=[]
        self.__adjust_source=[]
        self.__mem_DNMM=[]
        self.__limit_line=1
        self.__pattern_bias=[]
        self.__modeling=[]
        self.__bias={}
        self.__neuron_grid=[Lib_NAS_Rnas_IA_._neuron(int(id_0)),
                            Lib_NAS_Rnas_IA_._neuron(int(id_1)),
                            Lib_NAS_Rnas_IA_._neuron(int(id_2)),
                            Lib_NAS_Rnas_IA_._neuron(int(id_3))]
        self.__den=[]
        self.__base_pattern=[]
        self.__grid=_grid_.strip()
        
        for base_pattern in range(8): 
            self.__base_pattern.append(0)  

    # @info: imputs
    def _pattern_grid(self,_pattern_,limit_line):
        pattern=[];dump_pattern="";neuron_id=0;_patterns=[]
        self.__limit_line=int(limit_line)
        tmp=[];_seq_=""
        _ramdon_=0
        
        while(_ramdon_<=2000):
            _pos_dec=random.randrange(16)
            _pos_binary=bin(_pos_dec)
            if len(_pos_binary[2:])==1:
                _seq_="000"+str(_pos_binary[2:])
            elif len(_pos_binary[2:])==2:
                _seq_="00"+str(_pos_binary[2:])
            elif len(_pos_binary[2:])==3:
                _seq_="0"+str(_pos_binary[2:])
            else:_seq_=_pos_binary[2:]     
            if _seq_ in self.__tmp_neuron_patterns[:]:
                continue
            else:tmp.append(_seq_)
            _ramdon_+=1
            
        for x in range(2000):
            if (tmp[x]==Lib_NAS_Rnas_IA_._st(0) or 
                tmp[x]==Lib_NAS_Rnas_IA_._st(1) or 
                tmp[x]==Lib_NAS_Rnas_IA_._st(2) or 
                tmp[x]==Lib_NAS_Rnas_IA_._st(3)):
                
                if tmp[x] not in self.__tmp_neuron_patterns:
                    self.__tmp_neuron_patterns.append(tmp[x])
                    
        for x in range(4):
            self.__bias[x]=[self.__tmp_neuron_patterns[x]]
        self._set_(pattern,_pattern_)
        
        for token in self.__base_pattern:
            dump_pattern+=str(token)
        rnl_grid = open(self.__grid,"r")
        
        for neuron_pattern in rnl_grid.readlines():
            _patterns.append(neuron_pattern)
        rnl_grid.close()
        
        for i in range(len(_patterns)-1,-1,-1):
            neuron_pattern=_patterns[i] # neuron_4:0000
            neuron_id=neuron_pattern[:neuron_pattern.find(":")]
            token_id=int(neuron_id[neuron_id.find("_")+1:])
            
            _id_=int(token_id)
            _patterns.pop(_patterns.index(neuron_pattern))
            rnl_grid = open(self.__grid,"w")
            
            for token_id in range(4):
                rnl_grid.write(str(self.__neuron_grid[token_id])+
                    ":"+self.__tmp_neuron_patterns[token_id]+'\n')

            for token in _patterns:
                rnl_grid.write(token)
            rnl_grid.close()
            
        for token in range(len(self.__base_pattern)):
            self.__base_pattern[token]=0
            
        return self.__tmp_neuron_patterns

    # @info: imputs/Layers/soma
    def _layers_(self,_dendrite_0_,_dendrite_1_):
        _composite_den_=(str(_dendrite_0_)+str(_dendrite_1_))
        def _layers_in(self,_dendrite_0_,_dendrite_1_):
            #axon_sense=0
            axon_0=(
                self.__n0._memory_pattern_(
                    _dendrite_0_,_dendrite_1_))
            axon_1=(
                self.__n1._memory_pattern_(
                    _dendrite_0_,_dendrite_1_))
            axon_2=(
                self.__n2._memory_pattern_(
                    _dendrite_0_,_dendrite_1_))
            axon_3=(
                self.__n3._memory_pattern_(
                    _dendrite_0_,_dendrite_1_))
            _seq_pattern_=Lib_NAS_Rnas_IA_._st(4)
            
            axon_sense=(self.__n4.
                _memory_pattern_(axon_0,axon_1,
                    axon_2,axon_3,_seq_pattern_))
            
            _composite_bias_=(str(axon_0)+str(axon_1)+
                str(axon_2)+str(axon_3)) 
            
            if _composite_bias_ in self.__tmp_neuron_patterns: 
                neuron=(Lib_NAS_Rnas_IA_.
                    _neuron_matriz(int(self.__tmp_neuron_patterns.
                        index(_composite_bias_))))
                self.__pattern_bias.append(neuron) 
                
            for token in self.__pattern_bias:
                (self.__modeling.
                    append(str(self.
                        __tmp_neuron_patterns[int(token[1:])])))
                
            return (neuron,_composite_bias_,axon_sense)

        neuron,_composite_bias_,axon_sense=(_layers_in(self,
            _dendrite_0_,_dendrite_1_))
        
        (self.__mem_DNMM.append(neuron+"_v"+
            _composite_den_+"_p"+_composite_bias_+"_F"+str(axon_sense)))
        
        return (self.__pattern_bias,self.
            __modeling[-(self.
                __limit_line*4):],self.
            __mem_DNMM)

    # @info: modelizacion
    def _modeling_(self,_struct,_path_,
        _DNMM,bits,limit,bloques=0):
        _pattern_=[]
        _pattern_=(_struct.
            _pattern_map_source_parser(_path_,
                _DNMM,bits,limit,bloques))
        
        _learning_=(_struct.
            _correlator_DNMM(_pattern_[0],_path_))

        _mem=_struct._pattern_grid(_learning_,limit) 
        
        for pattern in range(len(_pattern_)):
            _dendrite_="";offset=0
            
            for imput in range(4):
                _dendrite_=_pattern_[pattern]
                imput+=offset
                _dendrite_0,_dendrite_1=(_struct.
                    _adapter_bin(_dendrite_[imput],
                        _dendrite_[imput+1])) 
                _neurons,_modeling,_mem_DNMM=(_struct.
                    _layers_(int(_dendrite_0),
                        int(_dendrite_1)))
                offset+=1
                
        return (_mem,_neurons,_modeling,
            _mem_DNMM)

    # @info: INIT
    def _pattern_map_source_parser(self,map_file,
        _DNMM,segmento_pattern,limit_line,bloques=0):
        self.__DNMM_STRUCT=int(_DNMM) 
        _pattern_sequence=[];_crash_sequence=[]
        _binary_copy="";_source_bin=[];_bin_tmp=[]
        _len_frame=""
        
        rnl_source_original = open(map_file,"r")

        for token in rnl_source_original.readlines():
            _binary_copy+=str(token[:-1])
        self.__source_bin.append(_binary_copy)
        rnl_source_original.close()
        _len_frame=len(self.__source_bin[0][:])

        for y in range(len(self.__source_bin[0][:])/8):
            (_crash_sequence.
                append(self.__source_bin[0][y*8:8+(y*8)]))
            
        for x in range(_len_frame):
           self.__adjust_source.append(self.__source_bin[0][x:x+1])
        _pattern_sequence.append(_crash_sequence[0])
        _crash_sequence.pop(0)
        _binary_copy=""

        for token in _crash_sequence:_binary_copy+=str(token)
        _source_bin.append(_binary_copy)
        
        for y in range(len(_source_bin[0])):
            _bin_tmp.append(_source_bin[0][y])
        _source_bin.pop(0)
        _binary_copy=""
        
        for token in _bin_tmp:_binary_copy+=str(token)
        _source_bin.append(_binary_copy)
        rnl_source_original = open(map_file,"w")
        rnl_source_original.write(_source_bin[0]+'\n')
        rnl_source_original.close()
        
        return _pattern_sequence

    #correlador DNMM
    def _correlator_DNMM(self,_binary_pattern_,_path_):
        tokens=[];secuencia=[]
        
        for token in _binary_pattern_:
            if ord(token)==32:token='0'
            tokens.append(int(token))
            
        for x in range(len(tokens)):
            if tokens[x]==1:secuencia.append(x)
        return secuencia

    # @info: Correlador DNMM
    def _adapter_bin(self,_dendrite_0,_dendrite_1):
        if ord(_dendrite_0)==32:_dendrite_0='0'
        if ord(_dendrite_1)==32:_dendrite_1='0'
        
        return _dendrite_0,_dendrite_1

    def _set_(self,pattern,_pattern_):
        
        for token in range(len(self.__base_pattern)):
            self.__base_pattern[token]=0
            
        for token in _pattern_:
            pattern.append(int(token))
            
        for token in pattern: 
            self.__base_pattern[token]=1
        
