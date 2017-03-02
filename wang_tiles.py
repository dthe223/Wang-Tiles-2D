import sys, random
from time import sleep
from graphics import *
sys.setrecursionlimit(10000)

tiles = {1:{'u':'red','l':'blue','r':'yellow','d':'green'},2:{'u':'green','l':'blue','r':'blue','d':'green'},3:{'u':'red','l':'yellow','r':'yellow','d':'red'},4:{'u':'green','l':'yellow','r':'blue','d':'red'},5:{'u':'red','l':'yellow','r':'blue','d':'green'},6:{'u':'green','l':'yellow','r':'yellow','d':'green'},7:{'u':'red','l':'blue','r':'blue','d':'red'},8:{'u':'green','l':'blue','r':'yellow','d':'red'}}

tileMap = []        # 2d array of tessellation
mapSize = 0         # num of rows / columns
tilesPlaced = 0     # keeps track of num of tiles "placed"
totalNeededTiles = mapSize * mapSize    # total num of needed tiles for area
picChoice = ""      # name of pic chosen to use
winSize = 1057#1313      # size of window for graphics
win = GraphWin("Wang Tiles", winSize, winSize)
win.setBackground("white")

def findSafeTile(row, col, disMethod): ## backtracks left->right and up->down
    global tilesPlaced, totalNeededTiles, win
    if (tilesPlaced ==  totalNeededTiles):  # Base Case (SOLUTION)
        if disMethod == "1":
            displayMap(1)
        elif disMethod == "2":
            displayPic(2)
        elif disMethod == "3":
            displayMap(3)
        elif disMethod == "4":
            displayPic(4)
        sys.tracebacklimit = 0
        
        win.getMouse()
        win.close()
        sys.exit()
    if col == mapSize:  # Done w/ row, go to next one
        row += 1
        col = 0
        
    checkTiles = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}  # tracks if tile has been checked curr yet
    random.seed()
    while checkTiles[0] != 8:   # test tiles randomly until one that fits, or all checked
        rtile = random.randrange(1, 9, 1)
        if checkTiles[rtile] == 1:
            continue
        if isSafe(row, col, tiles[rtile]):
            placeTile(row, col, rtile)
            checkTiles[rtile] = 1
            
            findSafeTile(row, col + 1, disMethod)  # move to next col, maybe next row
            
            removeTile(row, col)    # get here only if backtracked
    return

def isSafe(row, col, tileColors):
    global mapSize
    up = left = right = down = True
    if row != 0:            # check up
        if tileMap[row-1][col] != 0 and tiles[tileMap[row-1][col]]['d'] != tileColors['u']:
            up = False
    if col != 0:            # check left
        if tileMap[row][col-1] != 0 and tiles[tileMap[row][col-1]]['r'] != tileColors['l']:
            left = False
    if col != (mapSize -1): # check right
        if tileMap[row][col+1] != 0 and tiles[tileMap[row][col+1]]['l'] != tileColors['r']:
            right = False
    if row != (mapSize -1): # check down
        if tileMap[row+1][col] != 0 and tiles[tileMap[row+1][col]]['u'] != tileColors['d']:
            down = False
    return(up and left and right and down)  # true iff all == True

def placeTile(row, col, tile):
    global tilesPlaced
    tileMap[row][col] = tile
    tilesPlaced += 1
    
def removeTile(row, col):
    global tilesPlaced
    tileMap[row][col] = 0
    tilesPlaced -= 1
    
def displayMap(method):
    global win, winSize, mapSize
   
    if (method == 1): 
        timeDelay = .00
        currx = int(mapSize / 2) - 1
        curry = int(mapSize / 2) - 1
        starti = 1
        if mapSize % 2 == 1:
            currx += 1  # b/c of the truncation of decimal (.5)
            curry += 1
            drawTile(currx, curry, 0)
            sleep(timeDelay)
            currx -= 1
            starti = 2
        for i in range(starti, mapSize, 2): # takes this many loops to fill in area
            for up in range(i): # Loop to go up edge of spiral
                drawTile(currx, curry, 0)
                sleep(timeDelay)
                if up == i-1:   # if curr box is last one, then set currPos to right instead of up
                    currx += 1
                else:
                    curry -= 1
            for right in range(i):  # loop to go right on top of spiral
                drawTile(currx, curry, 0)
                sleep(timeDelay)
                if right == i-1:
                    curry += 1
                else:
                    currx += 1
            for down in range(i):
                drawTile(currx, curry, 0)
                sleep(timeDelay)
                if down == i-1:
                    currx -= 1
                else:
                    curry += 1
            for left in range(i):
                drawTile(currx, curry, 0)
                sleep(timeDelay)
                currx -= 1
    else:
        for row in range(mapSize):
            for col in range(mapSize):
                drawTile(col, row, 0)
    return

