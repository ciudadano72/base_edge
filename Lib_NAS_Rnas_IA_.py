
import random
from goto import with_goto

# GOTO_module:
# https://app.travis-ci.com/github/snoack/python-goto/builds/218451000
# https://github.com/snoack/python-goto/blob/master/README.md


#lib_NAS_Rnas_IA.py
#libreria ampliada --Lib

# @ciudadano72 
# @autor:Jose Luis Prado Seoane 
# https://github.com/ciudadano72
# https://joseluisprase.wixsite.com/jlps


# @info: Funcion de aprendizaje
@with_goto
def _func_learning(_neuron_seq_,_inputs_den_,
_grid_RnA_,_pattern_learning_,_bias_out_,pattern_learned_grid):
    base_neurons=[];base_learning=[]
    neurons_rdm=[];pattern_learned=[]
    counter=0;base=0
    
    for x in range(len(_grid_RnA_)):
        (base_neurons.append(_bias_learning(0)[0:]))
        (pattern_learned.append(_bias_learning(0)[0:]))
        
    for token in _pattern_learning_:
        (base_learning.append(int(token)))
        
    if _bias_out_!=base_learning[int(_neuron_seq_)]:
        label.backend
        neuron_id_rdm=random.randrange(len(_grid_RnA_))
        
        if neuron_id_rdm not in neurons_rdm:
            (_grid_RnA_[neuron_id_rdm]._pattern_grid(_bias_learning(1)))
            n_0_out=(_grid_RnA_[0]._memory_pattern_(_inputs_den_[0],_inputs_den_[1]))
            n_1_out=(_grid_RnA_[1]._memory_pattern_(_inputs_den_[0],_inputs_den_[1]))
            n_2_out=(_grid_RnA_[2]._memory_pattern_(n_0_out,n_1_out))
            
            if (base_learning[0]==1 and
                base_learning[1]==0 and
                base_learning[2]==0 and
                base_learning[3]==0 and
                n_2_out==0 and
                base_learning[_neuron_seq_]==1):
                counter+=1
                
                if counter>=2:
                    counter=0
                    base=0
            else:
                base=base_learning[_neuron_seq_]
                
            if n_2_out!=base:
                neurons_rdm.append(neuron_id_rdm)
                pattern_learned[neuron_id_rdm]=(_bias_learning(1))
                goto.backend
                
                (_grid_RnA_[neuron_id_rdm]._pattern_grid(_bias_learning(0)))
            else:
                pattern_learned[neuron_id_rdm]=(_bias_learning(1))
                (pattern_learned_grid.append(pattern_learned))
                
                (_grid_RnA_[neuron_id_rdm]._pattern_grid(_bias_learning(0)))
        else:
            goto.backend
    else:
        (pattern_learned_grid.append(pattern_learned))
    for id_neuron in range(len(_grid_RnA_)):
        (_grid_RnA_[id_neuron]._pattern_grid(_bias_learning(0)))
    return pattern_learned_grid

def _st_errs_ (id_state):
    def _st0():global _state;_state="333"
    def _st1():global _state;_state="303"
    def _st2():global _state;_state="033"
    def _st3():global _state;_state="300"
    __state = ({0 : _st0,1 : _st1,2 : _st2,3 : _st3,})
    __state [int(id_state)]()
    
    return _state

def _matrix_pos_ (id_matrix):
    def _p1():global _matrix_pos;_matrix_pos=1
    def _p2():global _matrix_pos;_matrix_pos=2
    def _p3():global _matrix_pos;_matrix_pos=3
    def _p4():global _matrix_pos;_matrix_pos=4
    def _p5():global _matrix_pos;_matrix_pos=5
    def _p6():global _matrix_pos;_matrix_pos=6
    def _p7():global _matrix_pos;_matrix_pos=7
    def _p8():global _matrix_pos;_matrix_pos=8
    def _p9():global _matrix_pos;_matrix_pos=9
    def _p10():global _matrix_pos;_matrix_pos=10
    def _p11():global _matrix_pos;_matrix_pos=11
    def _p12():global _matrix_pos;_matrix_pos=12
    def _p13():global _matrix_pos;_matrix_pos=13
    def _p14():global _matrix_pos;_matrix_pos=14
    def _p15():global _matrix_pos;_matrix_pos=15
    def _p16():global _matrix_pos;_matrix_pos=16
    __state = ({'11' : _p1,'21' : _p2,'31' : _p3,'41' : _p4,
                '12' : _p5,'22' : _p6,'32' : _p7,'42' : _p8,
                '13' : _p9,'23' : _p10,'33' : _p11,'43' : _p12,
                '14' : _p13,'24' : _p14,'34' : _p15,'44' : _p16,})
    __state [str(id_matrix)]()
    
    return _matrix_pos

