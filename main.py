#Oliver (Ollie) Kim
#October 24, 2024

#CS172 HW04 pygame. bouncing ball! transformed into Breakout!
#win condition: breaking all the bricks
#lose condition: letting the ball hit the bottom of the display

import pygame
from ball import Ball
from paddle import Paddle 
from text import Text
from brick import Brick

#display!
pygame.init()
surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Breakout!")

#colors
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (195, 7, 7)
ORANGE = (255, 144, 27)
YELLOW = (255, 226, 61)
GREEN = (47, 167, 14)
BLUE = (10, 187, 184)
PURPLE = (138, 33, 226)

#drawables list!
drawablesList = []
unbrokenList = []

myBall = Ball(400, 400, 25, DARKBLUE)
myPaddle = Paddle(200, 25, DARKBLUE) 
myScoreBoard = Text("Score: 0", 10, 10) 
livesCount = Text("3: Lives", 690, 10)
victoryMessage = Text("", 300, 250)
loserMessage = Text("", 300, 250)

drawablesList.append(myBall)
drawablesList.append(myPaddle)
drawablesList.append(myScoreBoard)
drawablesList.append(livesCount)

#drawing and grouping bricks
for i in range(5):
    brick = Brick((100 + i*150), 60, 60, 20, RED)
    unbrokenList.append(brick)
for i in range(5):
    brick = Brick((100 + i*150), 110, 60, 20, ORANGE)
    unbrokenList.append(brick)
for i in range(5):
    brick = Brick((100 + i*150), 160, 60, 20, YELLOW)
    unbrokenList.append(brick)
for i in range(5):
    brick = Brick((100 + i*150), 210, 60, 20, GREEN)
    unbrokenList.append(brick)
for i in range(5):
    brick = Brick((100 + i*150), 260, 60, 20, BLUE)
    unbrokenList.append(brick)
for i in range(5):
    brick = Brick((100 + i*150), 310, 60, 20, PURPLE)
    unbrokenList.append(brick)
# brick = Brick(600, 200, 60, 20, RED)
# unbrokenList.append(brick)

fpsClock = pygame.time.Clock()

score = 0
lives = 3
running = True
levelComplete = False
while running:
    surface.fill((255, 255, 255))
    #if you lost a ball, respawning a new one
    if myBall not in drawablesList:
        myBall = Ball(400, 400, 25, DARKBLUE)
        drawablesList.append(myBall)

    for drawable in drawablesList:
        drawable.draw(surface)
    for brick in unbrokenList:
        brick.draw(surface)

    #ball location details
    ballLoc = myBall.getLoc()
    ballXLoc = ballLoc[0]
    ballYLoc = ballLoc[1]

    #quitting after victory screen
    if not unbrokenList and levelComplete:
        victoryMessage.setMessage("LEVEL COMPLETE")
        victoryMessage.draw(surface)
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False
    
    #death screen (if ball touches bottom edge of screen)
    if ballYLoc > 570:
        drawablesList.remove(myBall)
        lives -= 1
        score -= 10
        myScoreBoard.setMessage("Score: " + str(score))
        livesCount.setMessage(str(lives) + ": Lives")
        if lives == 0:
            loserMessage.setMessage("GAME OVER")
            loserMessage.draw(surface)
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False

    #ball and paddle bounce
    if myBall.intersects(myPaddle):
        myBall.setYSpeed(myBall.getYSpeed()*-1)

    # Brick and ball collision check
    if unbrokenList:  # if list isn't empty
        for brick in unbrokenList[:]:  # Make a copy of the list for safe iteration
            # brick location details
            brickLoc = brick.getLoc()
            brickXLoc = brickLoc[0]
            brickYLoc = brickLoc[1]

            # ball location details
            ballLoc = myBall.getLoc()
            ballXLoc = ballLoc[0]
            ballYLoc = ballLoc[1]

            # bouncing ball off brick, according to which side the collision was
            if ((abs(brick.leftSide() - myBall.rightSide()) < 5) or (abs(brick.rightSide() - myBall.leftSide()) < 5)) and (brick.bottomSide() < ballYLoc < brick.topSide()):
                myBall.setXSpeed(-1 * myBall.getXSpeed())
                unbrokenList.remove(brick)
                score += 1
                myScoreBoard.setMessage("Score: " + str(score))

            elif ((abs(brick.topSide() - myBall.bottomSide()) < 5) or (abs(brick.bottomSide() - myBall.topSide()) < 5)) and (brick.leftSide() < ballXLoc < brick.rightSide()):
                myBall.setYSpeed(-1 * myBall.getYSpeed())
                unbrokenList.remove(brick)
                score += 1
                myScoreBoard.setMessage("Score: " + str(score))
            
            if not unbrokenList: #huzzah!
                levelComplete = True

    myBall.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    fpsClock.tick(60)
exit() 