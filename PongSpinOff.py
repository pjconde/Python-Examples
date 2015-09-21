#Pablojose Conde 903016892
#pjcodne@gatech.edu

from Graphics import *
from Myro import askQuestion, timer
import time
import os

win = Window("Don't Let it Out", 620, 450)
win.setBackground(makeColor(255,255,255))
win.mode = "physics"

win.gravity = Vector(0,0)

# Setting the boundaries for game ---------------------------------------------------------------------------

top_boundary = Rectangle((0, 0), (620, 50))
top_boundary.bodyType = "static"
top_boundary.setFill(makeColor(0,0,0))
top_boundary.draw(win)

bottom_boundary = Rectangle((0, 430), (620, 470))
bottom_boundary.bodyType = "static"
bottom_boundary.setFill(makeColor(0,0,0))
bottom_boundary.draw(win)

# -----------------------------------------------------------------------------------------------------------

# Beginning Settings for Game -------------------------------------------------------------------------------

def askNames():
    name_input = askQuestion("Which name would you like to enter?", ["Player 1", "Player 2","Let's Starts!"])
    if name_input == "Player 1":
        player1_name = input("What is Player 1's name?")
        player1Name = Text((50, 25), player1_name)
        player1Name.setFill(makeColor(255,255,255))
        player1Name.fontSize = 30
        player1Name.bodyType = "static"
        player1Name.undraw()
        player1Name.draw(win)
        askNames()
    elif name_input == "Player 2":
        player2_name = input("What is Player 2's name?")
        player2Name = Text((570, 25), player2_name)
        player2Name.setFill(makeColor(255,255,255))
        player2Name.fontSize = 30
        player2Name.bodyType = "static"
        player2Name.undraw()
        player2Name.draw(win)
        askNames()
    elif name_input == "Let's Start!":
        return
askNames()

# -----------------------------------------------------------------------------------------------------------

# Gets the Highscore from the highscores text file ----------------------------------------------------------

def getHighScore():
    highscoresList = open("highscores.txt", "a+")
    highscoresList.seek(0)
    numLines = len(highscoresList.readlines())      # Gets the number of lines in the file
    highscoresList.seek(0)                          # Returns to the top of the file to read
    if numLines == 0:                               # If the file is empty (no lines) it adds a 0
        highscoresList.write("0\n")
    highscoresList.seek(0)                          # Returns to the top of the file to read
    scoresList = highscoresList.readlines()         # Reads the lines in the file and stores them as a list
    scoresList = map(int, scoresList)               # Converts list from file into integers
    highscore = max(scoresList)                     # Gets the highest score in the current list of scores
    highscore = int(highscore)
    highscoresList.close()
    print("The current highscore to beat: {}".format(highscore))    # Prints the current highscore
getHighScore()

# -----------------------------------------------------------------------------------------------------------

# Drawing the two players (rectangles) ----------------------------------------------------------------------

player_one = Rectangle((20, 70), (40, 170)) # Left rectangle is player 1
player_one.bodyType = "static"
player_one.setFill(makeColor(0,0,128)) # Player 1 is the blue colored rectangle
player_one.draw(win)

player_two = Rectangle((580, 70), (600, 170)) # Right rectangle is player 2
player_two.bodyType = "static"
player_two.setFill(makeColor(178,34,34)) # Player 2 is the red colored rectangle
player_two.draw(win)

# -----------------------------------------------------------------------------------------------------------

# Some Global variables needed ------------------------------------------------------------------------------

x, y = 500, 120
ball = Circle((x, y), 10)
ball.setFill(makeColor(255,140,0))
ball.bounce = 1.02

yourscore = 0

# -----------------------------------------------------------------------------------------------------------

start = Text((310, 225), "Click on the window to see who is the best!")
start.setFill(makeColor(0,0,0))
start.draw(win)

def handleMouseClick(win, event):
    global ball
    ball.bounce = 1.02
    start.undraw()
    ball.draw(win)
    ball.body.ApplyForce( Vector(-75, 75))

onMouseDown(handleMouseClick)



# Makes the controlls for the two players and loops the score ------------------------------------------------

def controls():
    global ball
    global yourscore
    keep_going = True
    start = time.time()
    while keep_going:
        if ball.getX() < 0:
            ball = Circle((500, 120), 10)
            ball.setFill(makeColor(255,140,0))
            end = time.time()
            keep_going = False
            elapsed = int(end - start)
            yourscore = elapsed * (100)
            print("Your score is {} !".format(yourscore))

            # File I/O to read, write, and update high score for the game ----------------------------------------------

            highscores = open("highscores.txt", "a+")
            highscores.write(str(yourscore)+"\n")         # Adds the users' score into the file
            highscores.seek(0)                            # Returns to the top of the file
            scoresList = highscores.readlines()           # Reads file line by line and adds it to a list
            scoresList = map(int, scoresList)             # Converts the list from the file into integers
            highscore = max(scoresList)                   # Gets the highest score in the current list of scores
            highscore = int(highscore)
            highscores.close()
            print("The current highscore: {}".format(highscore))    # Prints the current high score

            # -------------------------------------------------------------------------------------------------

        if ball.getX() > 620:
            ball = Circle((500, 120), 10)
            ball.setFill(makeColor(255,140,0))
            end = time.time()
            keep_going = False
            elapsed = end - start
            yourscore = int(elapsed * (100))
            print("Your score was {} !".format(yourscore))

            # File I/O to read, write, and update high score for the game ----------------------------------------------

            highscores = open("highscores.txt", "a+")
            highscores.write(str(yourscore)+"\n")         # Adds the users' score into the file
            highscores.seek(0)                            # Returns to the top of the file
            scoresList = highscores.readlines()           # Reads file line by line and adds it to a list
            scoresList = map(int, scoresList)             # Converts the list from the file into integers
            highscore = max(scoresList)                   # Gets the highest score in the current list of scores
            highscore = int(highscore)
            highscores.close()
            print("The current highscore: {}".format(highscore))    # Prints the current high score

            # -------------------------------------------------------------------------------------------------

        if getKeyPressed():
            key = getLastKey()
            if key == "w":
                player_one.move(0, -5)
            elif key == "s":
                player_one.move(0, 5)
            if key == "o":
                player_two.move(0, -5)
            elif key == "l":
                player_two.move(0, 5)
            if key == "b":
                ball.undraw()
                ball = Circle((500, 120), 10)
                ball.setFill(makeColor(255,140,0))


        win.step(.01)
# ------------------------------------------------------------------------------------------------------------
win.run(controls)
