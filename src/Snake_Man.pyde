# Liam Scott | Snake-Man | Mar 2, 2023

# ArrayList<Food> apples = new ArrayList<Food>()
score = 0
level = 1
boolean = play
from PIL import Image

def setup():
    fullScreen()
    # Apples
    #apples = new Food()
    
    # Random Stuff
    play = false
    
def draw():
    background(27, 100 ,0)
    noCursor()
    fill(0)
    rect(mouseX, mouseY, 35, 35)
    rectMode(CENTER)
    
    # Checks to see if the StartScreen is going to appear
    if(!play):
        startScreen()
    elif(play):
        endScreen()
        
    try:
        img = Image.open("Stage 1.png")
    
    # Other Methods    
    infoPanel()

def infoPanel():
    fill(127, 127)
    rectMode(CENTER)
    rect(0, 0, width, 50)
    textAlign(CENTER)
    textSize(40)
    fill(255)
    text("Score: " + score + "Level: " + level, width/2, 40)
    
def startScreen():
    background(0)
    textAlign(CENTER)
    textSize(40)
    fill(255)
    text("Welcome to PLACEHOLDER GAME name", width/2, height/2)
    text("By Python Coding Group", width/2, height/2+30)
    text("Press Any Key to Start", width/2, height/2)
    if(keyPressed):
        play = true
        
def endScreen():
    background(0)
    fill(255)
    textAlign(CENTER)
    textSize(40)
    text("Game Over", width/2, height/2)
    play = false
    noLoop()
