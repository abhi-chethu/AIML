[]:def infoGain(P,N):
    import math
    return -P/P(P+N)*math.log2(P/(P+N))-N/(P+N)*math.log2(N/(P+N))

[]:def insertNode(tree,addTo,Node):
    for k,v in tree.items():
        if isinstance(v,dict):
            tree[k]=insertNode(v,addTo,Node)
    if addTo in tree:
        if isinstance(tree[addTo],dict):
            tree[addTo][Node]='Node'
        else:
            tree[addTo]={Node:'None'}
    return tree        

[]:def insertConcept(tree,addTo,Node):
    for k,v in tree.items():
        if isinstance(v,dict):
            tree[k]=insertConcept(v,addTo,Node)
    if addTo in tree:
        tree[addTo]=Node
    return tree

[]:def getNextNode(data,Attributelist,concept,conceptVals,tree,addTo):
    Total=data.shape[0]
    if Total=0:
        return tree
    countC={}
    for cVal in conceptVals:
        dataC=data[data[concept]==cVal]
        countC[cVal]=dataC.shape[0]
    if countC[cVals[0]]==0:
        tree=insertConcept(tree,addTo,conceptVals[1])
        return tree
    if countC[conceptVals[1]]==0:
        tree=insertConcept(tree,addTo,conceptVals[0])
        return tree
    class Entropy=infoGain(countC[conceptVal[0]]countC[conceptVals[1]])
    Attr={}
    for a in AttrubutrList:
        Attr[a]=list(set(data[a]))
    AttrCount={}
    Entropy Attr={}
    for att in Attr:
        for c in conceptVals:
            iData=data[data[att]==vals]
