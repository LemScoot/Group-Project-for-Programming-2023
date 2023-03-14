# Liam Scott | Snake-Man | Mar 2, 2023

score = 0
level = 1
play = True
# from PIL import Image

def setup():
    size(1000, 1000)
    # apples = new Food()
    
def draw():
    background(255)
    noCursor()
    fill(0)
    rect(mouseX, mouseY, 35, 35)
    rectMode(CENTER)
    Food.display()
    
    # Checks to see if the StartScreen is going to appear
    if play:
        startScreen()
    elif play:
        endScreen()
        
    # try:
    #     img = Image.open("Stage 1.png")
    
    # Other Methods    
    infoPanel()

def infoPanel():
    fill(127, 127)
    rectMode(CENTER)
    rect(0, 0, width, 250)
    textAlign(CENTER)
    textSize(40)
    fill(255)
    # text("Score: " + score + "Level: " + level, width/2, 40)
    
def startScreen():
    background(0)
    textAlign(CENTER)
    textSize(40)
    fill(255)
    text("Welcome to PLACEHOLDER GAME name", width/2, height/2+50)
    text("By Python Coding Group", width/2, height/2+90)
    text("Press SpaceBar to Start", width/2, height/2)
    if(key == ' '):
        play = True
        
def endScreen():
    background(0)
    fill(255)
    textAlign(CENTER)
    textSize(40)
    text("Game Over", width/2, height/2)
    play = False
    noLoop()
