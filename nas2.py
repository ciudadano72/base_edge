
import random
import os.path
from goto import with_goto

# https://app.travis-ci.com/github/snoack/python-goto/builds/218451000
# https://github.com/snoack/python-goto/blob/master/README.md

# Neuron nas2.py (v2()) --Dimension (Inputs): 8 Bits (Byte)

# Formato (RamDisk)................................................................................
#['neuron_0', '00000000', 0.45850301377748925, 0.16083532993829508, 0.4806212011207709,....]
#['neuron_0', '00000001', -0.3318987541981926, -0.1271516008337673, -0.1706896578960917,...]
#['neuron_0', '00000010', -0.3041522393974597, -0.603140026446308, -0.4990531067269519,....]
#['neuron_0', '00000011', -0.17675953152131363, -0.44938666768423363, -0.9051075360268186,.]
# .................................................................................................
# TENSOR : array (8 Bits)--Byte/s (Inputs == Dimension)

# @ciudadano72 
# @autor:Jose Luis Prado Seoane 
# https://github.com/ciudadano72
# https://joseluisprase.wixsite.com/jlps

class neuron(object):
    def __init__(self,id_):
        self.__learning = 0.5
        self.__id_ = int(id_)
        
        self.__ref_class = (self.__class__.__name__+
            "_" + str(self.__id_))
        
        self.__memory_ = "rnl_sinap_ia_"+self.__ref_class
        self.__inputs_neuron=[]
    
    def cmp(self,a, b):
        return (a > b) - (a < b)

    # @def:__inputs__
    def ibn_(self,inputs_array,axon_ptron=11):        
        for _input_ in inputs_array:
            self.__inputs_neuron.append(int(_input_))
            
        self.__axon_ptron_out = int(axon_ptron)
        self._out_ = 0
        
        if self.__axon_ptron_out != 11:
            self.sinap()
        else:
            (self._memory_back_sinap(self.
                __inputs_neuron))
        for rst in self.__inputs_neuron[:]:
            (self.__inputs_neuron.remove(rst))

    # @def:Reseat __memory__
    def rst_sign_(self):
        if os.path.exists(self.__memory_) != 0:
            os.remove(self.__memory_)

    # @def:__sinaptica__
    @with_goto
    def sinap(self):
        pesos=[];_mem_=[];entradas=[]

        for _input_ in self.__inputs_neuron:
            entradas.append(int(_input_))
        for x in range(len(entradas)):
            pesos.append(random.uniform(0,1))
            
        salida=0;corrector=0
        label.backend
        
        sumatoria = (self.
            funcionActivacion(entradas,pesos))
        
        if sumatoria > 0:
            salida=1
            corrector = -2.0
        elif sumatoria<=0:
            salida=0
            corrector = 2.0

        if self.cmp(salida,self.__axon_ptron_out)!=0:
            for i,x in enumerate(pesos):
                if self.__axon_ptron_out == 0:
                    pesos[i]=(pesos[i]+
                        (corrector*self.__learning))
                elif self.__axon_ptron_out == 1:
                    salida = 1
                    goto.frontend
            goto.backend
            
        else:
            label.frontend
            rnl_map_sinap = open(self.__memory_,"a+")
            
            _bin_ = (str(
                bin(entradas[0])+bin(entradas[1]) + 
                bin(entradas[2])+bin(entradas[3]) + 
                bin(entradas[4])+bin(entradas[5]) + 
                bin(entradas[6])+bin(entradas[7])))
            _mem_.append(self.__ref_class)
            (_mem_.append(
                _bin_[2]+_bin_[5]+_bin_[8]+_bin_[11]+
                _bin_[14]+_bin_[17]+_bin_[20]+_bin_[23]))
            _mem_.append(pesos[0]);_mem_.append(pesos[1])
            _mem_.append(pesos[2]);_mem_.append(pesos[3])
            _mem_.append(pesos[4]);_mem_.append(pesos[5])
            _mem_.append(pesos[6]);_mem_.append(pesos[7])
            _mem_.append(sumatoria)
            
            rnl_map_sinap.write(str(_mem_) + '\n')
            rnl_map_sinap.close()

    # @def:__back_with_learning
    @with_goto
    def _memory_back_sinap(self,entradas):
        adrr_memory = [];pesos=[];_offset_= 1
        _bin_ = (str(
            bin(entradas[0]) + bin(entradas[1]) + 
            bin(entradas[2])+bin(entradas[3]) + 
            bin(entradas[4])+bin(entradas[5]) + 
            bin(entradas[6])+bin(entradas[7])))
        _mem_=(
            _bin_[2]+_bin_[5]+_bin_[8]+_bin_[11]+
            _bin_[14]+_bin_[17]+_bin_[20]+_bin_[23])
        rnl_map_sinap = open(self.__memory_,"r")
        v_offset_ = str(self.__id_);_offset_ = len(v_offset_)
        
        for w_ibn in rnl_map_sinap.readlines():
            if (w_ibn[14+(_offset_-1):22+(_offset_-1)])==_mem_:
                for match_ in range(2,10):
                    (adrr_memory.
                        append(w_ibn.split(',')[match_]))
                break
        rnl_map_sinap.close()
        
        for w_ret in adrr_memory:
            pesos.append(float(w_ret))
        sumatoria = (self.
            funcionActivacion(entradas,pesos))
        if sumatoria > 0:self._out_=1
        elif sumatoria<=0:self._out_=0

    # @def:__func_activacion__
    def funcionActivacion(self,entradas,pesos):
        sumatoria=0
        
        for i in range(len(entradas)):
            sumatoria = sumatoria+(entradas[i]*pesos[i])
            
        if sumatoria == 0.0:
            for i in range(len(entradas)):
                sumatoria = sumatoria + (1 * pesos[i])
                return sumatoria
        else:
            return sumatoria


