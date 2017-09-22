from __future__ import print_function
import random
#implementing 30 bricks randomly on board
# x,y denote top left point of rectangle
class Brick:
	def __init__(self,matrix):
		count=0
		for i in range(0,2000):
			x=random.randrange(2,42,2)
			y=random.randrange(4,80,4)
			e=0
			for k in range(0,2):
				for l in range(0,4):
					if matrix[x+k][y+l]=="X" or matrix[x+k][y+l]=="/":
						e=e+1
						break
			if x==2 and y==4:
				e=e+1
			if e==0:
				ch=True
			else:
				ch=False	
			if ch==True:
				for k in range(0,2):
					for l in range(0,4):
						matrix[x+k][y+l]="/"
				count=count+1
			else:
				continue
			if count==30:
				break
	

