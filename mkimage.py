from PIL import Image
from PIL import ImageDraw
import json
f=open("mandeldata","r")
mb=json.loads(f.read())
f.close()
img=Image.new("RGB",(len(mb),len(mb[0])),"white")
draw = ImageDraw.Draw(img)
for i,row in enumerate(mb):
	for j,cel in enumerate(row):
		if(cel==-1):
			color=(0,0,0)
		else:
			color=(255,255,255)
		draw.point([i,j],color)
img.save("out.png", "PNG")
