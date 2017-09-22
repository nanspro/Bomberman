from __future__ import print_function
from termcolor import colored
import config
import os,sys
class Wall:
	def __init__(self,matrix):
		for i in range(0,44,1):
			if i==0 or i==1 or i==42 or i==43:
				for j in range(0,88,1):
					matrix[i][j]="X"
			else:
				for j in range(0,88,1):
					if j==0 or j==1 or j==2 or j==3 or j==86 or j==87 or j==85 or j==84:
						matrix[i][j]="X"
					else:
						matrix[i][j]=" "

		for i in range(4,40,4):
			for j in range(8,80,8):
				for k in range(0,2):
					for l in range(0,4):
						matrix[i+k][j+l]="X"
		matrix[2][4]='B'
		matrix[2][5]='B'
		matrix[2][6]='B'
		matrix[2][7]='B'
		matrix[3][4]='B'
		matrix[3][5]='B'
		matrix[3][6]='B'
		matrix[3][7]='B'


	def show(self,matrix):
		os.system('clear')
		for i in range(0,44):
			for j in range(0,88):
				if matrix[i][j]=='E':
					print (colored(matrix[i][j],"red"),end='')
				elif matrix[i][j]=='B':
					print (colored(matrix[i][j],"green"),end='')
				elif matrix[i][j]=='X':
					print (colored(matrix[i][j],"blue"),end='')
				elif matrix[i][j]=='/':
					print (colored(matrix[i][j],"yellow"),end='')
				else:
					print(matrix[i][j],end='')
			print("")
		print("Lives left: "+str(config.lives)+"  " +"Score: "+str(config.score))