def displayPic(method):
    global win, winSize, mapSize
    
    halfSq = 16
    fullSq = 32
    if method == 2:
        timeDelay = .0
        currx = int(mapSize / 2) - 1
        curry = int(mapSize / 2) - 1
        starti = 1
        if  mapSize % 2 == 1:
            currx += 1  # b/c of the truncation fo the decimal (.5)
            curry += 1
            drawTile(currx, curry, 1)
            sleep(timeDelay)
            currx -= 1
            starti = 2
        for i in range(starti, mapSize, 2): # takes this many loops to fill area
            for up in range(i): # loop to go up edge of spiral
                drawTile(currx, curry, 1)
                sleep(timeDelay)
                if up == i-1:   # if curr box is lasy one, then set currPos to right instead of up
                    currx += 1
                else:
                    curry -= 1
            for right in range(i):  # looop to go right on top of spiral
                drawTile(currx, curry, 1)
                sleep(timeDelay)
                if right == i-1:
                    curry += 1
                else:
                    currx += 1
            for down in range(i):
                drawTile(currx, curry, 1)
                sleep(timeDelay)
                if down == i-1:
                    currx -= 1
                else:
                    curry += 1
            for left in range(i):
                drawTile(currx, curry, 1)
                sleep(timeDelay)
                currx -= 1
    else:
        for row in range(mapSize):
            for col in range(mapSize):
                drawTile(col, row, 1)
    return
    
def drawTile(currx, curry, gridOrPic):
    global win, winSize, mapSize
    halfSq = int((winSize/mapSize) / 2)
    fullSq = int(halfSq * 2)
    if gridOrPic == 0:
        ul = Point((halfSq+(fullSq*currx))-halfSq,(halfSq+(fullSq*curry))-halfSq)
        ur = Point((halfSq+(fullSq*currx))+halfSq,(halfSq+(fullSq*curry))-halfSq)
        ll = Point((halfSq+(fullSq*currx))-halfSq,(halfSq+(fullSq*curry))+halfSq)
        lr = Point((halfSq+(fullSq*currx))+halfSq,(halfSq+(fullSq*curry))+halfSq)
        center = Point((halfSq+(fullSq*currx)),(halfSq+(fullSq*curry)))
        up = Polygon(ul, ur, center)
        up.setFill(tiles[tileMap[curry][currx]]['u'])
        left = Polygon(ul, ll, center)
        left.setFill(tiles[tileMap[curry][currx]]['l'])
        right = Polygon(ur, lr, center)
        right.setFill(tiles[tileMap[curry][currx]]['r'])
        down = Polygon(ll, lr, center)
        down.setFill(tiles[tileMap[curry][currx]]['d'])
        up.draw(win)
        left.draw(win)
        right.draw(win)
        down.draw(win)
    else:
        halfSq = 16
        fullSq = 32
        if tileMap[currx][curry] == 1 or tileMap[currx][curry] == 5:
                title = picChoice+"1.gif"
        elif tileMap[currx][curry] == 2 or tileMap[currx][curry] == 6:
            title = picChoice+"2.gif"
        elif tileMap[currx][curry] == 3 or tileMap[currx][curry] == 7:
            title = picChoice+"3.gif"
        else:
            title = picChoice+"4.gif"
            
        tilePic = Image(Point(halfSq+(fullSq*currx), halfSq+(fullSq*curry)), title)
        tilePic.draw(win)
    return


