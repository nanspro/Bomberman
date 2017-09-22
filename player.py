class Bomberman:
#movement of bomberman
	def __init__(self,matrix):
		self.x=2
		self.y=4

	def move_right(self,matrix,x,y):
		if matrix[x][y+4]==' ' and matrix[x+1][y+7]==' ':
			for i in range(x,x+2):
				for j in range(y+4,y+8):
					matrix[i][j]='B'

			for i in range(x,x+2):
				for j in range(y,y+4):
					matrix[i][j]=' '
			self.y=self.y+4
		else:
			return
	def move_left(self,matrix,x,y):
		if matrix[x][y-4]==' ' and matrix[x+1][y-1]==' ':
			for i in range(x,x+2):
				for j in range(y-4,y):
					matrix[i][j]='B'

			for i in range(x,x+2):
				for j in range(y,y+4):
					matrix[i][j]=' '
			self.y=self.y-4
		else:
			return
	def move_down(self,matrix,x,y):
		if matrix[x+2][y]==' ' and matrix[x+3][y+3]==' ':
			for i in range(x+2,x+4):
				for j in range(y,y+4):
					matrix[i][j]='B'

			for i in range(x,x+2):
				for j in range(y,y+4):
					matrix[i][j]=' '
			self.x=self.x+2
		else:
			return
	def move_up(self,matrix,x,y):
		if matrix[x-2][y]==' ' and matrix[x-1][y+3]==' ':
			for i in range(x-2,x):
				for j in range(y,y+4):
					matrix[i][j]='B'

			for i in range(x,x+2):
				for j in range(y,y+4):
					matrix[i][j]=' '
			self.x=self.x-2
		else:
			return
	def death(self,matrix,f,g):
		if (self.x==f and self.y==g) or (self.x==f-2 and self.y==g) or(self.x==f+2 and self.y==g) or (self.x==f and self.y==g+4) or (self.x==f and self.y==g-4):	
			for i in range(self.x,self.x+2):
				for j in range(self.y,self.y+4):
					matrix[i][j]=' '
			matrix[2][4]='B'
			matrix[2][5]='B'
			matrix[2][6]='B'
			matrix[2][7]='B'
			matrix[3][4]='B'
			matrix[3][5]='B'
			matrix[3][6]='B'
			matrix[3][7]='B'
			self.x=2
			self.y=4
			return 1
		else:
			return 0
