def add_succeeding_zeroes(wanted_length,string):
   return '0'*(wanted_length-len(string))+string
   
class State(object):
  def __init__(self, p_state,p_dimension=0):
      self.in_basin=False
      self.in_attractor=False
      self.basin_number=None
      self.weight=0 # for attractor states only
      self.first_attractor_state_number=None # for basin states only
      
      if isinstance(p_state,int):
        self.state_number=p_state
        self.dimension=p_dimension
        return

      if isinstance(p_state,str):
        self.set_state(p_state)
        return

    
  def full_output(self):
    view_string=""
    if self.in_basin:
      view_string="BasinState: " + str(self.state_number) +", of basin: " + str(self.basin_number) + ", attracted to state: " + str(self.first_attractor_state_number) + "\n" 
      return view_string
      
    if self.in_attractor:
      view_string="AttractorState: " + str(self.state_number)+ ", of basin: " + str(self.basin_number) + ", has weight: " + str(self.weight) + "\n"
      return view_string
    
    view_string="FreeState: " + str(self.state_number) + "\n"
    return view_string
    
    
  def __str__(self):
    return self.full_output()
     
  
  def __repr__(self):
    return self.full_output()
    
  def cpy(self):
    new_state=State(self.state_number,self.dimension)
    return new_state
   
  
  def set_state(self,state):
    if type(state)==type(""):
      self.dimension=len(state)
      self.state_number=int(state,base=2)
      return
      
    if type(state)==type([]):
      self.state_number=0
      state_string=""
      for item in state:
        state_string+=str(item)
      self.state_number = int("0b"+state_string,base=2)
      self.dimension = len(state)
      return
      
    if type(state)==type(0):
      self.state_number=state
      #todo smth with dimension check
      return
  
  def as_string(self):
    return add_succeeding_zeroes(self.dimension,bin(self.state_number)[2:])
    
  
  def as_list(self):
    a_list=[]
    state_string=self.as_string()
    for c in state_string:
      a_list.append(c)
    return a_list
  
  def as_int(self):
    return self.state_number
    
"""
 state1=State(42,N)
  print state1.state_number, state1.dimension
  print state1.as_string()
  print state1.as_list()
  state1.set_state(1)
  print state1
  state1.set_state("1111")
  print state1.state_number, state1.dimension
  state1.set_state([0,1,0,0,0])
  print state1.state_number, state1.dimension
  state1=State("0101010")
  print state1.state_number,state1.dimension
  
"""
    

    