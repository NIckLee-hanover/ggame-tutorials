
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
#keysused = ["right arrow", "left arrow", "W", "A", "S", "D", "space"]
class SpaceShip(Sprite):
    """
    Animated space ship
    """
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,65,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
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
            self.vy += 0.1
            
    def down(self, event):
        if self.vy > -1:
            self.vy -= 0.1
            
    def right(self, event):
        if self.vx < 1:
            self.vx += 0.1

    def left(self, event):
        if self.vx > 1:
            self.vx -= 0.1
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
        SpaceShip((100,100))
        SpaceShip((150,150))
        SpaceShip((200,50))
        
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
                
                
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
            
myapp = SpaceGame()

myapp.run()