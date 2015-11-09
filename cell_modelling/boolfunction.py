import cell_modelling.saveload
import os
import random

class BoolFunction(object):
    def __init__(self, K=0, values_string=""):
        current_folder_path = os.path.dirname(__file__)
        self.K = K
        self.values_string = values_string
          
          #self.__class__ = type(self.__class__.__name__, (self.__class__,), {})
          #self.__class__.__call__ = self.evaluate
          
          
          
        #def __getstate__(self): return self.__dict__

        #def __setstate__(self, d): self.__dict__.update(d)

        #def __reduce__(self):
        #  return (BoolFunction, ())
    
    
    
    def __str__(self):
        return self.values_string
    
    def __repr__(self):
        return self.values_string
    
    def generate_random(self, zeroes):    
        for i in range(2**self.K):
            rnd_value = '0' if random.random() < zeroes else '1'
            self.values_string += rnd_value

    def evaluate(self,inputs_string):
        return self.values_string[int(inputs_string,base=2)]

    
    
      
    
      
  
      
