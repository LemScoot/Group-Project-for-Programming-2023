# Liam Scott | Snake-Man | Mar 2, 2023

# Imports
from Food import Food
from Snake import Snake

score = 0
play = False # Change to False if you want to play

def setup():
    size(900,1000)
    global img
    img = loadImage("Stage 1.png")
    
def draw():
    # background(27,110,0)
    image(img, 0, 100)   
    
    if play:
        startScreen()
    elif play:
        background(0)
        noCursor()
        
    infoPanel()
        
def infoPanel():
    fill(13.3, 54.5, 13.3)
    rectMode(CENTER)
    rect(0, 0, 2000, 200)
    textAlign(CENTER)
    textSize(40)
    fill(255)
    text("Score: ", 100, 60)
    
def startScreen():
    background(0)
    textAlign(CENTER)
    textSize(40)
    fill(255)
    text("Welcome to the Snake clone", width/2, height/2)
    text("By Python Coding Group", width/2, height/2+30)
    text("Press Spacebar to play this game",width/2, height/2 + 60)
    textSize(30)
    if(keyPressed == ' '):
        play = True
        
def endScreen():
    background(0)
    fill(255)
    textAlign(CENTER)
    textSize(40)
    text("Game Over", width/2,height/2)
    play = False
    noLoop()