def _st_bin_2 (id_state):
    def _st0():global _state;_state="00"
    def _st1():global _state;_state="01"
    def _st2():global _state;_state="10"
    def _st3():global _state;_state="11"
    __state = ({0 : _st0,1 : _st1,2 : _st2,3 :_st3,})
    __state [int(id_state)]()
    
    return _state

def _cypher (id_):
    def _DES():global _cypher;_cypher="12345678"
    __state = ({0 : _DES,})
    __state [int(id_)]()
    
    return _cypher

def _st(id_state):
    def _st0():global _state;_state="1000"
    def _st1():global _state;_state="0100"
    def _st2():global _state;_state="0010"
    def _st3():global _state;_state="0001"
    def _st4():global _state;_state="0110"
    def _st5():global _state;_state=['0000',
    '0001','0010','0011','0100','0101','0110',
    '0111','1000','1001','1010','1011','1100',
    '1101','1110','1111']
    __state = ({0 : _st0,1 : _st1,2 : _st2,3 :
        _st3,4 : _st4,5 : _st5,})
    __state [int(id_state)]()
    
    return _state

def _parser_object(_object_):
    def _token_0():global _tokens;_tokens="Profile_Object.*|    id.*|    posx.*|    posy1.*|    DeathO.*|    join:.*|  Object-end.*"
    def _token_1():global _tokens;_tokens="Profile_Object"
    def _token_2():global _tokens;_tokens="  Object-end"
    __state = ({'tokens' : _token_0,'open' : _token_1,'close' : _token_2,})
    __state [str(_object_)]()
    
    return _tokens

def _st_parser (id_state):
    def _st0():global _state;_state='Profile_Object:'
    def _st1():global _state;_state='id'
    def _st2():global _state;_state='posx'
    def _st3():global _state;_state='posy1'
    def _st4():global _state;_state='DeathO'
    def _st5():global _state;_state='join:'
    __state = ({0 : _st0,1 : _st1,2 : _st2,3 :_st3,4 :_st4,5 :_st5,})
    __state [int(id_state)]()
    
    return _state

def _neuron(neuron_id):
    def mem_pattern(index):global _id_neuron;_id_neuron='neuron_'+str(index)
    __id_neuron = {"neuron" : mem_pattern,}
    __id_neuron ["neuron"](int(neuron_id))
    
    return str(_id_neuron)

def _len_source(_path_):
    token=0
    _source = open(_path_,"r")
    
    for linea in _source:
        token+=len(linea[:-1])
    
    return int((token/8)+1)

#correlador DNMM
def _correlator_DNMM(_binary_pattern_,_path_):
    tokens=[];secuencia=[]
    
    for token in _binary_pattern_:
        if ord(token)==32:token='0'
        tokens.append(int(token))
        
    for x in range(len(tokens)):
        if tokens[x]==1:secuencia.append(x)
    return secuencia

#Polarizador and [3] /nand [0,1,2]
def _bias_learning(id_mode_state):
    def s0():global _pattern;_pattern=[3]
    def s1():global _pattern;_pattern=[0,1,2]
    __pattern = {0 : s0,1 : s1,}
    __pattern [int(id_mode_state)]()
    
    return _pattern

#correlador DNMM
def _adapter_bin(_dendrite_0,_dendrite_1):
    if ord(_dendrite_0)==32:_dendrite_0='0'
    if ord(_dendrite_1)==32:_dendrite_1='0'
    return _dendrite_0,_dendrite_1

def _neuron_matriz(neuron_id):
    def mem_pattern(index):global _id_neuron;_id_neuron='n'+str(index)
    __id_neuron = {"neuron" : mem_pattern,}
    __id_neuron ["neuron"](int(neuron_id))
    return str(_id_neuron)
