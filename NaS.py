
import sys
import math
import random

# NaS.py
# Neuron artificial 

# @ciudadano72 
# @autor:Jose Luis Prado Seoane 
# https://github.com/ciudadano72
# https://joseluisprase.wixsite.com/jlps

class _n_(object):
    def __init__(self,id_):
        self._learn=0
        self._out_ = 0.0
        self._offset=0.0
        self._Wij=[]
        self.__selector=0
        self._SuM_DenWij=0
        self.__id_ = int(id_)
        self.__ref_class = (self.
            __class__.__name__+
            "_" + str(self.__id_))
        
        self.__memory_ = ("rnl_sinap_ia_"+self.
            __ref_class)
        self.__vector_neuron=[]

    # @def:SuM
    def get_DenWij(self):
        return self._SuM_DenWij
    
    # @def:Set umbral
    def get_Wij(self):
        return self._Wij

    # @def:Set umbral
    def setWij(self,Wij):
        self._learn=1
        for rst in self._Wij[:]:
            (self._Wij.remove(rst))               
        for x in range(4): #----Pragma Mark
            self._Wij.append(Wij[x])
            
    def func_a(self):
        for i in range(len(self.__vector_neuron)):
            self._SuM_DenWij = (self._SuM_DenWij+(self.__vector_neuron[i]*self._Wij[i]))
        
    # @def:__Sinap
    def ibn_(self,tensor_den):
        self._SuM_DenWij=0
        
        if self._learn==0:
            if self.__selector==0:
                for rst in self._Wij[:]:
                    (self._Wij.remove(rst)) 
                for rst in self.__vector_neuron[:]:
                    (self.__vector_neuron.remove(rst)) 
                for _input_ in tensor_den:
                    (self.__vector_neuron.append(float(_input_)))
                for x in range(len(self.__vector_neuron)):
                    self._Wij.append(random.uniform(-1,1))
            elif self.__selector==1:
                self.func_a()       
        elif self._learn==1:
            print ("Memory %s") %self._Wij
            self.func_a() 
        func_a = 1 / (1 + math.exp(-self._SuM_DenWij))
        self._out_ = float(func_a)
        self._learn=0
        self.__selector==0

    # @def:__Learning
    def _WijP(self,factor_Wij):
        self.__selector=1 
        for t in range(len(factor_Wij)): #2
            self._Wij[t]=(float(self._Wij[t]+factor_Wij[t]))
