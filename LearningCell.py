import Cell
from goto import with_goto
from goto.goto import goto
from random import randint

# GOTO_module:
# https://app.travis-ci.com/github/snoack/python-goto/builds/218451000
# https://github.com/snoack/python-goto/blob/master/README.md
# learning

# @ciudadano72 
# @autor:Jose Luis Prado Seoane 
# https://github.com/ciudadano72
# https://joseluisprase.wixsite.com/jlps

# @class
class _LearningCell_(object):
    def __init__(self,tolerancia,epoc,corr,LenT,absDomains):
        self.__epoc=epoc; self.__corr=corr
        self.__absDomains=absDomains
        self.__tolerancia=tolerancia
        self.__LenT=int(LenT)
        self.__rx=[]

    @with_goto
    def _sinapsis_(self):
        input_=[]
        ord_domain=0

        for Local_matriz in self.__absDomains:
            print (Local_matriz)
            
            RnA_=(Cell._cell_(int(randint(0,1000)),4,9,self.__epoc,self.__corr,4,4,9,4,4,8,8,0))
            
            ord_domain+=1
            label.backend
            
            for valueSensor in range(len(Local_matriz)):
                
                OUT_=RnA_.netlist()
                
                for rst in input_[:]:
                    (input_.remove(rst))
                    
                for x in range(int(self.__LenT)):
                    (input_.append(Local_matriz[valueSensor][0][x]))
                    
                diff=(OUT_[0]-Local_matriz[valueSensor][1][0])
                rtn,rdout,y,learningD,size,Wij_neurons,id_=(RnA_.Struct_(
                    input_,Local_matriz[valueSensor][1][0],diff,OUT_[0],self.__tolerancia))
                _err_=(((float(rtn)-float(learningD))/
                float(learningD))*100)
                
                _Pattern_=RnA_.MeM_()
                
                OUT_=RnA_.netlist(input_)
                
                if learningD != rdout :
                    goto.backend
                self.__rx.append([_Pattern_,rdout])
                
        return self.__rx
