import nas2
import lib_nas

# Lab

# @ciudadano72 
# @autor:Jose Luis Prado Seoane 
# https://github.com/ciudadano72
# https://joseluisprase.wixsite.com/jlps

def _init_net_():
    n0 = nas2.neuron(0)
    
    for t in range(4):
        print ("\nEspecifique learning binario: ") 

        __learning_logic= int(input ('_logic: '))

        print (lib_nas._memory_2(__learning_logic))
        
        lib_nas._layer_1_1_nasv2(n0,0,lib_nas._memory_2(__learning_logic))

        for x in range(2):
            den_0= int(input ('den_0: '))
            den_1= int(input ('den_1: '))
            den_2= int(input ('den_2: '))
            den_3= int(input ('den_3: '))
            den_4= int(input ('den_4: '))
            den_5= int(input ('den_5: '))
            den_6= int(input ('den_6: '))
            den_7= int(input ('den_7: '))
            n0.ibn_([den_0,den_1,den_2,den_3,den_4,den_5,den_6,den_7])
            
            print ("->> %s") %n0._out_
_init_net_()

# app
def _init_net_2():
    n0 = nas2.neuron(0)
    
    for t in range(2):
        print ("\nEspecifique learning binario: ")  
        
        __learning_logic= int(input ('_logic: '))
        print (lib_nas._memory_2(__learning_logic))
        
        lib_nas._layer_1_1_nasv2(
            n0,0,
            lib_nas._memory_2(__learning_logic))

        for x in range(4): # variar el range 0--256 patterns
            den_0= int(input ('den_0: '))
            den_1= int(input ('den_1: '))
            den_2= int(input ('den_2: '))
            den_3= int(input ('den_3: '))
            den_4= int(input ('den_4: '))
            den_5= int(input ('den_5: '))
            den_6= int(input ('den_6: '))
            den_7= int(input ('den_7: '))
            n0.ibn_([den_0,den_1,den_2,den_3,den_4,den_5,den_6,den_7])

            print (">> %s") %n0._out_
#_init_net_2()
