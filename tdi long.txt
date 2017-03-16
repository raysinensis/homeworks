import timeit
start=timeit.default_timer()
n=24
expectnum=0
expectover=0
for x in range(0,2**n):
    resultx=(str(bin(x))[2:]).zfill(n)
    splitx=list(str(resultx))
    splitx=[int(i) for i in splitx]
    countofone=splitx.count(1)
    chancex=float((0.6**countofone)*(0.4**(n-countofone)))
    groupn=1
    for x in range(0,len(splitx)-1):
        if splitx[x]+splitx[x+1]==1:
            groupn+=1
    expectnum+=chancex*groupn
    if groupn>12:
        expectover+=chancex
print(expectnum)
print(expectover)
stop=timeit.default_timer()
print(stop - start)
