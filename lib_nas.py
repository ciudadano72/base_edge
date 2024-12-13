
import sys

#lib_nas.py
#libreria Neuronal basica (parcial) --Lib

# @ciudadano72 
# @autor:Jose Luis Prado Seoane 
# https://github.com/ciudadano72
# https://joseluisprase.wixsite.com/jlps

def cmp(a, b):
    return (a > b) - (a < b)

# @info: Version Base
def _layer_1_1_(_neuron,_idnas,_learn):
    
    def neuron_0():
        _neuron.rst_sign_()
        _neuron.ibn_(0,0,int(_learn[0]))
        _neuron.ibn_(0,1,int(_learn[1]))
        _neuron.ibn_(1,0,int(_learn[2]))
        _neuron.ibn_(1,1,int(_learn[3]))
        
    __rst_sign = {0 : neuron_0,}
    __rst_sign [int(_idnas)]()

#Balanceador funci0n -6 modos-
def _memory_(id_mode):
    def s0():global _learn;_learn=[0,0,0,1]
    def s1():global _learn;_learn=[1,1,1,0]
    def s2():global _learn;_learn=[0,1,1,1]
    def s3():global _learn;_learn=[1,0,0,0]
    def s4():global _learn;_learn=[0,1,1,0]
    def s5():global _learn;_learn=[1,0,0,1]
    __learn = {0 : s0,1 : s1,2 : s2,3 : s3,4 : s4,5 : s5,}
    __learn [int(id_mode)]()
    return _learn

def _epoc_(id_mode):
    def s0():global _learn;_learn=100000
    def s1():global _learn;_learn=200000
    def s2():global _learn;_learn=300000
    def s3():global _learn;_learn=400000
    def s4():global _learn;_learn=500000
    __learn = {0 : s0,1 : s1,2 : s2,3 : s3,4 : s4,}
    __learn [int(id_mode)]()
    return int(_learn)

#Balanceador NASV2
def _memory_2(id_mode):
    def s0():global _learn;_learn=[0,1]
    def s1():global _learn;_learn=[1,0]
    def s2():global _learn;_learn=[0,1]
    def s3():global _learn;_learn=[1,0]
    def s4():global _learn;_learn=[0,1]
    def s5():global _learn;_learn=[1,0]
    __learn = {0 : s0,1 : s1,2 : s2,3 : s3,4 : s4,5 : s5,}
    __learn [int(id_mode)]()
    return [_learn,id_mode]

#SET: NASV2
def _layer_1_1_nasv2(_neuron,_idnas,_learn):
    def neuron_0():
        bin_2=[0,1];_inputs_=[]
        for b0 in bin_2:
            for b1 in bin_2:
                for b2 in bin_2:
                    for b3 in bin_2:
                        for b4 in bin_2:
                            for b5 in bin_2:
                                for b6 in bin_2:
                                    for b7 in bin_2:
                                        (_inputs_.
                                            append([b0,b1,b2,b3,b4,b5,b6,b7]))
        _neuron.rst_sign_();
        if _learn[1]==0 or _learn[1]==1:
            for den_ in range(255):
                (_neuron.ibn_(_inputs_[den_],int(_learn[0][0])))
            (_neuron.
                ibn_(_inputs_[255],int(_learn[0][1])))
        elif _learn[1]==2 or _learn[1]==3:
            (_neuron.ibn_(_inputs_[0],int(_learn[0][0])))
            for den_ in range(1,256):
                (_neuron.ibn_(_inputs_[den_],int(_learn[0][1])))
        elif _learn[1]==4 or _learn[1]==5:
            (_neuron.ibn_(_inputs_[0],int(_learn[0][0])))
            (_neuron.ibn_(_inputs_[255],int(_learn[0][0])))
            for den_ in range(1,255):
                (_neuron.ibn_(_inputs_[den_],int(_learn[0][1])))
    __rst_sign = {0 : neuron_0,}
    __rst_sign [int(_idnas)]()

# @info: Version extendida
def _layer_1_2_(_neuron,_idnas,_learn):
    def neuron():
        _neuron.rst_sign_()
        _neuron.ibn_(0,0,int(_learn[0]))
        _neuron.ibn_(0,1,int(_learn[1]))
        _neuron.ibn_(1,0,int(_learn[2]))
        _neuron.ibn_(1,1,int(_learn[3]))
    __rst_sign = {int(_idnas) : neuron,}
    __rst_sign [int(_idnas)]()

#Balanceador funci0n -6 modos-
def _memory_3(id_mode):
    def s0():global _learn;_learn=[0,0,0,0,0,0,0,1]
    def s1():global _learn;_learn=[1,1,1,1,1,1,1,0]
    def s2():global _learn;_learn=[0,1,1,1,1,1,1,1]
    def s3():global _learn;_learn=[1,0,0,0,0,0,0,0]
    __learn = {0 : s0,1 : s1,2 : s2,3: s3,}
    __learn [int(id_mode)]()
    return _learn

