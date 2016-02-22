#function that takes an integer and prints that number of rows and columns in asterisks

def draw_square(integer):
	for i in range(0, integer):
		print "* " * integer

#function that draws a checkerboard 

def draw_checkerboard():
	for i in range (0, 4):
		print " x o" * 4 
		print " o x" * 4 
