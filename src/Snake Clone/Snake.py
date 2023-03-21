# Liam Scott | 3/16/23 | Computer Programming

class Snake:

    x = 0
    y = 0
  
def Snake(self):
    self.snake.shape('square')
    self.snake.color("white")
    self.snake.penup()
    self.snake.goto(self.x,self.y)
  
    def draw(self):
        self.snake.goto(self.x,self.y)

    def tick(self):
        if(keyboard.is_pressed('w')):
            self.y = self.y - 0.1
        if(keyboard.is_pressed('s')):
            self.y = self.y + 0.1
        if(keyboard.is_pressed('a')):
            self.x = self.x - 0.1
        if(keyboard.is_pressed('d')):
            self.x = self.x + 0.1
            self.snake.goto(self.x,self.y)
