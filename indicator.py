import pygame

# Initialize Pygame
pygame.init()

# Set window size and title
window_size = (512, 512)
window_title = "Crypto Indicator"
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)
MenuStatus = "main"
TitleText = "Main Menu"

# Load and set window icon
icon = pygame.image.load("images/logo.png")
pygame.display.set_icon(icon)

# Load background image
bg = pygame.image.load("images/bg.png")

# Draw background on screen
screen.blit(bg, (0, 0))

global GlobalTransition
GlobalTransition = 0
global GlobalTradeMenu
GlobalTradeMenu = 1

# Create button class
class Button:
    def __init__(self, x, y, Oimg, title):
        # Load button image
        buttons.append(self)
        self.image = pygame.image.load("images/btn.png")
        self.image = self.image.convert_alpha()
        self.Oimage = pygame.image.load(Oimg)
        self.Oimage = self.Oimage.convert_alpha()
        self.x = x
        self.y = y
        self.mouseHover = 0
        self.title = title
        self.alpha = 0
        self.created = 1

    def draw_button(self):
        global GlobalTransition
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.Oimage, (self.x + 28, self.y + 28))
        if GlobalTransition == 1:
            self.y += 1
            self.alpha -= 3
            self.image.set_alpha(self.alpha)
            self.Oimage.set_alpha(self.alpha)
            global buttons
            if self.alpha <= 0:
                self.alpha = 0
                del self
                buttons = []
        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # Check if mouse is over the button
        if GlobalTransition == 0:
            if self.created == 1:
                if self.alpha < 255:
                    self.alpha += 3
                else:
                    self.alpha = 255
            if self.alpha == 255:
                if self.created > 0:
                    self.created -= 0.25
            if self.x <= mouse_x <= self.x + self.image.get_width() and self.y <= mouse_y <= self.y + self.image.get_height() and self.created == 0:
                self.mouseHover = 1
                self.image.set_alpha(self.alpha/2)
                self.Oimage.set_alpha(self.alpha/2)
                if mouse_click[0] == 1:
                    global MenuStatus, TitleText
                    MenuStatus = self.title
                    TitleText = self.title
            else:
                self.mouseHover = 0
                self.image.set_alpha(self.alpha)
                self.Oimage.set_alpha(self.alpha)

class TitleObj:

    def __init__(self):
        # Load title background image
        self.img = pygame.image.load("images/title_bg.png")
        self.x = 0
        self.y = 0
        self.rdy = 1

    def update(self):
        if self. y == 0 and self.rdy != 1:
            self.rdy += 0.25
        else:
            self.rdy = 0
        screen.blit(self.img, (self.x, self.y))
        global GlobalTransition
        if GlobalTransition == 1:
            if self.y > -16:
                self.y -= 0.2
            else:
                self.y = -16
        if GlobalTransition == 2:
            if self.y < 0:
                self.y += 0.2
            else:
                self.y = 0
                MenuStatus = "main"
                GlobalTransition = 0

class returnBtn:
    def __init__(self):
        # Load title background image
        self.img = pygame.image.load("images/icon_return.png")
        self.img2 = pygame.image.load("images/icon_return2.png")
        self.x = 32
        self.y = 32
        self.Yy = self.y
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def update(self):
        global GlobalTransition
        global MenuStatus
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        if self.x < mouse_pos[0] < self.x + self.width and self.Yy < mouse_pos[1] < self.Yy + self.height and buttons == []:
            screen.blit(self.img2, (self.x, self.Yy))
            if mouse_click[0] == 1 and GlobalTransition == 1:
                GlobalTransition = 2
                MenuStatus = "main"
        else:
            screen.blit(self.img, (self.x, self.Yy))

# List to store all button instances
buttons = []

def mainMenuButtons():
    if buttons == []:
        Button(58, 100, r"images\icon_1.png", "Signals")
        Button(276, 100, r"images\icon_2.png", "Analysis")
        Button(58, 308, r"images\icon_3.png", "Coin List")
        Button(276, 308, r"images\icon_4.png", "Place Orders")

def tradeMenuButtons():
    if buttons == []:
        global GlobalTradeMenu
        GlobalTradeMenu = 1
        Button(58, 100, r"images\buy_btn.png", "Buy")
        Button(276, 100, r"images\sell_btn.png", "Sell")

# Create button instances
mainMenuButtons()
rButton = returnBtn()

# Update display
pygame.display.update()

#Title Text --
# Load font and set text color
TitleObj = TitleObj()
font = pygame.font.Font(r"Data\TitleFont.otf", 34)
text_color = (255, 255, 255)

# Run game loop

running = True
while running:
    print(GlobalTransition)
    rButton.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if MenuStatus == "main":
        PlaceOrderSetup = 0
        TitleChanged = 0
        for each in buttons:
            if each.mouseHover == 1:
                TitleText = each.title
                TitleChanged = 1
        if TitleChanged == 0:
            TitleText = "Main Menu"
            if TitleObj.rdy == 1:
                mainMenuButtons()
    else:
        if GlobalTransition == 0:
            TitleText = MenuStatus
            GlobalTransition = 1

        if TitleText == "Place Orders":
            pass

    # Render the text
    text = font.render(TitleText, True, text_color)

    # Get the rectangle representing the text
    text_rect = text.get_rect()

    # Center the text rectangle in the top middle of the window
    text_rect.centerx = screen.get_rect().centerx
    text_rect.top = 26+TitleObj.y

    # Blit the text to the screen
    screen.blit(text, text_rect)


    screen.blit(bg, (0, 0))

    TitleObj.update()
    rButton.Yy = rButton.y + TitleObj.y
    rButton.update()

    screen.blit(text, text_rect)
    for button in buttons:
        button.draw_button()

    pygame.display.update()

# Quit Pygame
pygame.quit()