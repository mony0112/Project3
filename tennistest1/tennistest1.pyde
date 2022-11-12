posX = -400
posY = posX**2
def setup():
    size(800,600)

def draw():
    background(174,98,200)
    global posX
    global posY
    fill(237,200,17)
    ellipse(posX+400,posY,40,40)
    posX = posX + 2
    posY = posX**2/250
    if posX > 400:
        posX = -400
