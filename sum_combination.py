def mapmain(n):
	arraycomb=[0]*n
	x=0
	mapcomb(n,1,x)
def mapcomb(n,i,x):
	if n==0:
		print(arraycomb)
	else:
		for k in list(range(i,int((n/2)+1)))+[n]:
			arraycomb[x]=(k)
			mapcomb(n-k,k,x+1)
def mapmain(y,x):
	arraycomb=[0]*x
	mapcomb(y,0,x)
def mapcomb(n,i,x):
	if i==x-1:
		arraycomb[i]=n
		print(arraycomb)
	else:
		for k in range(1,n-x+i+2):
			arraycomb[i]=(k)
			mapcomb(n-k,i+1,x)
