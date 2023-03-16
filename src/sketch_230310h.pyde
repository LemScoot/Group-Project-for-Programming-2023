# Lucas Jackson, Liam Scott | Snake-Man | March 2 2023
score = 0
level = 1
play = True

def setup():
    size(1000,1000)
    
def draw():
    background(27,110,0)
    noCursor()
    fill(0)
    rect(mouseX,mouseY,35,35)
    rectMode(CENTER)    
    
    if play:
        startScreen()
    elif play:
        endScreen()
        
    infoPanel()
        
def infoPanel():
    fill(127, 127)
    rectMode(CENTER)
    rect(0,0,width,50)
    textAlign(CENTER)
    textSize(40)
    fill(255)
    #text("Score: " + score + "Level: " + level)
    
def startScreen():
    background(0)
    textAlign(CENTER)
    textSize(40)
    fill(255)
    text("Welcome to the Snake clone", width/2, height/2)
    text("By Python Coding Group", width/2, height/2+30)
    text("Press Spacebar to play this game",width/2, height/2 + 60)
    textSize(30)
    if(key == ' '):
        play = True
        
def endScreen():
    background(0)
    fill(255)
    textAlign(CENTER)
    textSize(40)
    text("Game Over", width/2,height/2)
    play = False
    noLoop()
