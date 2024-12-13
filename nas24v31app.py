
import lib_nas
from nas24v31 import _neuron_24v31

# app_local

# @ciudadano72 
# @autor:Jose Luis Prado Seoane 
# https://github.com/ciudadano72
# https://joseluisprase.wixsite.com/jlps

def _init_net_3_(_bias_0, _bias_1):
    neuron_0 = _neuron_24v31(_bias_0,"RNA_grid")
    neuron_1 = _neuron_24v31(_bias_1,"RNA_grid")

    _pattern_0=input ('LEARNING_0: ')
    learning_0=lib_nas._correlator(_pattern_0)
    
    print (_pattern_0)
    print (learning_0)
    
    neuron_0._mapper_(learning_0)
    neuron_0._pattern_grid(learning_0)  

    _pattern_1=input ('LEARNING_1: ')
    learning_1=lib_nas._correlator(_pattern_1)
    neuron_1._mapper_(learning_1)
    neuron_1._pattern_grid(learning_1)
    #neuron_1._mute_(1)
    
    for x in range(1):
        for x in range(4):
            den_0_io= int(input ('den_0: '))
            den_1_io= int(input ('den_1: '))
            
            neuron_0_out=neuron_0._memory_pattern_(den_0_io,den_1_io)   
            print (">> neuron_0: %s") %neuron_0_out
            
            neuron_1_out=neuron_1._memory_pattern_(den_0_io,den_1_io)   
            print (">> neuron_1: %s") %neuron_1_out
            
_init_net_3_(0,1)