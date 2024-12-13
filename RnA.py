
import lib_nas
import LearningCell

# Netlist

# @ciudadano72 
# @autor:Jose Luis Prado Seoane 
# https://github.com/ciudadano72
# https://joseluisprase.wixsite.com/jlps

class _LearningRnA_(object):
    def __init__(self,id_,tolerancia,epoc,corr,LenT,absDomains):
        self.__id_ = int(id_)
        self.__epoc=epoc; self.__corr=corr
        self.__absDomains=absDomains
        self.__tolerancia=int(tolerancia)
        self.__LenT=int(LenT)

    def _sinapsis_(self):
        Cell_0=LearningCell._LearningCell_(
            self.__tolerancia,self.__epoc,
            self.__corr,self.__LenT,self.__absDomains)
        
        OUT_,Pattern=Cell_0._sinapsis_()
        
        return OUT_,Pattern
