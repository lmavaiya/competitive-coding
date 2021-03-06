n=4

def is_safe(maze,x,y):
	if x<n and y<n and maze[x][y]==1:
		return True
	return False

def rat_in_maze(maze,x,y,sol):
	
	#Base case
	if x==n-1 and y==n-1:
		sol[x][y]=1
		for i in sol:
			print(i,end="\n")
		return True

	if is_safe(maze,x,y):
		sol[x][y]=1

		if rat_in_maze(maze,x+1,y,sol)==True:
			return True

		
		if rat_in_maze(maze,x,y+1,sol)==True:
			return True

		sol[x][y]=0
		return False
	
	return False



if __name__ == '__main__':
	maze=[	[1,0,0,0],
			[1,1,1,1],
			[0,1,0,0],
			[1,1,1,1]]

	sol=[	[0,0,0,0],
			[0,0,0,0],
			[0,0,0,0],
			[0,0,0,0]]


	print(rat_in_maze(maze,0,0,sol))

