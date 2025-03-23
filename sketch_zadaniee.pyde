x=0
def setup():
    frameRate(30)
    size(600,400)
def draw():
    global x
    background(225) 
    stroke(60)
    strokeWeight(80)
    point(280,x)
    x=x+1
    
    
    
