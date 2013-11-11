import pygame
import random
black=(0,0,0)
white=(255,255,255)
green=(1,255,0)
yellow=(15,100,0)
red=(255,0,0)
pygame.init()
size=[700,500]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("SnowFlakes")
done=False
clock=pygame.time.Clock()
star_list=[]
for i in range(100):
                x=random.randrange(0,650)
                y=random.randrange(0,500)
		star_list.append([x,y])

while done==False:
	clock.tick(10)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done=True
	screen.fill(black)
	for i in range(len(star_list)):
		pygame.draw.circle(screen,white,star_list[i],random.randrange(2,4))
		star_list[i][1]+=3
		y=random.randrange(0,10)
		x=random.randrange(0,650)
		if star_list[i][1]>500:
			star_list[i][1]=y
			star_list[i][0]=x
			
		
	pygame.display.flip()
pygame.quit()







































