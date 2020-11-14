import pygame as py
#Screen Dimension Variables#
screen_w = 640
screen_l = 640
#Variables Storing RGB values for colours#
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 255)
blue = (0, 0, 255)
white = (255, 255, 255)
orange = (255, 100, 0)
yellow = (255, 255, 0)

score = 0
lives = 3

#Position for Weapon#
x = (screen_w * 0.45)
y = (screen_l * 0.8)

#pygame initilisation#
py.init()
#Setting Display Variable#
Mdisplay = py.display.set_mode((screen_w, screen_l))
#Sets a caption for the window#
py.display.set_caption('Atari Break-in')
# Sets IG time counter
clock = py.time.Clock()

#Loads the Images needed (Not my own)#

space = py.image.load('space.jpg')
gun = py.image.load('unnamed.png')

gunSCALED = py.transform.scale(gun, (100, 100))


def gun_sub(x, y):
    Mdisplay.blit(gunSCALED, (x, y))


#Checks to see if dead#
dead = False
while dead == False:
    for event in py.event.get():
        #Checks for keys pressed#
        if event.type == py.QUIT:
            dead = True
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT and x > 0:
                x -= 20
            if event.key == py.K_RIGHT and x < 560:
                x += 20
        #Outputs event type and time to shell#
        print(event)

    Mdisplay.blit(space, [0, 0])
    gun_sub(x, y)

    py.display.update()

    #Sets FPS counter to 60/second#
    clock.tick(60)

py.quit()
quit()
