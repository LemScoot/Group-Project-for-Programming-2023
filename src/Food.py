# Liam Scott | 3/16/23 | Computer Programming

class Food:
    x = 0
    y = 0
    diam = 0
    
    def Food(self):
        self.x = 500
        self.y = -100
        self.diam = int(10,10)
        self.rand = int(random(3))
        if (rand == 0):
            food = loadImage("food.png")
            
    def display(self):
        imageMode(CENTER)
        food.resize(diam, diam)
        image(food,x,y)