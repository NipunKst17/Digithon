import pygame
import random
import math
pygame.init()
sc=pygame.display.set_mode((500,500))
pos_x=0
pos_y=250
clk=pygame.time.Clock()
run=True
velocity_x=0
width=50
angle=0
count=0
tempss=pos_x-20*math.cos(math.pi/2-angle)
print("tempss ",tempss)
keys={"Left":False,"Right":False,"Up":False,"Down":False,"Stop":False}
robo_img=pygame.image.load("roboss.png")
def get_command(keys,counts):
#write your code here in this function include all the necessary terms but return the counts' updated value
#returning counts is important for simulation




#def assign(ev,value,keys,counts):
    #if ev==pygame.K_LEFT:
        #keys["Left"]=value
    #elif ev==pygame.K_RIGHT:
        #keys["Right"]=value
    #elif ev==pygame.K_UP:
        #keys["Up"]=value
        #counts=1
    #elif ev==pygame.K_DOWN:
        #keys["Down"]=value
        #counts=-1
    #elif ev==pygame.K_SPACE:
        #keys["Space"]=value
    #return counts
    #assignCount(keys)
#def assignCount(keys):
#    if keys["Up"][0]==True:
#        keys["Up"][1]+=1
#    if keys["Down"][0]==True:
#        keys["Down"][1]+=1
def assignVelocity(keys,count):
    velocity_x=0
    if keys["Down"]==True and count==-1:
        velocity_x=-1
    if keys["Up"]==True and count==1:
        velocity_x=1
    if keys["Stop"]==True:
        velocity_x=0
    return velocity_x
def assignAngle(keys,angles):
    angle=angles
    if keys["Right"]==True:
        angle-=5*(math.pi/180)
    elif keys["Left"]==True:
        angle+=5*(math.pi/180)
    return angle
#def Stop(keys):
    #keys["Stop"]=False
    #if keys["Up"]==True:
        #keys["Up"]=False
        #count=0
        #keys["Up"][1]=0
    #if keys["Down"]==True:
        #keys["Down"]=False
        #count=0
while run:
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            run=False
        #elif ev.type==pygame.KEYDOWN:
            #count=assign(ev.key,True,keys,count)
        #elif ev.type==pygame.KEYUP:
            #if ev.key==pygame.K_SPACE:
                #keys["Space"]=False
                #if keys["Up"]==True:
                    #keys["Up"]=False
                    #count=0
                    #keys["Up"][1]=0
                #if keys["Down"]==True:
                    #keys["Down"]=False
                    #count=0
                    #keys["Down"][1]=0
            #if ev.key==pygame.K_RIGHT:
                #keys["Right"]=False
            #if ev.key==pygame.K_LEFT:
                #keys["Left"]=False
    #assign(ev.key,False,keys)
    count=get_command(keys,count)
    clk.tick(10)
    print("count ",count)
    velocity_x=assignVelocity(keys,count)
    #temp=pos_x
    angle=assignAngle(keys,angle)
    temp=pos_x
    temps=pos_y
    print(pos_y," initial")
    print("angle ",angle)
    pos_x-=velocity_x*20*math.cos(math.pi/2-angle)
    pos_y-=velocity_x*20*math.sin(math.pi/2-angle)
    print("cos(angle): ",math.cos(math.pi/2))
    print("pos_x: ",pos_x)
    print(pos_y,temps)
    clk.tick(80)
    sc.fill('orange')
    w=robo_img.get_width()
    h=robo_img.get_height()
    if pos_x<0:
        if(pos_x!=tempss):
            pos_y=temps
        pos_x=0
        print("in pos_x<0")
    elif  pos_x>500-0.5*w:
        pos_x=500-0.5*w
        pos_y=temps
        print("in pos_x>500-0.5*w")
    temp=pos_x
    if pos_y<0:
        pos_y=0
        pos_x=temp
        print("in pos_y<0")
    elif pos_y>500-0.4*h:
        pos_y=500-0.4*h
        pos_x=temp
        print("in pos_y>500-0.4*h")
    roboScaled_image=pygame.transform.scale(robo_img,(w*0.5,h*0.4))
    robo_rotate_image=pygame.transform.rotate(roboScaled_image,((angle)*(180/math.pi)))
    print(pos_y,"final")
    sc.blit(robo_rotate_image,(pos_x,pos_y))
    pygame.display.update()
pygame.quit()