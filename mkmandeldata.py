import numpy
import json

MAXI=100
WIDTH=100
HEIGHT=100
mb=numpy.zeros([WIDTH,HEIGHT])
for i in range(WIDTH):
	for j in range(HEIGHT):
		res=0
		c=[(4.0/WIDTH)*i-2,(4.0/HEIGHT)*j-2]
		z=[0.0,0.0]
		inter=0
		while inter<MAXI and res < 4:
			nz=[0,0]
			nz[0]=z[0]*z[0]-z[1]*z[1]+c[0]
			nz[1]=2* z[0] * z[1] +c[1]
			z=nz
			res=z[0]*z[0]+z[1]*z[1]
			inter=inter+1
		if res<4:
			mb[i][j]=-1
		else:
			mb[i][j]=inter 
print json.dumps(mb.tolist())
