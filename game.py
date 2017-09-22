import walls,bricks,player,enemy,bomb,config
from alarmexception import *
from getchunix import *
import random
import config
config.lives=3
config.score=0
getch = GetchUnix()
matrix = [[0 for y in range(88)] for x in range(44)]
a=walls.Wall(matrix)
b=bricks.Brick(matrix)
z=player.Bomberman(matrix)
e1=enemy.Enemy1(matrix)
e2=enemy.Enemy2(matrix)


a.show(matrix)
tim=0
def alarmHandler(signum, frame):
    raise AlarmException

def input_to(timeout=1):
	signal.signal(signal.SIGALRM, alarmHandler)
	signal.alarm(timeout)
	try:
		text = getch()
		signal.alarm(0)
		return text
	except AlarmException:
			
		signal.signal(signal.SIGALRM, signal.SIG_IGN)
	return ''



while(1):
	c=input_to()
	
	if c=='d':
		z.move_right(matrix,z.x,z.y)
		e1.move(matrix)
		e2.move(matrix)
		if matrix[z.x][z.y+4]=='E':
			config.lives=config.lives-1
			for i in range(z.x,z.x+2):
				for j in range(z.y,z.y+4):
					matrix[i][j]=' '
			matrix[2][4]='B'
			matrix[2][5]='B'
			matrix[2][6]='B'
			matrix[2][7]='B'
			matrix[3][4]='B'
			matrix[3][5]='B'
			matrix[3][6]='B'
			matrix[3][7]='B'
			z.x=2
			z.y=4			
	if c=='a':
		z.move_left(matrix,z.x,z.y)
		e1.move(matrix)
		e2.move(matrix)
		if matrix[z.x][z.y-4]=='E':
			config.lives=config.lives-1
			for i in range(z.x,z.x+2):
				for j in range(z.y,z.y+4):
					matrix[i][j]=' '
			matrix[2][4]='B'
			matrix[2][5]='B'
			matrix[2][6]='B'
			matrix[2][7]='B'
			matrix[3][4]='B'
			matrix[3][5]='B'
			matrix[3][6]='B'
			matrix[3][7]='B'
			z.x=2
			z.y=4		
	if c=='s':
		z.move_down(matrix,z.x,z.y)
		e1.move(matrix)
		e2.move(matrix)
		if matrix[z.x+2][z.y]=='E':
			config.lives=config.lives-1
			for i in range(z.x,z.x+2):
				for j in range(z.y,z.y+4):
					matrix[i][j]=' '
			matrix[2][4]='B'
			matrix[2][5]='B'
			matrix[2][6]='B'
			matrix[2][7]='B'
			matrix[3][4]='B'
			matrix[3][5]='B'
			matrix[3][6]='B'
			matrix[3][7]='B'
			z.x=2
			z.y=4		
	if c=='w':
		z.move_up(matrix,z.x,z.y)
		e1.move(matrix)
		e2.move(matrix)
		if matrix[z.x-2][z.y]=='E':
			config.lives=config.lives-1
			for i in range(z.x,z.x+2):
				for j in range(z.y,z.y+4):
					matrix[i][j]=' '
			matrix[2][4]='B'
			matrix[2][5]='B'
			matrix[2][6]='B'
			matrix[2][7]='B'
			matrix[3][4]='B'
			matrix[3][5]='B'
			matrix[3][6]='B'
			matrix[3][7]='B'
			z.x=2
			z.y=4		
	if c=='b' and tim==0:
		tim=3
		bom=bomb.Bomb()		
		x1=z.x
		y1=z.y
		while tim>0:
			tim=tim-1
			c=input_to()
			if c=='d':
				e1.move(matrix)
				e2.move(matrix)
				z.move_right(matrix,z.x,z.y)
				a.show(matrix)
			if c=='a':
				e1.move(matrix)
				e2.move(matrix)
				z.move_left(matrix,z.x,z.y)
				a.show(matrix)
			if c=='s':
				e1.move(matrix)
				e2.move(matrix)
				z.move_down(matrix,z.x,z.y)
				a.show(matrix)
			if c=='w':
				e1.move(matrix)
				e2.move(matrix)
				z.move_up(matrix,z.x,z.y)
				a.show(matrix)
		if tim==0:
			bom.explode(matrix,x1,y1,'*')
			a.show(matrix)
			time.sleep(2)
			bom.explode(matrix,x1,y1,' ')
			if z.death(matrix,x1,y1)==1:
				config.lives=config.lives-1
			a.show(matrix)
	if c=='q' or config.lives==0:
		sys.exit(0)
	a.show(matrix)