# Balanceador neuronal de funcion -6 modos-
def _memory_basic(id_mode):
    def s0():global _learn_;i0=0;i1=0;i2=0;i3=1;_learn_= str(i0) + str(i1) + str(i2) + str(i3) #AND
    def s1():global _learn_;i0=1;i1=1;i2=1;i3=0;_learn_= str(i0) + str(i1) + str(i2) + str(i3) #NAND
    def s2():global _learn_;i0=0;i1=1;i2=1;i3=1;_learn_= str(i0) + str(i1) + str(i2) + str(i3) #OR
    def s3():global _learn_;i0=1;i1=0;i2=0;i3=0;_learn_= str(i0) + str(i1) + str(i2) + str(i3) #NOR
    def s4():global _learn_;i0=0;i1=1;i2=1;i3=0;_learn_= str(i0) + str(i1) + str(i2) + str(i3) #XOR
    def s5():global _learn_;i0=1;i1=0;i2=0;i3=1;_learn_= str(i0) + str(i1) + str(i2) + str(i3) #XNOR
    __learn = {0 : s0,1 : s1,2 : s2,3 : s3,4 : s4,5 : s5,};__learn [int(id_mode)]()
    return _learn_

#correlador General
def _correlator(_binary_pattern_):
    tokens=[];secuencia=[]
    
    for token in _binary_pattern_:
        tokens.append(int(token))
        
    for x in range(len(tokens)):
        if tokens[x]==1:secuencia.append(x)
        
    return secuencia

# Balanceador de aprendizaje -4 estados-
def _pattern_nas_v10(__dendrite_0,__dendrite_1,_out_nas,_pattern):
    _bin_ = str(bin(__dendrite_0) + bin(__dendrite_1))
    _mem_ = (_bin_[2] + _bin_[5])
    
    def s_00():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[0])) != 0]
    def s_01():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[1])) != 0]
    def s_10():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[2])) != 0]
    def s_11():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[3])) != 0]
    __balancer = {"00" : s_00,"01" : s_01,"10" : s_10,"11" : s_11,}
    __balancer [_mem_]()
    
    return _balancer_

# Balanceador de aprendizaje -4 estados-
def _pattern_nas(__dendrite_0,__dendrite_1,_out_nas,_pattern):
    _bin_ = str(bin(__dendrite_0) + bin(__dendrite_1))
    _mem_ = (_bin_[2] + _bin_[5])
    
    def mem_pattern(index):
        global _balancer_
        _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[int(index)])) != 0]
    __balancer = {"adaptative" : mem_pattern,}
    __balancer ["adaptative"](int(str(_mem_), 2))
    
    return _balancer_

#Balanceador aprendizaje -256 estados-
def _pattern_nas_256(__den_0,__den_1,__den_2,__den_3,__den_4,
    __den_5,__den_6,__den_7,_out_nas,_pattern):
    _bin_ = (str(bin(__den_0)+bin(__den_1)+bin(__den_2)+
        bin(__den_3)+bin(__den_4)+bin(__den_5)+bin(__den_6)+bin(__den_7)))
    _mem_=(_bin_[2]+_bin_[5]+_bin_[8]+_bin_[11]+_bin_[14]+_bin_[17]+_bin_[20]+_bin_[23])
    
    def mem_pattern(index):
        global _balancer_
        _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[int(index)])) != 0]
    __balancer = {"adaptative" : mem_pattern,}
    __balancer ["adaptative"](int(str(_mem_), 2))
    
    return _balancer_

# Balanceador aprendizaje -16 estados-
def _pattern_nas_16_v10(__dendrite_0,__dendrite_1,__dendrite_2,__dendrite_3,_out_nas,_pattern):
    _bin_ = str(bin(__dendrite_0)+bin(__dendrite_1)+bin(__dendrite_2)+bin(__dendrite_3))
    _mem_=(_bin_[2]+_bin_[5]+_bin_[8]+_bin_[11])
    
    def s_0000():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[0])) != 0]
    def s_0001():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[1])) != 0]
    def s_0010():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[2])) != 0]
    def s_0011():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[3])) != 0]
    def s_0100():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[4])) != 0]
    def s_0101():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[5])) != 0]
    def s_0110():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[6])) != 0]
    def s_0111():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[7])) != 0]
    def s_1000():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[8])) != 0]
    def s_1001():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[9])) != 0]
    def s_1010():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[10])) != 0]
    def s_1011():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[11])) != 0]
    def s_1100():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[12])) != 0]
    def s_1101():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[13])) != 0]
    def s_1110():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[14])) != 0]
    def s_1111():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[15])) != 0]
    
    __balancer = {"0000" : s_0000,"0001" : s_0001,"0010" : s_0010,"0011" : s_0011,
                  "0100" : s_0100,"0101" : s_0101,"0110" : s_0110,"0111" : s_0111,
                  "1000" : s_1000,"1001" : s_1001,"1010" : s_1010,"1011" : s_1011,
                  "1100" : s_1100,"1101" : s_1101,"1110" : s_1110,"1111" : s_1111,}
    __balancer [_mem_]()
    
    return _balancer_

# Balanceador de aprendizaje -16 estados-

def _pattern_nas_16(__dendrite_0,__dendrite_1,__dendrite_2,__dendrite_3,_out_nas,_pattern):
    _bin_ = str(bin(__dendrite_0)+bin(__dendrite_1)+bin(__dendrite_2)+bin(__dendrite_3))
    _mem_=(_bin_[2]+_bin_[5]+_bin_[8]+_bin_[11])
    
    def mem_pattern(index):
        global _balancer_
        _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[int(index)])) != 0]
    __balancer = {"adaptative" : mem_pattern,}
    __balancer ["adaptative"](int(str(_mem_), 2))
    
    return _balancer_
