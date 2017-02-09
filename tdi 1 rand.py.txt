import random
import timeit
import csv
##start=timeit.default_timer()
groupsum=0
groupoversum=0
groupover240=0
filename="f:/random1.csv"
for z in range(1,501):
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
