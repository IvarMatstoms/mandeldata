import json
f=open("mandeldata","r")
mb=json.loads(f.read())
f.close()
#print mb[0]
for row in mb:
	rowstr=""
	for pos in row:
		#print pos
		if pos==-1:
			#print "hi"
			rowstr+="#"
		else:
			rowstr+="-"
	print rowstr		
