import pygame
black=(0,0,0)
white=(255,255,255)
green=(1,255,0)
yellow=(15,100,0)
red=(255,0,0)
pygame.init()
size=[700,500]
screen=pygame.display.set_mode(size)
pygame.display.set_caption('Anime')
done=False
clock=pygame.time.Clock()
rect_x=0
rect_y=0
rect_change_x=5
rect_change_y=5
while done==False:
	clock.tick(20)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done=True
	screen.fill(black)
	pygame.draw.rect(screen,white,[rect_x,rect_y,50,50])
	rect_x+=rect_change_x
	rect_y+=rect_change_y
	if rect_y>450 or rect_y<0:
		rect_change_y=rect_change_y*-1
	if rect_x>650 or rect_x<0:
		rect_change_x=rect_change_x*-1
	pygame.display.flip()
pygame.quit()









































































