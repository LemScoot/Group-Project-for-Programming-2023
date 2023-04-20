class Snake(object):
    
    x = 0
    y = 0
    w = 5
    h = 5
  
def Snake(self, xpos, ypos):
    ypos = ypos
    color = 255
  
    def draw(self):
        self.snake.goto(self.x,self.y)

    def move(self):
        if(keyboard.is_pressed('w')):
            self.y = self.y - 0.1
        if(keyboard.is_pressed('s')):
            self.y = self.y + 0.1
        if(keyboard.is_pressed('a')):
            self.x = self.x - 0.1
        if(keyboard.is_pressed('d')):
            self.x = self.x + 0.1
            self.snake.goto(self.x,self.y)
            
    def display(self):
        color(self.color)
        rect(0, self.ypos, width, self.ypos)