def init():
    global win, winSize, mapSize, totalNeededTiles, picChoice
    fontSize = 26
    mapSizeQuesText = Text(Point(winSize/2,winSize/4), "Enter the size of square you would like to tile?")
    mapSizeQuesText.setSize(fontSize)
    msInput = Entry(Point(winSize/2, winSize/4+winSize/16), 4)
    msInput.setSize(fontSize)
    msInput.setText("25")
    choiceSep = 40
    circleRadius = 15
    circle1 = Circle(Point((3*winSize)/8, (3*winSize)/8+choiceSep), circleRadius)
    
    circle2 = Circle(Point((3*winSize)/8, (3*winSize)/8+choiceSep*2), circleRadius)
    circle3 = Circle(Point((3*winSize)/8, (3*winSize)/8+choiceSep*3), circleRadius)
    circle4 = Circle(Point((3*winSize)/8, (3*winSize)/8+choiceSep*4), circleRadius)
    circlePts = [[circle1.getCenter().getX(),circle1.getCenter().getY()],[circle2.getCenter().getX(),circle2.getCenter().getY()],[circle3.getCenter().getX(),circle3.getCenter().getY()],[circle4.getCenter().getX(),circle4.getCenter().getY()]]
    optSep = 75
    opt1 = Text(Point((winSize/2)+optSep, (3*winSize)/8+choiceSep), "Normal Sprial")
    opt2 = Text(Point((winSize/2)+optSep, (3*winSize)/8+choiceSep*2), "Picture Spiral")
    opt3 = Text(Point((winSize/2)+optSep-5, (3*winSize)/8+choiceSep*3), "Normal Grid")
    opt4 = Text(Point((winSize/2)+optSep, (3*winSize)/8+choiceSep*4), "Picture Grid")
    opt1.setSize(fontSize)
    opt2.setSize(fontSize)
    opt3.setSize(fontSize)
    opt4.setSize(fontSize)
    halfBoxWidth = 50    
    runSq = Rectangle(Point(winSize/2-halfBoxWidth, (3*winSize)/4), Point(winSize/2+halfBoxWidth, (3*winSize)/4+halfBoxWidth))
    runText = Text(runSq.getCenter(), "RUN")
    runText.setSize(24)
    
    mapSizeQuesText.draw(win)
    circle1.draw(win)
    circle2.draw(win)
    circle3.draw(win)
    circle4.draw(win)
    opt1.draw(win)
    opt2.draw(win)
    opt3.draw(win)
    opt4.draw(win)
    runSq.draw(win)
    runText.draw(win)
    msInput.draw(win)
    text = Text(Point(25,25),"")
    text.draw(win)
   
    selectedOpt = "1"  
    while True:   # checks for click in circle or run with size entered
        click = win.getMouse()
        text.undraw()
        xPt = click.getX()
        yPt = click.getY()
        
        if ((circlePts[0][0]-circleRadius)<=xPt and xPt<=(circlePts[0][0]+circleRadius)): # checks if x within circles
            if (circlePts[0][1]-circleRadius<=yPt and yPt<=circlePts[0][1]+circleRadius): # checks if y within circles
                circle1.setFill("Blue"); circle2.setFill("White"); circle3.setFill("White"); circle4.setFill("White")
                selectedOpt = "1"
            elif (circlePts[1][1]-circleRadius<=yPt and yPt<=circlePts[1][1]+circleRadius):
                circle1.setFill("White"); circle2.setFill("Blue"); circle3.setFill("White"); circle4.setFill("White")
                selectedOpt = "2"
                msInput.setText("32")
            elif (circlePts[2][1]-circleRadius<=yPt and yPt<=circlePts[2][1]+circleRadius):
                circle1.setFill("White"); circle2.setFill("White"); circle3.setFill("Blue"); circle4.setFill("White")
                selectedOpt = "3"
            elif (circlePts[3][1]-circleRadius<=yPt and yPt<=circlePts[3][1]+circleRadius):
                circle1.setFill("White"); circle2.setFill("White"); circle3.setFill("White"); circle4.setFill("Blue")
                selectedOpt = "4"
                msInput.setText("32")
        elif runSq.getP1().getX() <= xPt <= runSq.getP2().getX() and msInput.getText()!="": # check if x in run button
            if (runSq.getP1().getY() <= yPt <= runSq.getP2().getY()) and selectedOpt!="":   # check if y in run button
                break                                                                       # also if size and circle have been filled
        
    mapSize = int(msInput.getText())
    totalNeededTiles = mapSize * mapSize
    msInput.undraw()
    cleanUp = Rectangle(Point(-5,-5), Point(winSize+5,winSize+5))
    cleanUp.setFill("white")
    cleanUp.draw(win)
    if selectedOpt == "2" or selectedOpt == "4":
        picChoice()
    return(selectedOpt)

