import sys, random
from graphics import *
sys.setrecursionlimit(10000)

tiles = {1:{'u':'red','l':'blue','r':'yellow','d':'green'},2:{'u':'green','l':'blue','r':'blue','d':'green'},3:{'u':'red','l':'yellow','r':'yellow','d':'red'},4:{'u':'green','l':'yellow','r':'blue','d':'red'},5:{'u':'red','l':'yellow','r':'blue','d':'green'},6:{'u':'green','l':'yellow','r':'yellow','d':'green'},7:{'u':'red','l':'blue','r':'blue','d':'red'},8:{'u':'green','l':'blue','r':'yellow','d':'red'}}

tileMap = []
mapSize = 0
tilesPlaced = 0
totalNeededTiles = mapSize * mapSize
winSize = 608
win = GraphWin("Wang Tiles", 628, 628)
	
def findSafeTile(row, col):
	global tilesPlaced, totalNeededTiles, win
	if (tilesPlaced == totalNeededTiles): # Base Case: A SOLUTION
		displayMap()
		sys.tracebacklimit = 0
		
		win.getMouse()
		win.close()
		sys.exit()
	if (col == mapSize): # Done with row, go to next one
		row += 1
		col = 0
		
	checkTiles = {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
	random.seed()
	while (checkTiles[0] != 8): # Test tiles randomly until find one to fit or checks them all
		rtile = random.randrange(1, 9, 1)
		if (checkTiles[rtile] == 1):
			continue
	#for rtile in range(1,9,1):
		if (isSafe(row, col, tiles[rtile])): # If safe then place it
			placeTile(row, col, rtile)
			checkTiles[rtile] = 1		

			# Move onto the next col, maybe next row
			findSafeTile(row, col + 1)

			# If we get here, we've backtracked
			removeTile(row, col)
	return
			
def isSafe(row, col, tileColors):
	global mapSize
	up = True; left = True; right = True; down = True
	if (row != 0):    # Check Up
		if (tileMap[row-1][col] != 0 and tiles[tileMap[row-1][col]]['d'] != tileColors['u']):
			up = False
	if (col != 0):    # Check Left
		if (tileMap[row][col-1] != 0 and tiles[tileMap[row][col-1]]['r'] != tileColors['l']):
			left = False
	if (col != (mapSize - 1)):    # Check Right
		if (tileMap[row][col+1] != 0 and tiles[tileMap[row][col+1]]['l'] != tileColors['r']):
			right = False
	if (row != (mapSize - 1)):    # Check Down
		if (tileMap[row+1][col] != 0 and tiles[tileMap[row+1][col]]['u'] != tileColors['d']):
			down = False
	return (up and left and right and down)

def placeTile(row, col, tile):
	global tilesPlaced
	tileMap[row][col] = tile
	tilesPlaced += 1
	
def removeTile(row, col):
	global tilesPlaced
	tileMap[row][col] = 0
	tilesPlaced -= 1
	
def displayMap():
	global win,winSize,mapSize
	
	halfSq = int((winSize/mapSize) / 2)
	fullSq = int(winSize/mapSize)
	for row in range(mapSize):
		for col in range(mapSize):
			
			'''if (tileMap[row][col] == 1 or tileMap[row][col] == 5):
				title = "1.gif"
			elif (tileMap[row][col] == 1 or tileMap[row][col] == 6):
				title = "2.gif"
			elif (tileMap[row][col] == 3 or tileMap[row][col] == 7):
				title = "3.gif"
			else:
				title = "4.gif"'''
			'''elif (tileMap[row][col] == 4):
				title = "4.gif"
			elif (tileMap[row][col] == 5):
				title = "5.gif"
			elif (tileMap[row][col] == 6):
				title = "6.gif"
			elif (tileMap[row][col] == 7):
				title = "7.gif"
			else:
				title = "8.gif"'''
			
			'''tilePic = Image(Point(16+(32*col),16+(32*row)), title)
			tilePic.draw(win)'''
			
			ul = Point((halfSq+(fullSq*col))-halfSq,(halfSq+(fullSq*row))-halfSq)
			ur = Point((halfSq+(fullSq*col))+halfSq,(halfSq+(fullSq*row))-halfSq)
			ll = Point((halfSq+(fullSq*col))-halfSq,(halfSq+(fullSq*row))+halfSq)
			lr = Point((halfSq+(fullSq*col))+halfSq,(halfSq+(fullSq*row))+halfSq)
			center = Point((halfSq+(fullSq*col)),(halfSq+(fullSq*row)))
			up = Polygon(ul, ur, center)
			up.setFill(tiles[tileMap[row][col]]['u'])
			left = Polygon(ul, ll, center)
			left.setFill(tiles[tileMap[row][col]]['l'])
			right = Polygon(ur, lr, center)
			right.setFill(tiles[tileMap[row][col]]['r'])
			down = Polygon(ll, lr, center)
			down.setFill(tiles[tileMap[row][col]]['d'])
			up.draw(win)
			left.draw(win)
			right.draw(win)
			down.draw(win)
			
	win.getMouse()
	win.close()
	
def main():
	global mapSize, totalNeededTiles
	mapSize = int(input("Enter the size of square you would like to tile: "))
	totalNeededTiles = mapSize * mapSize
	for row in range(mapSize):
		row = []
		for col in range(mapSize):
			row.append(0)
		tileMap.append(row)
	
	findSafeTile(0, 0)
main()