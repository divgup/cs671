import numpy as np
import cv2
import math
import os
import random
from PIL import Image, ImageDraw
import csv
os.system("mkdir data1")
length = [7,15]
width = [1,3]
color = [(255,0,0),(0,0,255)]

itr = 0
for i in length:
    if(i==7):
        label1 = 0
    else:
        label1 = 1    
    for j in width:
        if j == 1:
            label2 = 0
        else:
            label2 = 1    
        for k in range(0,12):
            theta = k*15*(math.pi)/180
            for c in color:
                if(c==(255,0,0)):
                    label = 0
                for r in range(1000):
                    im1 = np.zeros((28,28,3),dtype='int')
                    im = Image.fromarray(im1,'RGB')
                    line1 = ImageDraw.Draw(im)
                    y2 = i*(math.sin(theta))
                    x2 = i*(math.cos(theta))
                    xshift=random.randint(int((x2/2)-14),int(14-(x2/2)))
                    yshift = random.randint(int((y2/2)-14),int(14-(y2/2)))
                       #point1,point2 = (int(14- (x2/2) +xshift),int(14 + (y2/2) + yshift)),(int(14 + (x2/2) + xshift),int(14 - (y2/2) + yshift))
                       #point1, point2 = (x1, y1), (x2, y2)
                    line1.line((int(14- (x2/2) +xshift),int(14 + (y2/2) + yshift),int(14 + (x2/2) + xshift),int(14 - (y2/2) + yshift)), fill = c, width=j)
                    iname = str(itr)+".jpg"
                    #    itr+=1
                    iname = str(label1)+"_"+str(label2)+"_"+str(k)+"_"+str(label)+str(r+1)+".jpg"
                        #writer.writerow([str(itr),str(iname)])
                    im.save("data1/"+iname)

def makeVideo(outputVideoname):  
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    outputVideo = cv2.VideoWriter(outputVideoname,fourcc,2,(84,84))

    for i in length:
        if(i==7):
            label1 = 0
        else:
            label1 = 1 
        for j in width:
            if j == 1:
                label2 = 0
            else:
                label2 = 1
            for k in range(0,12):
                 for c in color:
                    if(c==(255,0,0)):
                        label = 0
                    else:
                        label = 1
                    for r in range(0,10):
                        frame = Image.new('RGB',(84,84)) 
                        iname1 = str(label1)+"_"+str(label2)+"_"+str(k)+"_"+str(label)+""+str(r*9+1)+".jpg"
                        iname2 = str(label1)+"_"+str(label2)+"_"+str(k)+"_"+str(label)+""+str(r*9+2)+".jpg"
                        iname3 = str(label1)+"_"+str(label2)+"_"+str(k)+"_"+str(label)+""+str(r*9+3)+".jpg"
                        iname4 = str(label1)+"_"+str(label2)+"_"+str(k)+"_"+str(label)+""+str(r*9+4)+".jpg"
                        iname5 = str(label1)+"_"+str(label2)+"_"+str(k)+"_"+str(label)+""+str(r*9+5)+".jpg"
                        iname6 = str(label1)+"_"+str(label2)+"_"+str(k)+"_"+str(label)+""+str(r*9+6)+".jpg"
                        iname7 = str(label1)+"_"+str(label2)+"_"+str(k)+"_"+str(label)+""+str(r*9+7)+".jpg"
                        iname8 = str(label1)+"_"+str(label2)+"_"+str(k)+"_"+str(label)+""+str(r*9+8)+".jpg"                        
                        iname9 = str(label1)+"_"+str(label2)+"_"+str(k)+"_"+str(label)+""+str(r*9+9)+".jpg"
                        frame.paste(Image.open("data1/"+iname1),(0,0,28,28))
                        frame.paste(Image.open("data1/"+iname2), (28,0,56,28))
                        frame.paste(Image.open("data1/"+iname3), (56,0,84,28))
                        frame.paste(Image.open("data1/"+iname4), (0,28,28,56))
                        frame.paste(Image.open("data1/"+iname5), (28,28,56,56))
                        frame.paste(Image.open("data1/"+iname6), (56,28,84,56))
                        frame.paste(Image.open("data1/"+iname7), (0,56,28,84))
                        frame.paste(Image.open("data1/"+iname8), (28,56,56,84))
                        frame.paste(Image.open("data1/"+iname9), (56,56,84,84))

                        frame = cv2.cvtColor(np.asarray(frame,dtype=np.uint8),cv2.COLOR_BGR2RGB)
#                         outputVideo.write(frame)
    outputVideo.release()  
makeVideo("ass1_q1.mp4")                  
