
import NaSS

# red neuronal NaSS

# @ciudadano72 
# @autor:Jose Luis Prado Seoane 
# https://github.com/ciudadano72
# https://joseluisprase.wixsite.com/jlps

class _cell_(object):
    def __init__(
        self,id_,dimNaSS,neurons,epoc,corr,dimWij,adj0,adj1,
        denLayer0,denLayer1_0,denLayer1_1,denLayer2,limit
        ):
        self.__Patternsrtn=[]
        self.__RnA=[]
        self.__Wij_neurons=[]
        self.__epoc=int(epoc)
        self.__adj_0=int(adj0)
        self.__adj_1=int(adj1);self.__corr=float(corr)
        self.__limit=float(limit)
        self.__denLayer_0=int(denLayer0)
        self.__denLayer_1_0=int(denLayer1_0)
        self.__denLayer_1_1=int(denLayer1_1)
        self.__denLayer_2=int(denLayer2)
        self.__dinWij=int(dimWij)
        self.__neurons=int(neurons)
        self.__id_ = int(id_)
        self.__ref_class = (self.__class__.__name__+"_" + str(self.__id_))
        
        for x in range (int(neurons)):
            (self.__RnA.append(NaSS._n_(x,int(dimNaSS))))

    def netlist(self,input_=[0,0,0,0]):
                  vector=[]
        # LAYER_0:
                  for x in range(self.__denLayer_0):
                      vector.append(input_[x])
                  for layer_0 in range(self.__denLayer_0):
                      
                      self.__RnA[layer_0].ibn_(vector)
                      
                  for rst in vector[:]:
                      vector.remove(rst)
        # LAYER_1:
                  for x in range(self.__denLayer_0):
                      vector.append(self.__RnA[x]._out_)
                  for layer_1 in range(
                    self.__denLayer_1_0,self.__denLayer_1_1):
                      
                      self.__RnA[layer_1].ibn_(vector)
                      
                  for rst in vector[:]:
                      vector.remove(rst)
        # LAYER_2:
                  for x in range(
                    self.__denLayer_1_0,self.__denLayer_1_1):
                      vector.append(self.__RnA[x]._out_)
                      
                  self.__RnA[self.__denLayer_2].ibn_(vector)
                  
                  for rst in vector[:]:
                      vector.remove(rst)
                      
                  return [self.__RnA[self.__denLayer_2]._out_]

    # @def:__MeM
    def MeM_(self):
        for x in range(self.__neurons):
            self.__Patternsrtn.append(self.__Wij_neurons[x])

        return self.__Patternsrtn

    # @def:__Learning
    def Struct_(self,input_,learning,diff,OUT,tolerancia):
        y=0.0;diff_c=0.0
        size=len(str(learning))
        
        for rst in self.__Wij_neurons[:]:
            (self.__Wij_neurons.remove(rst))
            
        for x in range(self.__epoc):
            if diff > self.__limit:
                y=y-self.__corr
            elif diff < self.__limit:
                y=y+self.__corr
                
            for neuron in range(self.__adj_0,self.__adj_1):
                self.__RnA[neuron]._WijP([y,y,y,y])
                
            OUT_=self.netlist(input_)
            
            diff_c=(OUT_[0]-learning)

            if (diff > self.__limit and diff_c < self.__limit):break
            elif (diff < self.__limit and diff_c > self.__limit):break
            
        for x in range(self.__neurons):
            (self.__Wij_neurons.append(self.__RnA[x].get_Wij()[:self.
            __dinWij]))
        return (OUT_[0],
            round(OUT_[0],tolerancia),y,
            learning,size,self.__Wij_neurons,self.__ref_class )
