def addSucceedingZeroes(wantedLength,string):
   return '0'*(wantedLength-len(string))+string
   
class State(object):
    def __init__(self, p_state,p_dimension=0,orig=None):
	if orig=None:
	    self.nonCopyConstructor()
	else:
	    if isinstance(orig,State):
		self.copyConstructor()
	    else:
		print "error: orig is not a State."
	    
    def nonCopyConstructor(self,state):
	self.inBasin=False
	self.inAttractor=False
	self.basinNumber=None
	self.weight=0 # for attractor states only
      
      
	if isinstance(state,int):
	    self.stateNumber=p_state
	    self.dimension=p_dimension
	    return
	  
	if isinstance(state,str):
	    self.setState(p_state)
	    return
	    
    def copyConstructor(self,orig):
	self.stateNumber=orig.sate
    
    def inBasin(self):
	if isinstance(self,BasinState
	

    
    def fullOutput(self):
	viewString=""
	"""
    if self.inBasin:
      viewString="BasinState: " + str(self.stateNumber) +", of basin: " + str(self.basinNumber) + ", attracted to state: " + str(self.firstAttractorStateNumber) + "\n" 
      return viewString
      
    if self.inAttractor:
      viewString="AttractorState: " + str(self.stateNumber)+ ", of basin: " + str(self.basinNumber) + ", has weight: " + str(self.weight) + "\n"
      return viewString
	"""
	viewString="FreeState: " + str(self.stateNumber) + "\n"
	return viewString
    
    
    def __str__(self):
	return self.fullOutput()
     
  
    def __repr__(self):
	return self.fullOutput()
    
    def cpy(self):
	newState=State(self.stateNumber,self.dimension)
	return newState
   
  
    def setState(self,state):
	if isinstance(state,str):
	    self.dimension=len(state)
	    self.stateNumber=int(state,base=2)
	    return
      
	if isinstance(state,list):
	    self.stateNumber=0
	    stateString=""
	    for item in state:
		stateString+=str(item)
	    self.stateNumber = int(stateString,base=2)
	    self.dimension = len(state)
	    return
      
	if isinstance(state,int):
	    self.stateNumber=state
	    #todo smth with dimension check
	    return
  
    def asString(self):
	return addSucceedingZeroes(self.dimension,bin(self.stateNumber)[2:])
    
  
    def asList(self):
	aList=[]
	stateString=self.asString()
	for c in stateString:
	    aList.append(c)
	return aList
  
    def asInt(self):
	return self.stateNumber
    
    
class BasinState(State):
    def __init__(self,s_stateObject,s_basinNumber):
	self=State(s_stateObject)
	print "self:",self
	print "in basinstate"	
	
	self.basinNumber=s_basinNumber
	self.firstAttractorStateNumber=None # for basin states only

def main():
    basicState=State(42)
    print basicState
    basicState2=State(basicState)
    print basicState2
    
    basicState.stateNumber=45
    
    print basicState
    
    #basinState=BasinState(basicState,44)
    #print basinState
	
if __name__ == '__main__':
    main()
"""
 state1=State(42,N)
  print state1.stateNumber, state1.dimension
  print state1.asString()
  print state1.asList()
  state1.setState(1)
  print state1
  state1.setState("1111")
  print state1.stateNumber, state1.dimension
  state1.setState([0,1,0,0,0])
  print state1.stateNumber, state1.dimension
  state1=State("0101010")
  print state1.stateNumber,state1.dimension
  
"""
    

    