global globalFunctionsAmount
global summ
summ =0
globalFunctionsAmount=0

from Automata import NK_Automata

from ProxyFunctions import decimalIntToBinaryList
from Debug import log

import AutomataProssesing
import ProxyFunctions
import BoolFunction

# not working correctly
def throughAllCollocations(fromAmount,byAmount):
    # eg: throughAllCollocations(3,2)=[[1,2],[1,3],[2,1],[2,3]...]
    elementsToCollocateList=range(fromAmount)
    return throughAllCollocationsRecursive(elementsToCollocateList,byAmount)
    
def throughAllCollocationsRecursive(elementsToCollocateList,byAmount):
    reList=[]
    if byAmount==0:
	return []
    for i in range(len(elementsToCollocateList)):
	item=elementsToCollocateList[i]
	elementsToCollocateListWithoutItem=elementsToCollocateList[:]
	del elementsToCollocateListWithoutItem[i]
	recursiveList=throughAllCollocationsRecursive(elementsToCollocateListWithoutItem,byAmount-1)
	print recursiveList
	
	if len(recursiveList)==0:
	    return [[item]]
	    
	for j in range(len(recursiveList)):
	    recursiveItem=recursiveList[j]
	    
	    reList+=[[item]+recursiveItem]
    return reList
    
def throughAllCombinations(fromAmount,byAmount):
    
    # from 3 by 2: [1,2], [1,3], [2,3]
    """
    [1,2,3][]
    [2,3] [1]
    [3] [1,2] <--
    [2,3] [1]
    [2] [1,3] <--
    [2,3] [1]
    [1,2,3][] 
    [2,3]  []
    [3]   [2]
    []  [2,3] <--
    [3]   [2]
    [2,3]  []
    """
    """
    [1,2,3,4][]
    [2,3,4] [1]
    [3,4] [1,2] <--
    [2,3,4] [1]
    [2,4] [1,3] <--
    [2,3,4] [1] 
    [2,3] [1,4] <--
    [2,3,4] [1] 
    [2,3,4] []   
    
    []
    """
    """
    [1,2,3,4][]
    [2,3,4] [1]
    [3,4] [1,2] 
    [4] [1,2,3] <--
    [3,4] [1,2]
    [3] [1,2,4] <--
    [3,4] [1,2]
    
    
    [2,4] [1,3] <--
    [2,3,4] [1] 
    [2,3] [1,4] <--
    [2,3,4] [1] 
    [2,3,4] []   
    
    []
    """
    elementsToCombineList=range(fromAmount)
    #currentCombination=[]
    reList=[]
    reList =throughAllCombinationsRecursive(elementsToCombineList,byAmount)
    return reList
    
def delElementsLessOrEqualThanValue(lst,value):
    reLst=[]
    for item in lst:
        if item>value:
            reLst.append(item)
    return reLst
    
#complexity: n*(n-1)*(n-2)...(n-1)
def throughAllCombinationsRecursive(elementsToCombineList,byAmount):
    reList=[]
    
    if byAmount==0:
        return []
    
    for i in range(len(elementsToCombineList)):
        item=elementsToCombineList[i]
    
    
        elementsToCombineListWithoutItemS=delElementsLessOrEqualThanValue(elementsToCombineList,item)
        
        
        if len(elementsToCombineListWithoutItemS) < byAmount-1 and byAmount>1:
            
            return reList
        
        recursiveList=throughAllCombinationsRecursive(elementsToCombineListWithoutItemS,byAmount-1)
        log("recursiveList"+ str(recursiveList))
    
    
        if len(recursiveList)==0:
            reList+=[[item]]
        
        for j in range(len(recursiveList)):
            recursiveItem=recursiveList[j]
            reList+=[[item]+recursiveItem]
        
    
    
    return reList
    
def throughAllCombinationsWithRepititions(fromAmount,byAmount):
    
    # from 2 by 2: [0,0], [0,1], [1,0], [1,1]
    """
    [1,2][]
    [1,2] [1]
    [3] [1,2] <--
    [2,3] [1]
    [2] [1,3] <--
    [2,3] [1]
    [1,2,3][] 
    [2,3]  []
    [3]   [2]
    []  [2,3] <--
    [3]   [2]
    [2,3]  []
    """
    
    elementsToCombineList=range(fromAmount)
    #currentCombination=[]
    reList=[]
    reList =throughAllCombinationsWithRepititionsRecursive(elementsToCombineList,byAmount)
    return reList
    
def delElementsLessThanValue(lst,value):
    reLst=[]
    for item in lst:
        if item>=value:
            reLst.append(item)
    return reLst
    