def picChoice():
    global picChoice
    boxWidth = 250
    halfWid = 125
    eigthWid = 31.25
    boxHeight = 90
    halfHei = 45
    fontSize = 16
    edgeABox = Rectangle(Point(winSize/4-halfWid,winSize/6-halfHei),Point(winSize/4+halfWid,winSize/6+halfHei))
    a1 = Image(Point(winSize/4-3*eigthWid,winSize/6-10), "1edgeA/1.gif")
    a2 = Image(Point(winSize/4-eigthWid,winSize/6-10), "1edgeA/2.gif")
    a3 = Image(Point(winSize/4+eigthWid,winSize/6-10), "1edgeA/3.gif")
    a4 = Image(Point(winSize/4+3*eigthWid,winSize/6-10), "1edgeA/4.gif")
    atext = Text(Point(winSize/4,winSize/6+27), "Edge A")
    atext.setSize(fontSize)
   
    edgeBBox = Rectangle(Point(winSize/4-halfWid,2*winSize/6-halfHei),Point(winSize/4+halfWid,2*winSize/6+halfHei))
    b1 = Image(Point(winSize/4-3*eigthWid,2*winSize/6-10), "1edgeB/1.gif")
    b2 = Image(Point(winSize/4-eigthWid,2*winSize/6-10), "1edgeB/2.gif")
    b3 = Image(Point(winSize/4+eigthWid,2*winSize/6-10), "1edgeB/3.gif")
    b4 = Image(Point(winSize/4+3*eigthWid,2*winSize/6-10), "1edgeB/4.gif")
    btext = Text(Point(winSize/4,2*winSize/6+27), "Edge B")
    btext.setSize(fontSize)

    wall3dBox = Rectangle(Point(winSize/4-halfWid,3*winSize/6-halfHei),Point(winSize/4+halfWid,3*winSize/6+halfHei))
    wall1 = Image(Point(winSize/4-3*eigthWid,3*winSize/6-10), "3dWall-4/1.gif")
    wall2 = Image(Point(winSize/4-eigthWid,3*winSize/6-10), "3dWall-4/2.gif")
    wall3 = Image(Point(winSize/4+eigthWid,3*winSize/6-10), "3dWall-4/2.gif")
    wall4 = Image(Point(winSize/4+3*eigthWid,3*winSize/6-10), "3dWall-4/4.gif")
    walltext = Text(Point(winSize/4,3*winSize/6+27), "3D Wall")
    walltext.setSize(fontSize)

    bowTieBox = Rectangle(Point(winSize/4-halfWid,4*winSize/6-halfHei),Point(winSize/4+halfWid,4*winSize/6+halfHei))
    bowTie1 = Image(Point(winSize/4-3*eigthWid,4*winSize/6-10), "BowTie/1.gif")
    bowTie2 = Image(Point(winSize/4-eigthWid,4*winSize/6-10), "BowTie/2.gif")
    bowTie3 = Image(Point(winSize/4+eigthWid,4*winSize/6-10), "BowTie/3.gif")
    bowTie4 = Image(Point(winSize/4+3*eigthWid,4*winSize/6-10), "BowTie/4.gif")
    bowTietext = Text(Point(winSize/4,4*winSize/6+27), "Bow Tie")
    bowTietext.setSize(fontSize)

    braidBox = Rectangle(Point(winSize/4-halfWid,5*winSize/6-halfHei),Point(winSize/4+halfWid,5*winSize/6+halfHei))
    braid1 = Image(Point(winSize/4-3*eigthWid,5*winSize/6-10), "Braid/1.gif")
    braid2 = Image(Point(winSize/4-eigthWid,5*winSize/6-10), "Braid/2.gif")
    braid3 = Image(Point(winSize/4+eigthWid,5*winSize/6-10), "Braid/3.gif")
    braid4 = Image(Point(winSize/4+3*eigthWid,5*winSize/6-10), "Braid/4.gif")
    braidtext = Text(Point(winSize/4,5*winSize/6+27), "Braid")
    braidtext.setSize(fontSize)

    bubblesBox = Rectangle(Point(3*winSize/4-halfWid,winSize/6-halfHei),Point(3*winSize/4+halfWid,winSize/6+halfHei))
    bubbles1 = Image(Point(3*winSize/4-3*eigthWid,winSize/6-10), "Bubbles/1.gif")
    bubbles2 = Image(Point(3*winSize/4-eigthWid,winSize/6-10), "Bubbles/2.gif")
    bubbles3 = Image(Point(3*winSize/4+eigthWid,winSize/6-10), "Bubbles/3.gif")
    bubbles4 = Image(Point(3*winSize/4+3*eigthWid,winSize/6-10), "Bubbles/4.gif")
    bubblestext = Text(Point(3*winSize/4,winSize/6+27), "Bubbles")
    bubblestext.setSize(fontSize)

    dublinBox = Rectangle(Point(3*winSize/4-halfWid,2*winSize/6-halfHei),Point(3*winSize/4+halfWid,2*winSize/6+halfHei))
    dublin1 = Image(Point(3*winSize/4-3*eigthWid,2*winSize/6-10), "Dublin/1.gif")
    dublin2 = Image(Point(3*winSize/4-eigthWid,2*winSize/6-10), "Dublin/2.gif")
    dublin3 = Image(Point(3*winSize/4+eigthWid,2*winSize/6-10), "Dublin/3.gif")
    dublin4 = Image(Point(3*winSize/4+3*eigthWid,2*winSize/6-10), "Dublin/4.gif")
    dublintext = Text(Point(3*winSize/4,2*winSize/6+27), "Dublin")
    dublintext.setSize(fontSize)
        
    osloBox = Rectangle(Point(3*winSize/4-halfWid,3*winSize/6-halfHei),Point(3*winSize/4+halfWid,3*winSize/6+halfHei))
    oslo1 = Image(Point(3*winSize/4-3*eigthWid,3*winSize/6-10), "Oslo/1.gif")
    oslo2 = Image(Point(3*winSize/4-eigthWid,3*winSize/6-10), "Oslo/2.gif")
    oslo3 = Image(Point(3*winSize/4+eigthWid,3*winSize/6-10), "Oslo/3.gif")
    oslo4 = Image(Point(3*winSize/4+3*eigthWid,3*winSize/6-10), "Oslo/4.gif")
    oslotext = Text(Point(3*winSize/4,3*winSize/6+27), "Oslo")
    oslotext.setSize(fontSize)
        
    poolBox = Rectangle(Point(3*winSize/4-halfWid,4*winSize/6-halfHei),Point(3*winSize/4+halfWid,4*winSize/6+halfHei))
    pool1 = Image(Point(3*winSize/4-3*eigthWid,4*winSize/6-10), "Pool/1.gif")
    pool2 = Image(Point(3*winSize/4-eigthWid,4*winSize/6-10), "Pool/2.gif")
    pool3 = Image(Point(3*winSize/4+eigthWid,4*winSize/6-10), "Pool/3.gif")
    pool4 = Image(Point(3*winSize/4+3*eigthWid,4*winSize/6-10), "Pool/4.gif")    
    pooltext = Text(Point(3*winSize/4,4*winSize/6+27), "Pool")
    pooltext.setSize(fontSize)    

    romeBox = Rectangle(Point(3*winSize/4-halfWid,5*winSize/6-halfHei),Point(3*winSize/4+halfWid,5*winSize/6+halfHei))
    rome1 = Image(Point(3*winSize/4-3*eigthWid,5*winSize/6-10), "Rome-4/1.gif")
    rome2 = Image(Point(3*winSize/4-eigthWid,5*winSize/6-10), "Rome-4/2.gif")
    rome3 = Image(Point(3*winSize/4+eigthWid,5*winSize/6-10), "Rome-4/3.gif")
    rome4 = Image(Point(3*winSize/4+3*eigthWid,5*winSize/6-10), "Rome-4/4.gif")    
    rometext = Text(Point(3*winSize/4,5*winSize/6+27), "Rome")
    rometext.setSize(fontSize)

    edgeABox.draw(win)
    edgeBBox.draw(win)
    wall3dBox.draw(win)
    bowTieBox.draw(win)
    #braidBox.draw(win)
    bubblesBox.draw(win)
    dublinBox.draw(win)
    osloBox.draw(win)
    poolBox.draw(win)
    romeBox.draw(win)
    a1.draw(win)
    a2.draw(win)
    a3.draw(win)
    a4.draw(win)
    b1.draw(win)
    b2.draw(win)
    b3.draw(win)
    b4.draw(win)
    wall1.draw(win)
    wall2.draw(win)
    wall3.draw(win)
    wall4.draw(win)    
    bowTie1.draw(win)
    bowTie2.draw(win)
    bowTie3.draw(win)
    bowTie4.draw(win)
    #braid1.draw(win)
    #braid2.draw(win)
    #braid3.draw(win)
    #braid4.draw(win)
    bubbles1.draw(win)
    bubbles2.draw(win)
    bubbles3.draw(win)
    bubbles4.draw(win)
    dublin1.draw(win)
    dublin2.draw(win)
    dublin3.draw(win)
    dublin4.draw(win)
    oslo1.draw(win)
    oslo2.draw(win)
    oslo3.draw(win)
    oslo4.draw(win)
    pool1.draw(win)
    pool2.draw(win)
    pool3.draw(win)
    pool4.draw(win)
    rome1.draw(win)
    rome2.draw(win)
    rome3.draw(win)
    rome4.draw(win)
    atext.draw(win)
    btext.draw(win)
    walltext.draw(win)
    bowTietext.draw(win)
    #braidtext.draw(win)
    bubblestext.draw(win)
    dublintext.draw(win)
    oslotext.draw(win)
    pooltext.draw(win)
    rometext.draw(win)
    
    choice = ""
    while True:
        click = win.getMouse()
        xPt = click.getX()
        yPt = click.getY()
        if winSize/4-halfWid <= xPt <= winSize/4+halfWid:
            if winSize/6-halfHei <= yPt <= winSize/6+halfHei:
                picChoice = "1edgeA/"
                break
            elif 2*winSize/6-halfHei <= yPt <= 2*winSize/6+halfHei:
                picChoice = "1edgeB/"
                break
            elif 3*winSize/6-halfHei <= yPt <= 3*winSize/6+halfHei:
                picChoice = "3dWall-4/"
                break
            elif 4*winSize/6-halfHei <= yPt <= 4*winSize/6+halfHei:
                picChoice = "BowTie/"
                break
            elif 5*winSize/6-halfHei <= yPt <= 5*winSize/6+halfHei:
                picChoice = "Braid/"            
        elif 3*winSize/4-halfWid <= xPt <= 3*winSize/4+halfWid:
            if winSize/6-halfHei <= yPt <= winSize/6+halfHei:
                picChoice = "Bubbles/"
                break
            elif 2*winSize/6-halfHei <= yPt <= 2*winSize/6+halfHei:
                picChoice = "Dublin/"
                break
            elif 3*winSize/6-halfHei <= yPt <= 3*winSize/6+halfHei:
                picChoice = "Oslo/"
                break
            elif 4*winSize/6-halfHei <= yPt <= 4*winSize/6+halfHei:
                picChoice = "Pool/"
                break
            elif 5*winSize/6-halfHei <= yPt <= 5*winSize/6+halfHei:
                picChoice = "Rome-4/"            
                break
    return

def main():
    selectedOpt = init()
    for row in range(mapSize):  # initializes 2d array to 0
        row = []
        for col in range(mapSize):
            row.append(0)
        tileMap.append(row)
    
    findSafeTile(0, 0, selectedOpt)  # start backtracking at (0,0) pos
    
main()