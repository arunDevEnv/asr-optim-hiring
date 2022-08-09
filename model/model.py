# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 22:57:48 2022

@author: arun_
"""


import copy

with open('instance.txt') as f:
    lineD=f.readlines()
    
line=[]
for i in range(len(lineD)):
    check=[0,0,0]
    tmp=[int(j) for j in lineD[i].split()]
    if tmp!=check:
        line.append(tmp)
    else:
        break

 
runInstance={}

        
    
sizeLine=len(line)-1
i=0
while i<sizeLine:
    sizeMachine=int(line[i][0])
    temp=[]
    for j in range(sizeMachine):
        temp.append(line[i+j+1])
    tu=(i,tuple(line[i]))
    temp.sort(key=lambda x:x[0])
    runInstance[tu]=temp
    i+=sizeMachine+1
    # print(line[i])

instancesDictionary={}
ctr=1
for r in runInstance:
    # ctr=1
    optionList=runInstance[r]
    (cost,days)=(int(r[1][1]),int(r[1][2]))
    source=[0,0,0,0]
    sink=[days+1,0,0,0]
    extensionList=[]
    extensionList.append(source)
    # extensionList.append(sink)
    for i in range(len(optionList)):
        extensionList.append(optionList[i])
    combinationPossible=[]
    y=[source,sink]
    combinationPossible.append(y)    
    for j in range(len(extensionList)): 
        for k in range(len(combinationPossible)):
            # print(combinationPossible)
            if(extensionList[j][0]>combinationPossible[k][-2][0]):
                tmp=copy.deepcopy(combinationPossible[k])
                tmp.append(extensionList[j])
                tmp.sort(key=lambda x:x[0])
                combinationPossible.append(tmp)
    costList=[]
    for v in range(len(combinationPossible)):
        combo=combinationPossible[v]
        tmpCost={}
        tmpCost[0]=cost
        for t in range(1,days+2):
            for w in range(len(combo)):
                if (t==combo[w][0]):
                    tmpCost[t]=tmpCost[t-1]-combo[w][1]+combo[w-1][2]
                elif ((t>combo[w][0]) and (t<combo[w+1][0])):
                    tmpCost[t]=tmpCost[t-1]+combo[w][-1]
                else:
                    continue
        valueS=tmpCost.values()
        nonP=[i for i in valueS if i<0]
        if(len(nonP))>0:
            costList.append([combo,tmpCost,-1])
        else:
            costList.append([combo,tmpCost,tmpCost[days+1]])
    validList=[i for i in costList if i[2]!=-1]
    validList.sort(key=lambda x:x[2])
    outp=str(r[1])
    print(str(r[1])+f"| Case {ctr}: {validList[-1][-1]}" )                
    ctr+=1            
                
    instancesDictionary[r]=validList
