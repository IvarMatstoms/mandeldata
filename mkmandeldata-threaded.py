import numpy
import json
import threading

def calc(x,thid):
	global WIDTH
	global HEIGHT
	global mb
	global threadsdone
	global i
	for y in range(HEIGHT):
		res=0
		c=[(4.0/WIDTH)*x-2,(4.0/HEIGHT)*y-2]
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
				mb[x][y]=-1
			else:
				mb[x][y]=inter
	threadsdone+=1
	print str(thid)+":"+str(x)
	newThread(thid)

def newThread(thid):
	global i
	global WIDTH
	global HEIGHT
	global threads
	global threadsdone
	if(i<WIDTH):
		t = threading.Thread(target=calc, args = [i+1,thid])
		i=i+1
		t.start()
	else:
		if(threadsdone==WIDTH):
			saveMB()


def saveMB():
	global mb
	f=open("mandeldata","w")
	f.write(json.dumps(mb.tolist()))
	f.close()
threads=[]
MAXI=1024
WIDTH=4000
HEIGHT=4000
CORES=8
threadsdone=0
mb=numpy.zeros([WIDTH,HEIGHT])
i=0;
for k in range(CORES):
	newThread(k);
