"""
tutorial3.py
by Nick Lee
"""


from ggame import App, RectangleAsset, ImageAsset, SoundAsset
from ggame import LineStyle, Color, Sprite, Sound

myapp = App()

# define colors and line style
green = Color(0x00ff00, 1)
black = Color(0, 1)
noline = LineStyle(0, black)

# a rectangle asset and sprite to use as background
bg_asset = RectangleAsset(myapp.width, myapp.height, noline, green)
bg = Sprite(bg_asset, (0,0))

# A ball! This is already in the ggame-tutorials repository
ball_asset = ImageAsset("images/orb-150545_640.png")
ball = Sprite(ball_asset, (0, 0))

# Original image is too big. Scale it to 1/10 its original size
ball.scale = 0.1

# # custom attributes
ball.direction = 1
ball.go = True

# sounds
pew1_asset = SoundAsset("sounds/pew1.mp3")
pew1 = Sound(pew1_asset)
pop_asset = SoundAsset("sounds/reappear.mp3")
pop = Sound(pop_asset)


def reverse(b):
    b.direction *= -1
    pop.play()

def step():
    if ball.go:
        ball.x += ball.direction
        if ball.x + ball.width > myapp.width or ball.x < 0:
            ball.x -= ball.direction
            reverse(ball)
            
def spaceKey(event):
    ball.go = not ball.go
    
def reverseKey(event):
    reverse(ball)
    pop.play()
    
def mouseClick(event):
    ball.x = event.x
    ball.y = event.y
    pew1.play()
    
myapp.listenKeyEvent('keydown', 'space', spaceKey)
myapp.listenKeyEvent('keydown', 'r', reverseKey)
myapp.listenMouseEvent('click', mouseClick)

myapp.run(step)
