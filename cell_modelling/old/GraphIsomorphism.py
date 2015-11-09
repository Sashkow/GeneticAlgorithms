import ThroughAllAutomata
import copy

from Debug import log

# graps are actually automatas with graphs of states upon which the isomporphism is being checked
def isIsomorphic(graph1,graph2):
    #cycle/branches level isomporphism will be launched inside
    basinLevelBijectionsList=hasBasinLevelBijections(graph1,graph2)
    if basinLevelBijectionsList==[]:
        log("basins do not match")
        return False

    for basinLevelBijection in basinLevelBijectionsList:
        isomporphismEstablished=True
        for proImageBasin in basinLevelBijection:
            imageBasin=basinLevelBijection[proImageBasin]
            if not isIsomorphicBasins(proImageBasin,imageBasin,graph1,graph2):
                isomporphismEstablished=False
                break
        if isomporphismEstablished:
            return True

def getAllBasinAttractorStates(automata,basinIndex):
    attractorStatesList=[]
    for state in automata.statesList:
        if state.inAttractor and state.basinNumber==basinIndex:
            attractorStatesList.append(state)
    return attractorStatesList

def getAllBasinNonAttractorStates(automata,basinIndex):
    attractorStatesList=[]
    for state in automata.statesList:
        if (not state.inAttractor) and state.basinNumber==basinIndex:
            attractorStatesList.append(state)
    return attractorStatesList



def isIsomorphicBasins(basin1,basin2,graph1,graph2):
    attractor1Size=graph1.attractorDict[basin1][0]
    attractor2Size=graph2.attractorDict[basin2][0]
    if attractor1Size!=attractor2Size:
        return False

    attractorStatesList1=getAllBasinAttractorStates(graph1,basin1)
    basinStatesList1=getAllBasinNonAttractorStates(graph1,basin1)

    attractorStatesList2=getAllBasinAttractorStates(graph2,basin2)
    basinStatesList2=getAllBasinNonAttractorStates(graph2,basin2)

    #for startingIndex:

    #for each attractor state in basin1 starting with 1
    #   check if it matches basin2 starting with 1

    #for each attractor state in basin1 starting with 2
    #   check if it matches basin2 starting with 1
    #...










#returns dict {basinPower: [basin1,basin2]}
def analyseGraphBasins(graph):
    basinAmount_BasinList_Dict={}
    for basinNumber in graph.attractorDict:
        basinData=graph.attractorDict[basinNumber]
        basinAmount=basinData[0]+basinData[1]
        if basinAmount in basinAmount_BasinList_Dict:
            basinAmount_BasinList_Dict[basinAmount].append(basinNumber)
        else:
            basinAmount_BasinList_Dict[basinAmount]=[basinNumber]
    return basinAmount_BasinList_Dict





#basin level bijections are kinna isomporphic, but not fully however
#returns list of all bijections between basins of equal basin and attractor size
# [{basinOfGraph1:basinOfGraph2,...},...]
#Test cases are in test.py file
def hasBasinLevelBijections(graph1,graph2):
    basinLevelBijectionsList=[]
    basinSize_BasinsList_Dict1=analyseGraphBasins(graph1)
    basinSize_BasinsList_Dict2=analyseGraphBasins(graph2)

    for basinSize in basinSize_BasinsList_Dict1:

        if not basinSize in basinSize_BasinsList_Dict2:
            log("basin sizes do not match") # N_04_K_02/34027, 34028 to trigger
            return []

        equalBasinSizeBasinsList1=basinSize_BasinsList_Dict1[basinSize]
        equalBasinSizeBasinsList2=basinSize_BasinsList_Dict2[basinSize]




        if len(equalBasinSizeBasinsList1)!=len(equalBasinSizeBasinsList2):

            log("amounts of basins of certain size do not match")
            return []

        if len(equalBasinSizeBasinsList1)==1:
            log("simple bijection established")
            addToAllBijections(equalBasinSizeBasinsList1[0],equalBasinSizeBasinsList2[0],basinLevelBijectionsList)

        else:


            attractorSize_BasinList_Dict1=analyseGraphBasinAttractors(graph1,equalBasinSizeBasinsList1)
            attractorSize_BasinList_Dict2=analyseGraphBasinAttractors(graph2,equalBasinSizeBasinsList2)



            for attractorSize in attractorSize_BasinList_Dict1:

                if not attractorSize in attractorSize_BasinList_Dict2:
                    log("attractor of certain size is absent")
                    return []

                equalAttractorSizeBasinsList1=attractorSize_BasinList_Dict1[attractorSize]
                equalAttractorSizeBasinsList2=attractorSize_BasinList_Dict2[attractorSize]


                if len(attractorSize_BasinList_Dict1[attractorSize])!=len(attractorSize_BasinList_Dict2[attractorSize]):
                    log("attractor sizes do not match")
                    return []

                if len(attractorSize_BasinList_Dict1[attractorSize])==1:
                    log("simple bijection established")
                    addToAllBijections(attractorSize_BasinList_Dict1[attractorSize][0],attractorSize_BasinList_Dict1[attractorSize][0],basinLevelBijectionsList)
                else:
                    log("brute force is used to establish bijections")
                    #permutations are the ways to establish basin level bijections between equal sized and "attractor"ed basins
                    permutationsList=ThroughAllAutomata.throughAllPermutations(len(attractorSize_BasinList_Dict1[attractorSize]))

                    copiedBijectionsList=copy.deepcopy(basinLevelBijectionsList)

                    basinLevelBijectionsList=[]

                    for permutation in permutationsList:
                        iFrom=0
                        currentBijectionsList=copy.deepcopy(copiedBijectionsList)

                        for iTo in permutation:

                            addToAllBijections(equalAttractorSizeBasinsList1[iFrom],equalAttractorSizeBasinsList2[iTo],currentBijectionsList)
                            #print iFrom, iTo, currentBijectionsList
                            iFrom+=1
                        basinLevelBijectionsList+=currentBijectionsList
    log("All Fits") #N_04_K_02/34027, N_04_K_02/34025 to trigger
    return basinLevelBijectionsList


def addToAllBijections(basinIndex1,basinIndex2,basinLevelBijectionsList):

    if basinLevelBijectionsList==[]:
        basinLevelBijectionsList.append({basinIndex1:basinIndex2})
        return

    for bijectionDict in basinLevelBijectionsList:
        if basinIndex1 in bijectionDict:
            log("Error, bijection for the current value has already been established")
        bijectionDict[basinIndex1]=basinIndex2

def analyseGraphBasinAttractors(graph,equalBasinSizeBasinsList):
    attractorSize_BasinList_Dict={}
    for basinIndex in equalBasinSizeBasinsList:
        currentBasinAttractorSize = graph.attractorDict[basinIndex][0]
        if currentBasinAttractorSize in attractorSize_BasinList_Dict:
            attractorSize_BasinList_Dict[currentBasinAttractorSize].append(basinIndex)
        else:
            attractorSize_BasinList_Dict[currentBasinAttractorSize]=[basinIndex]
    return attractorSize_BasinList_Dict
