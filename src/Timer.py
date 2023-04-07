# Liam Scott | 3/16/23 | Computer Programming

class Timer: 

    int savedTime
    int totalTime
  
    def start():
        savedTime = millis()
    
    boolean isFinished():
        int passedTime = millis()- savedTime
        if (passedTime > totalTime):
            return True
        else:
            return False
