from ggame import App, RectangleAsset, ImageAsset, SoundAsset
from ggame import LineStyle, Color, Sprite, Sound

myapp = App()

green = Color(0x00ff00, 1)
black = Color(0, 1)
noline = LineStyle(0, black)

bg_asset = RectangleAsset(myapp.width, myapp.height, noline, green)
bg = Sprite(bg_asset, (0,0))

myapp.run()

