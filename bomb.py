import config
#Class to implement bomb by bomberman
class Bomb():
# function to explode the nearby bricks or enemies
	def explode(self,matrix,x,y,ch):
		for i in range(1,5):
			if matrix[x][y-i]=='/':
				config.score+=5
			if matrix[x][y-i]=='E':
				config.score+=25
#if nearby any wall is present then it doesn't explode
			if matrix[x][y-i]=='X':
				break
			else:
				matrix[x][y-i]=ch
				matrix[x+1][y-i]=ch
		for i in range(4,8):
			if matrix[x][y+i]=='/':
				config.score+=5
			if matrix[x][y+i]=='E':
				config.score+=25
			if matrix[x][y+i]=='X':
				break
			else:
				matrix[x][y+i]=ch
				matrix[x+1][y+i]=ch
		for i in range(2,4):
			if matrix[x+i][y]=='/':
				config.score+=10
			if matrix[x+i][y]=='E':
				config.score+=50
			if matrix[x+i][y]=='X':
				break
			else:
				matrix[x+i][y]=ch
				matrix[x+i][y+1]=ch
				matrix[x+i][y+2]=ch
				matrix[x+i][y+3]=ch
		for i in range(1,3):
			if matrix[x-i][y]=='/':
				config.score+=10
			if matrix[x-i][y]=='E':
				config.score+=50
			if matrix[x-i][y]=='X':
				break
			else:
				matrix[x-i][y]=ch
				matrix[x-i][y+1]=ch
				matrix[x-i][y+2]=ch
				matrix[x-i][y+3]=ch

