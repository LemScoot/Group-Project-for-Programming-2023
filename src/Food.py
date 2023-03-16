class Food:
    x=0
    y=0
    diam=0
    PImage food
    
    Food():
        x = int(10,10)
        y = -100
        diam = int(10,10)
        int rand = int(random(3))
        if (rand == 0):
            food = loadImage("food.png")
            
    def display():
        imageMode(CENTER)
        food.resize(diam, diam)
        image(food,x,y)
