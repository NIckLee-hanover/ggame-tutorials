from random import randint
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
#keysused = ["right arrow", "left arrow", "W", "A", "S", "D", "space"]

class SpaceShip(Sprite):
    ship = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,65,125), 4, 'vertical')
        
    def __init__(self, position):
        super().__init__(SpaceShip.ship, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.thrust = 0
        self.thrustframe = 1
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.rotRgo)
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.rotRstop)
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.rotLgo)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.rotRstop)
        
        SpaceGame.listenKeyEvent("keyup", "w", self.up)
        SpaceGame.listenKeyEvent("keydown", "w", self.down)
        SpaceGame.listenKeyEvent("keyup", "a", self.right)
        SpaceGame.listenKeyEvent("keydown", "a", self.left)
        SpaceGame.listenKeyEvent("keyup", "s", self.down)
        SpaceGame.listenKeyEvent("keydown", "s", self.up)
        SpaceGame.listenKeyEvent("keyup", "d", self.left)
        SpaceGame.listenKeyEvent("keydown", "d", self.right)
        self.fxcenter = self.fycenter = 0.5
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        # manage thrust animation
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)
        
    def thrustOn(self, event):
        self.thrust = 1
        
    def thrustOff(self, event):
        self.thrust = 0
    
    def rotRgo(self, event):
        self.vr = -0.05
        
    def rotRstop(self, event):
        self.vr = 0
        
    def rotLgo(self, event):
        self.vr = 0.05
        
    def rotLstop(self, event):
        self.vr = 0
        
    def up(self, event):
        if self.vy < 1:
            self.vy += 0.2
            
    def down(self, event):
        if self.vy > -1:
            self.vy -= 0.2
            
    def right(self, event):
        if self.vx < 1:
            self.vx += 0.2

    def left(self, event):
        if self.vx > -1:
            self.vx -= 0.2
    
class blast(Sprite):
    boom = ImageAsset("images/blast.png",
        Frame(0,0,8,8), 4,'horizontal')
        
    def __init__(self, position):
        super().__init__(blast.boom, position)
        self.newx = 0
        self.newy = 0
        self.blastgo = 0
        self.blastframe = 1
        SpaceGame.listenKeyEvent("keydown", "e", self.blastOn)
        SpaceGame.listenKeyEvent("keyup", "e", self.blastOff)

    def step(self):
        self.x += 0
        self.y += 0
        self.setImage(self.blastframe)
        if self.blastgo == 1:
            print('asodfas0)')
            self.newx = randint(0,10)
            self.newy = 1
            self.setImage(self.blastframe)
            self.blastframe += 1
            if self.blastframe == 7:
                self.blastframe = 3
        else:
            self.setImage(0)


  
    def blastOn(self, event):
        self.blastgo = 1

    def blastOff(self, event):
        self.blastgo = 0
        
class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self):
        super().__init__()
        # Background
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(self.width, self.height, noline, black)
        bg = Sprite(bg_asset, (0,0))
        blast((100,100))
    
        SpaceShip((100,100))
        SpaceShip((150,150))
        SpaceShip((200,200))
        blast((100,100))
        blast((200,200))
    
    def step(self):
        print('s')
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
            #print('a2')
        for boom in self.getSpritesbyClass(blast):
            boom.step()
            #print('r')
myapp = SpaceGame()

myapp.run()