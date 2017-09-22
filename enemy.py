import random
#Enemies top left coordinate is located
#and then we check if a rectangle can be made by these x,y
class Enemy1:
	def __init__(self,matrix):
		x=random.randrange(2,42,2)
		y=random.randrange(4,80,4)
		self.x=x
		self.y=y
		e=0
		for k in range(0,2):
			for l in range(0,4):
				if matrix[x+k][y+l]=="X" or matrix[x+k][y+l]=="/" or matrix[x+k][y+l]=="E":
					e=e+1
					break
		if (x==2 and y==4) or (x==2 and y==8) or(x==4 and y==4) or(x==6 and y==4) or(x==2 and y==12):
			e=e+1
		if e==0:
			ch=True
		else:
			ch=False	
		if ch==True:
			for k in range(0,2):
				for l in range(0,4):
					matrix[x+k][y+l]="E"
			self.x=x
			self.y=y
#we choose a no from list a

	def move(self,matrix):
		a=[1,2,3,4]
		r=random.choice(a)
# 1 denotes movement in right direction
		if r==1:
			if matrix[self.x][self.y+4]!='X' and matrix[self.x][self.y+4]!='/' and matrix[self.x][self.y+4]!='E':
				x=self.x
				y=self.y
				for i in range(x,x+2):
					for j in range(y+4,y+8):
						matrix[i][j]='E'

				for i in range(x,x+2):
					for j in range(y,y+4):
						matrix[i][j]=' '
			self.y=self.y+4
# 2 denotes movement in left direction
		if r==2:
			if matrix[self.x][self.y-4]!='X' and matrix[self.x][self.y-4]!='/' and matrix[self.x][self.y-4]!='E':
				x=self.x
				y=self.y

				for i in range(x,x+2):
					for j in range(y-4,y):
						matrix[i][j]='E'

				for i in range(x,x+2):
					for j in range(y,y+4):
						matrix[i][j]=' '
				self.y=self.y-4
# 3 denotes movement in down direction
		if r==3:
			if matrix[self.x+2][self.y]!='X' and matrix[self.x+2][self.y]!='/' and matrix[self.x+2][self.y]!='E':
				x=self.x
				y=self.y
				for i in range(x+2,x+4):
					for j in range(y,y+4):
						matrix[i][j]='E'

				for i in range(x,x+2):
					for j in range(y,y+4):
						matrix[i][j]=' '
				self.x=self.x+2
# 4 denotes movement in up direction
		if r==4:
			if matrix[self.x-2][self.y]!='X' and matrix[self.x-2][self.y]!='/' and matrix[self.x-2][self.y]!='E':	
				x=self.x
				y=self.y
				for i in range(x-2,x):
					for j in range(y,y+4):
						matrix[i][j]='E'

				for i in range(x,x+2):
					for j in range(y,y+4):
						matrix[i][j]=' '
				self.x=self.x-2
		
	
class Enemy2:
	def __init__(self,matrix):
		x=random.randrange(2,42,2)
		y=random.randrange(4,80,4)
		self.x=x
		self.y=y
		e=0
		for k in range(0,2):
			for l in range(0,4):
				if matrix[x+k][y+l]=="X" or matrix[x+k][y+l]=="/" or matrix[x+k][y+l]=="E":
					e=e+1
					break
		if (x==2 and y==4) or (x==2 and y==8) or(x==4 and y==4) or(x==6 and y==4) or(x==2 and y==12):
			e=e+1
		if e==0:
			ch=True
		else:
			ch=False	
		if ch==True:
			for k in range(0,2):
				for l in range(0,4):
					matrix[x+k][y+l]="E"
			
	def move(self,matrix):
		a=[1,2,3,4]
		r=random.choice(a)
		if r==1:
			if matrix[self.x][self.y+4]!='X' and matrix[self.x][self.y+4]!='/' and matrix[self.x][self.y+4]!='E':
				x=self.x
				y=self.y
				for i in range(x,x+2):
					for j in range(y+4,y+8):
						matrix[i][j]='E'

				for i in range(x,x+2):
					for j in range(y,y+4):
						matrix[i][j]=' '
			self.y=self.y+4
		
		if r==2:
			if matrix[self.x][self.y-4]!='X' and matrix[self.x][self.y-4]!='/' and matrix[self.x][self.y-4]!='E':
				x=self.x
				y=self.y

				for i in range(x,x+2):
					for j in range(y-4,y):
						matrix[i][j]='E'

				for i in range(x,x+2):
					for j in range(y,y+4):
						matrix[i][j]=' '
				self.y=self.y-4
			
		if r==3:
			if matrix[self.x+2][self.y]!='X' and matrix[self.x+2][self.y]!='/' and matrix[self.x+2][self.y]!='E':
				x=self.x
				y=self.y
				for i in range(x+2,x+4):
					for j in range(y,y+4):
						matrix[i][j]='E'

				for i in range(x,x+2):
					for j in range(y,y+4):
						matrix[i][j]=' '
				self.x=self.x+2
			
		if r==4:
			if matrix[self.x-2][self.y]!='X' and matrix[self.x-2][self.y]!='/' and matrix[self.x-2][self.y]!='E':	
				x=self.x
				y=self.y
				for i in range(x-2,x):
					for j in range(y,y+4):
						matrix[i][j]='E'

				for i in range(x,x+2):
					for j in range(y,y+4):
						matrix[i][j]=' '
				self.x=self.x-2
		
		
		