
from goto import with_goto
import RnADomainAbs0PcP
from random import randint

# GOTO_module:
# https://app.travis-ci.com/github/snoack/python-goto/builds/218451000
# https://github.com/snoack/python-goto/blob/master/README.md

# app()

# @ciudadano72 
# @autor:Jose Luis Prado Seoane 
# https://github.com/ciudadano72
# https://joseluisprase.wixsite.com/jlps

def cmp(a, b):
    return (a > b) - (a < b)

@with_goto
def _RnA(tolerancia):
    input_=[]
    indices_=[]
    ord_RnA=0
    ord_domain=0
    _structs_=[]

    absDomains=([
    [[[0.013,0.316,0.414,0.011,0.108,0.115,0.103,0.141,0.113,0.115,0.165,0.119,0.126,0.138,0.180], [0.001]]],
    [[[0.013,0.316,0.414,0.011,0.108,0.115,0.103,0.141,0.113,0.115,0.165,0.119,0.126,0.138,0.180], [0.012]]],
    ])

    patternAbs0integrate=[]
    Pattern__=[]
    for Local_matriz in absDomains:
        
        RnA_=(RnADomainAbs0PcP._cell_(int(randint(0,1000)),4,9,500000,0.00000001,4,4,9,4,4,8,8,0))
        
        ord_domain+=1
        label.backend
        
        for valueSensor in range(len(Local_matriz)):
            
            OUT_=RnA_.netlist()
            
            for rst in input_[:]:
                (input_.remove(rst))
                
            for x in range(15):
                (input_.append(Local_matriz[valueSensor][0][x]))
                
            diff=(OUT_[0]-Local_matriz[valueSensor][1][0])
            
            rtn,rdout,y,learningD,size,Wij_neurons,id_=(RnA_.Struct_(
                input_,Local_matriz[valueSensor][1][0],diff,OUT_[0],tolerancia))
            _err_=(((float(rtn)-float(learningD))/
            float(learningD))*100)
           
            _Pattern_=RnA_.MeM_()
            
            OUT_=RnA_.netlist(input_)

            if learningD != rdout :
                for rst in _Pattern_[:]:_Pattern_.remove(rst)
                goto.backend
            Pattern__.append(_Pattern_)

            print (rdout)

        _structs_.append([ord_RnA,learningD,rdout,round(_err_,tolerancia)])
        
        ord_RnA+=1
        for umbral in _structs_:
            abs_0=umbral[0]
            
            if abs_0 not in indices_:
                indices_.append(abs_0)
        patternAbs0integrate=[]
        
        for i in range(len(indices_)):
            patternLocal=[]
            
            for token in range(len(_structs_)):
                if cmp(_structs_[token][0],indices_[i])==0:
                    patternLocal.append(_structs_[token])
                    
            patternAbs0integrate.append(patternLocal)

_RnA(6)