def throughAllCombinationsWithRepititionsRecursive(elementsToCombineList,byAmount):
    reList=[]
    
    if byAmount==0:
        return []
    
    for i in range(len(elementsToCombineList)):
        item=elementsToCombineList[i]
    
    
        elementsToCombineListWithoutItemS=delElementsLessThanValue(elementsToCombineList,item)
        
        
        #if len(elementsToCombineListWithoutItemS) < byAmount-1 and byAmount>1:
        #    print "relist", reList, len(elementsToCombineListWithoutItemS), byAmount
        #    return reList
        
        recursiveList=throughAllCombinationsWithRepititionsRecursive(elementsToCombineListWithoutItemS,byAmount-1)
        #log("recursiveList"+ str(recursiveList))
    
    
        if len(recursiveList)==0:
            reList+=[[item]]
        
        for j in range(len(recursiveList)):
            recursiveItem=recursiveList[j]
            reList+=[[item]+recursiveItem]
        
    
    
    return reList

    
    
    
    
def throughAllPermutations(permutationElementsAmount):
    permutationElementsList=range(permutationElementsAmount)
    return throughAllPermutationsRecursive(permutationElementsList)
  
def throughAllPermutationsRecursive(permutationElementsList):
    reList=[]
    if len(permutationElementsList)==1:
	
	return [permutationElementsList]
    for i in range(len(permutationElementsList)):
	item=permutationElementsList[i]
	permutationElementsListWithoutItem=permutationElementsList[:]
	del permutationElementsListWithoutItem[i]
	
	recursiveList=throughAllPermutationsRecursive(permutationElementsListWithoutItem)
	for j in range(len(recursiveList)):
	    recursiveItem=recursiveList[j]
	    
	    
	    reList+=[[item]+recursiveItem]
    return reList
    
#AUTOMATA
    
# through all logic function truth tables
# through all links lists
def throughAllAutomata(N,K):
    # will launch throughAllLinks for each functionsList and will build an automata for each functionsList and each linksList
    throughAllFunctions(N,K)

#END AUTOMATA    
    
#LINKS    
    
def showLinksLinksList(linksList,linksListList):
    print "[",
    for currentLinksList in linksListList:
	print "[",
	for value in currentLinksList:
	    print linksList[value], ",",
	print "]",
    print "]"

def throughAllLinks(N,K):
    linksList=throughAllCombinations(N,K)
    #print "linksList", linksList
    linksListList=throughAllCombinationsWithRepititions(len(linksList),N)
    #print "linksListList",linksListList
    reList=[]
    for currentLinksNumbersList in linksListList:
	currentLinksList=[]
	for listNumber in currentLinksNumbersList:
	    currentLinksList.append(linksList[listNumber])
	reList.append(currentLinksList)
    return reList
    #showLinksLinksList(linksList,linksListList)
    
    

def throughAllLinksRecursive(N,K,functionsList,linksListList,linksList,Nvariable):
    if NVariable==0:
	return
	
    for linksListOrdinalNumber in range(2**K):
	linksListList+=[linksList[linksListOrdinalNumber]]
	throughAllLinksRecursive(N,K,functionsList,linksListList,linksList,Nvariable-1)
	del functionsList[-1]
	
#END LINKS	

#FUNCTIONS
# through all automata, to be correct
def throughAllFunctions(N,K):
    global summ
    functionsList=[]
    Nvariable=N
    
    throughAllFunctionsRecursive(N,K,functionsList,Nvariable)
    print summ

def throughAllFunctionsRecursive(N,K,functionsList,Nvariable):
    global globalFunctionsAmount
    global summ
    if Nvariable==0:
	globalFunctionsAmount+=1
	#throughAllLinks(N,K,functionsList)
	#print globalFunctionsAmount
	#print functionsList
	linksListList=throughAllLinks(N,K)
	
	for linksList in linksListList:
	    
	    
	    automataFunctionsList=[]
	    for functionList in functionsList:
		stringFunctionList=ProxyFunctions.boolListToString(functionList)
		automataFunction=BoolFunction.BoolFunction(K,stringFunctionList)
		automataFunctionsList.append(automataFunction)
	    
	    
	    print "Automata:",summ
	    currentAutomata = NK_Automata(N,K,automataFunctionsList,linksList)
	    AutomataProssesing.doAutomata(N,K,currentAutomata,summ)
	    
	    summ+=1
	    
	
	    
	    
	return
	
    for logicFunctionValuesOrdinalNumber in range(2**(2**K)):
	
	functionsList+=[functionValuesByOrdinalNumber(logicFunctionValuesOrdinalNumber,2**K)]
	throughAllFunctionsRecursive(N,K,functionsList,Nvariable-1)
	del functionsList[-1]

def functionValuesByOrdinalNumber(logicFunctionValuesOrdinalNumber,expectedAmountOfValues):
    #42,8->32+8+2,8->101010,8->00101010
    # or
    #42,8->32+8+2,8->010101,8->01010100
    functionValuesList=[]
    decimalValue=logicFunctionValuesOrdinalNumber
    while decimalValue>0:
	functionValuesList+=[decimalValue % 2]
	decimalValue=decimalValue/2
	
    amountOfValues=len(functionValuesList)
    if amountOfValues<expectedAmountOfValues:
	for i in range(expectedAmountOfValues-amountOfValues):
	    functionValuesList+=[0]
    
    return functionValuesList
	
#END FUNCTIONS	