# Lucas Jackson, Liam Scott | Snake-Man | March 2 2023
# Imports
from Snake import Snake

play = False
score = 0
value = 0# Change to False if you want to play

def setup():
    size(900,1000)
    global img,gif
    img = loadImage("Stage 1.png")
    gif = loadImage("startscreen.gif")
    
def draw():
    if not play:
        image(img, 0, 100)   
        fill(value)
        rectMode(CENTER)
        rect(width/2,height/2,900,1000)
        infoPanel()
    elif play:
        startScreen()
    
    image(img, 0 ,0)
    image(gif, -45, 0)
    
    textSize(20)
    fill(13.3, 54.5, 13.3)
    text("Welcome to Snake Clone", 715, 550)
    text("By the Python Coding Group", 715, 575)
    text("Wait a couple seconds", 705, 625)
    text("for the game to start", 705, 650)
    
    #if (foodTimer.isFinished()):
        #Food.add(new Food())
        #foodTimer.start()

def infoPanel():
    fill(13.3, 54.5, 13.3)
    rectMode(CENTER)
    rect(0, 0, 2000, 200)
    textAlign(CENTER)
    textSize(40)
    fill(255)
    text("Score: ", 100, 60)

def keyPressed():
    global img,gif
    if gif == 0:
        gif = loadImage("startscreen.gif")
    else:
        img = loadImage("Stage 1.png")
        
def startScreen():
    global gif
    gif = loadImage("Startscreen.gif")
    textAlign(CENTER)
    textSize(40)
    fill(255)
    text("Welcome to the Snake clone", width/2, height/2)
    text("Press Spacebar to play this game",width/2, height/2 + 60)
    if(keyPressed):
        play = True
        
def endScreen():
    background(0)
    fill(255)
    textAlign(CENTER)
    textSize(40)
    text("Game Over", width/2,height/2)
    play = False
    noLoop()
    
