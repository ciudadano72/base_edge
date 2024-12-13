
import nas
import lib_nas
from random import randint
from goto import with_goto

# @ciudadano72 
# @autor:Jose Luis Prado Seoane 
# https://github.com/ciudadano72
# https://joseluisprase.wixsite.com/jlps

def _init_net_():
    n0 = nas.neuron(0)
    
    while True:
        print ("\nEspecifique learning binario: ")  
        
        __learning_logic= int(raw_input ('_logic: '))
        
        lib_nas._layer_1_1_(n0,0,lib_nas._memory_(__learning_logic))

        try:
            __pesos_wij = open('rnl_sinap_ia_neuron_0','r')
            for Wij in __pesos_wij:
                print(Wij)
        except IOError:
          print ('No pueden abrir los pesos neuronales: %s') %n0.__class__.__name__
        else:
          __pesos_wij.close()

        for x in range(4):
            den_0= int(input ('den_0: '))
            den_1= int(input ('den_1: '))
            n0.ibn_(den_0,den_1)
            print (">> %s") %n0._out_

_init_net_()