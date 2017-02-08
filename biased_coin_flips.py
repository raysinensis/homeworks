#head as 1, tail as 0

def generateflips(n):
	arrayflips=[]
	for x in range(0,2**n):
		resultx=(str(bin(x))[2:]).zfill(n)
		splitx=list(str(resultx))
		splitx=[int(i) for i in splitx]
		arrayflips.append(splitx)
	return arrayflips
	
def chanceof(resultx,n):
	countofone=resultx.count(1)
	chancex=float((0.6**countofone)*(0.4**(n-countofone)))
	return(chancex)
	
def groupcount(resultx):
	groupn=1
	for x in range(0,len(resultx)-1):
		if resultx[x]+resultx[x+1]==1:
			groupn+=1
	return(groupn)

def fillarray(arrayflips,n):
	arraynumbers=[]
	for resultx in arrayflips:
		arraynumbers.append([chanceof(resultx,n),groupcount(resultx)])
	return arraynumbers

def expectgroup(arraynumbers):
	expectnum=0
	for numbersx in arraynumbers:
		expectnum+=numbersx[0]*numbersx[1]
	return expectnum

def expectover(arraynumbers,numberx):
	expectnum=0
	for numbersx in arraynumbers:
		if numbersx[1]>numberx:
			expectnum+=numbersx[0]
	return expectnum

def expectoverover(arraynumbers,numberx,numbery):
	expectnum=0
	i=0
	for numbersx in arraynumbers:
		if numbersx[1]>numberx and a10[i].count(1)>numbery:
			expectnum+=numbersx[0]
		i+=1
	return expectnum

def rearray(arraynumbers,numberx):
	rearrayed=[]
	chanceall=0
	for numbersx in arraynumbers:
		if numbersx[1]>numberx:
			rearrayed.append(numbersx)
			chanceall+=numbersx[0]
	print(chanceall)
	for i in range(0,len(rearrayed)):
		rearrayed[i][0]=rearrayed[i][0]/chanceall
	return rearrayed


#for n=10
a10=generateflips(10)
aall10=fillarray(a10,10)

##math: every final toss has a 0.6 of heads, 0.4 of tails, which means 0.6*0.4+0.4*0.6 is the expected increase of groups for every additional toss, the formula is (n=1 is 1 group) 1+(0.6*0.4+0.4*0.6)*(n-1)
expect500=1+(0.6*0.4+0.4*0.6)*(500-1)

import random
import timeit
import csv
##start=timeit.default_timer()
groupsum=0
groupoversum=0
groupover240=0
filename="f:/random1.csv"
for z in range(1,1001):
    groupsum=0
    groupoversum=0
    groupover240=0
    for i in range(1,100001):
        seq=[0]*500
        for j in range(0,500):
            if random.random()<=0.6:
                seq[j]=1
        groupn=1
        for x in range(0,len(seq)-1):
            if seq[x]+seq[x+1]==1:
                groupn+=1
        if groupn>250:
            groupoversum+=1
        if groupn>240:
            groupover240+=1
        groupsum+=groupn
    with open(filename, 'a') as csvfile:
        output = csv.writer(csvfile)
        output.writerow([groupsum,groupoversum,groupover240])
        ##print(groupsum)
        ##print(groupoversum)
        ##print(groupover240)
##stop=timeit.default_timer()
##print(stop - start)


import random
import csv
eventnum=0
flips=0
for z in range(1,2):
	for i in range(1,11):
		seq=[0]*200
		for j in range(0,200):
			if random.random()<=0.6:
			seq[j]=1
		flips+=1
		groupn=1
        	for x in range(0,len(seq)-1):
            		if seq[x]+seq[x+1]==1:
               			groupn+=1
		if seq.count(1)>100:
			if groupn>100:
				eventnum+1
print(eventnum/1000/100000)
print(eventnum/flips)	
		
