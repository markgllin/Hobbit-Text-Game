#T06.
#This game is a simulation of the book "The Hobbit". It simulates the scene where Bilbo enters the cave of Smaug and tries to steal as much gold as he can.
#This program can handle non-numerical values.
#There are various game modes implemented, each triggered when the player reaches a certain stage of the game.
#This program can record and write highscores of the the player.

import sys
import random

HIGHSCORE="scores.txt"
MAX_ROWS = 30
MAX_COLUMNS = 29
health=20
PLAYER="H"
EMPTY=" "
WALL="#"
GOLD="t"
DRAGFIRE="*"
points=0
endProgram=False
invuln=False
debug=False
finGame=False
complete=False
healthB4=20
pointsB4=0
mode2=False
mode3=False
tunEnRow=13
tunEnCol=14
farTunEnRow=0
play=True

#introduction to the game
def intro():
   print()
   print("\tYou are a hobbit by the name of Bilbo Baggins when one day, a group of dwarves arrive at your front door. The group of dwarves speak of a cave filled with gold that is free to be claimed for any who desires it. The only catch? It is guarded by a dragon named Smaug. The dwarves, aware that hobbits are known to be agile and silent in movement, pushes you to join them in their perilous quest")
   print()
   cont=raw_input("Press enter to continue")
   print()
   print("\tAfter many nights of travel, you and your group of dwarves arrive at the entrance of a tunnel that leads to the cave-filled gold. Your goal is to enter the cave and collect as much gold as you can, avoiding the obstacles and dangers that lie between you and fame.")
   print()
   cont=raw_input("Press 'enter' to continue")
   print()
   print("H= Player, '#'= Walls, 't'= Gold, '*'= Fire")
   print()
   cont=raw_input("Press 'enter' to begin your quest.")
   print()

#this function adds the feature of dragon fire into the main hall(mode2), whereupon stepping on it, player loses health
def dragonfireM1(erebor):
   MAX_ROW=28
   MAX_COL=28
   row=13
   while (row<MAX_ROW):
      col=1
      row=row+1
      while(col<MAX_COL):
         if (erebor[row][col]==DRAGFIRE):
            erebor[row][col]=EMPTY
         chance=random.randrange(0,101)
         if (erebor[row][col]==EMPTY) or (erebor[row][col]==GOLD) or (erebor[row][col]==WALL):
            if (chance<11) and (chance>=0):
               erebor[row][col]=DRAGFIRE
         elif (erebor[row][col]==PLAYER):
            if(chance<11) and (chance>=0):
               hitpoint()
         col=col+1

#this function adds the feature of dragon fire into the tunnel (mode3), whereupon stepping on it, player loses health
def dragonfireM2(erebor):
   global tunEnRow
   global tunEnCol
   global farTunEnRow
   MAX_ROW=28
   MAX_COL=28
   row=13
   while(row<MAX_ROW):
      col=1
      row=row+1
      while (col<MAX_COL):
         if (erebor[row][col]==DRAGFIRE):
            erebor[row][col]=EMPTY
         col=col+1
   if(erebor[13][14]==PLAYER):
      erebor[13][14]=PLAYER
   else:
      erebor[13][14]=DRAGFIRE
   chance=random.randrange(0,101)
   if (chance>=0) and (chance<25):
      tunEnRow=tunEnRow-1
      if (erebor[tunEnRow][tunEnCol]==PLAYER):
         erebor[tunEnRow][tunEnCol]=PLAYER
      else:
         erebor[tunEnRow][tunEnCol]=DRAGFIRE
   if (chance>=25) and (chance<50):
      tunEnRow=tunEnRow-1
      if (erebor[tunEnRow][tunEnCol]==PLAYER):
         erebor[tunEnRow][tunEnCol]=PLAYER
      else:
         erebor[tunEnRow][tunEnCol]=DRAGFIRE
      tunEnRow=tunEnRow-1
      if (erebor[tunEnRow][tunEnCol]==PLAYER):
         erebor[tunEnRow][tunEnCol]==PLAYER
      else:
         erebor[tunEnRow][tunEnCol]=DRAGFIRE
   if (chance>=50) and (chance<=100):
      if(erebor[tunEnRow][tunEnCol]==PLAYER):
         erebor[tunEnRow][tunEnCol]=PLAYER
      else:
         erebor[tunEnRow][tunEnCol]=DRAGFIRE
   farTunEnRow=tunEnRow
   while(farTunEnRow<=13):
      if (erebor[farTunEnRow][tunEnCol]==PLAYER):
         hitpoint()
         erebor[farTunEnRow][tunEnCol]=PLAYER
      else:
         erebor[farTunEnRow][tunEnCol]=DRAGFIRE
      farTunEnRow=farTunEnRow+1

#PLAYER health. If the player is hit by fire, Bilbo takes 4 damage to his health.
def hitpoint():
   global health
   global healthB4
   DMG=4
   healthB4=health
   if (invuln==False):
      health=health-DMG
      print("You've been hit by fire!")
   if (invuln==True):
      print("Youve been hit by fire but you're currently invulnerable (h@cks)")
      health=health

# The display() method was written entirely by James Tam
def  display (erebor):
   coordinates=[" "," "," ","0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S"]
   print()
   for r in range (0, MAX_ROWS+2, 1):
      sys.stdout.write(coordinates[r])
   print()
   print("----------------------------------")
   for r in range (0, MAX_ROWS, 1):
      sys.stdout.write("%2d|" % r)
      for c in range (0, MAX_COLUMNS, 1):
         sys.stdout.write(erebor[r][c])
      print()

#This function creates a list that countains the map of Erebor.
def initialize():
   erebor = []
   for r in range (0, MAX_ROWS, 1):
      erebor.append([])

   #              1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29 
   #              0   1   2   3   4   5   6   7   8   9   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S
   erebor[0] =  ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","H","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
   erebor[1] =  ["#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
   erebor[2] =  ["#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
   erebor[3] =  ["#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
   erebor[4] =  ["#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
   erebor[5] =  ["#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
   erebor[6] =  ["#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
   erebor[7] =  ["#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
   erebor[8] =  ["#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
   erebor[9] =  ["#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
   erebor[10] = ["#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
   erebor[11] = ["#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
   erebor[12] = ["#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
   erebor[13] = ["#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
   erebor[14] = ["#"," "," "," "," "," "," "," "," "," "," ","t"," "," "," "," "," "," ","#"," "," "," "," "," "," "," "," "," ","#"]
   erebor[15] = ["#"," "," "," "," "," ","#","#"," "," "," "," "," "," ","#"," "," "," "," ","#"," "," ","#","#"," "," "," "," ","#"]
   erebor[16] = ["#"," "," "," "," "," ","#","#"," "," "," "," "," "," ","t"," "," "," "," ","#"," "," ","#","#"," "," "," "," ","#"]
   erebor[17] = ["#","t"," "," ","t"," "," "," "," "," "," "," "," "," ","#"," "," "," "," ","#"," "," ","t"," "," "," "," "," ","#"]
   erebor[18] = ["#","#","#","#","#","#","#","#"," "," "," "," "," "," "," "," ","t"," "," "," "," ","#","#"," "," "," "," "," ","#"]
   erebor[19] = ["#","#"," "," "," "," ","#","#"," "," "," "," "," "," ","#"," "," "," "," "," "," ","#","#"," "," "," "," "," ","#"]
   erebor[20] = ["#"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","t"," "," "," "," ","#"]
   erebor[21] = ["#"," "," "," "," "," ","#","#"," "," "," "," "," "," ","#"," "," "," "," "," "," ","#","#"," "," "," "," "," ","#"]
   erebor[22] = ["#"," "," "," "," "," ","#","#"," "," "," ","t"," "," ","#"," "," "," "," "," "," ","#","#"," ","#","#","#","#","#"]
   erebor[23] = ["#"," "," ","t"," "," "," "," "," "," "," "," "," "," ","#"," "," "," "," "," "," ","#"," ","t"," "," "," "," ","#"]
   erebor[24] = ["#"," "," "," "," "," ","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"," ","#"]
   erebor[25] = ["#"," "," "," "," "," ","#","#"," "," "," "," "," "," ","#"," "," "," "," "," "," ","#","#"," "," "," ","t"," ","#"]
   erebor[26] = ["#"," "," "," "," "," "," "," "," ","t"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","#"]
   erebor[27] = ["#"," ","t"," "," "," ","#","#"," "," "," "," "," "," ","#"," "," "," "," "," "," ","#","#"," ","#","#","#","#","#"]
   erebor[28] = ["#"," "," "," "," "," ","#","#","t"," "," "," "," "," "," ","t"," "," "," "," "," ","#","#","t","t","t","t","t","#"]
   erebor[29] = ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]
   return(erebor)

#This function ends the game after the player returns to the entrance of the tunnel
def finishGame(place):
   global complete
   if (place[1][14]==PLAYER):
      complete=True
   if (place[0][14]==PLAYER) and (complete==True):
      return True
   return False

#this function governs the movements of the player
def move(cRow,cCol,turn,place):
   global endProgram
   dRow=cRow
   dCol=cCol
   TRIGGER=0
#pass on turn
   if(turn==5):
      dRow=cRow
      dCol=cCol
#move west
   if(turn==4):
      dCol=cCol-1
#move east
   if(turn==6):
      dCol=cCol+1
#move south
   if(turn==2):
      dRow=cRow+1
#move north
   if(turn==8):
      dRow=cRow-1
#move southwest
   if(turn==1):
      dRow=cRow+1
      dCol=cCol-1
#move southeast
   if(turn==3):
      dRow=cRow+1
      dCol=cCol+1
#move northwest
   if(turn==7):
      dRow=cRow-1
      dCol=cCol-1
#move northeast
   if(turn==9):
      dRow=cRow-1
      dCol=cCol+1
#close program if input=0
   if(turn==0):
      endProgram=True
      return(cRow,cCol)
#prevents player from moving onto wall
   if (place[dRow][dCol]==WALL):
      if(debug==True):
         print("A wall is in your way")
      place[cRow][cCol]=PLAYER
      return(cRow,cCol)
#picks up gold if player steps on it
   elif (place[dRow][dCol]==GOLD):
      tGold=True
      gold(tGold)
      place[cRow][cCol]=EMPTY
      place[dRow][dCol]=PLAYER
      return (dRow,dCol)
   else:
      tGold=False
      gold(tGold)
      place[cRow][cCol]=EMPTY
      place[dRow][dCol]=PLAYER
      return(dRow,dCol)

#awards player points if they pick up gold
def gold(tGold):
   global points
   global pointsB4
   points=int(points)
   pointsB4=int(pointsB4)
   if (tGold==True):
      pointsB4=points
      points=points+3
   else:
      pointsB4=points

#Menu options. Negative values lead to another function that brings up a cheat menu. '0' closes the game. Values between 1 and 9 returns the input value to the movement function.
def menu():
   global invuln
   TRIGGER=0
   print("Movement options:")
   print("-----------------")
   print("7 8 9")
   print("4 5 6")
   print("1 2 3")
   print("Enter 5 to pass on movement")
   print("Enter '0' to quit the game")
   ok=False
   movement=0
   while (ok==False):
      try:
         movement=int(input("Enter your selection (a value between 1 and 9):"))
         print("---------------------------------------------------------")
      except:
         ok=False
         print("Please enter an appropriate number within the range")
      else:
         if(movement<10) and (movement>=0):
            return(movement)
         elif(movement<TRIGGER):
            ok=False
            cheatmenu()
         elif (movement>9):
            ok=False

#if player enters any negative value, a cheat menu opens up where they can toggle debugging and invulnerability 'on' or 'off'
def cheatmenu():
   global debug
   global invuln
   invuln=False
   debug=False
   debugMode=input("Would you like to turn on (d)ebugging?:")
   if (debugMode=='d') or (debugMode=='D'):
      debug=True
   invulnerability=input("Would you like to turn on (i)nvulnerability?:")
   if (invulnerability=='i') or (invulnerability=='I'):
      invuln=True

#if player achieves the highscore, this function will write his highscore to a file
def writeHighscore(priorHighscore, scoresList):
   global points
   global health
   try:
      inputFile=open(HIGHSCORE, "w")
   except IOError:
      print("Unable to write to %s" %(HIGHSCORE))
   else:
      priorHighscore=int(priorHighscore)
      if (health!=0) and (priorHighscore<=points):
         name=str(input("Enter your name for highscore:"))
         points=str(points)
         health=str(health)
         name=name+":"+" "+points+" "+health
         inputFile.write(name)
      else:
         name=scoresList[0][0]
         points=scoresList[0][1]
         health=scoresList[0][2]
         name=name+" "+points+" "+health
         inputFile.write(name)
         print("You are not eligible for the highscore")
   inputFile.close()

#once player finishes the game,a highscore file will be opened and the highscore will be recorded
def readHighscore():
   global points
   highscores=[]
   try:
      inputFile=open(HIGHSCORE, "r")
   except IOError:
      print("Unable to open file %s" %(HIGHSCORE))
   else:
      highscore=0
      for line in inputFile:
         aPlayer=[]
         name, highscore, health= line.split()
         aPlayer.append(name)
         aPlayer.append(highscore)
         aPlayer.append(health)
         highscores.append(aPlayer)
      inputFile.close()
      return (highscore,highscores)

#this function displays the highscore
def pPoints(highscores):
   last=len(highscores)
   print()
   print ("HIGHSCORE")
   print("-----------")
   for r in range (0,last,1):
      for c in range (0,2,1):
         print("%s"  %(highscores[r][c]))
   print()

#debugging messages for displaying health, gold, invulnerability, etc.
def messages(end):
   if (invuln==True):
      invulnMsg="On"
   else:
      invulnMsg="Off"
   if (debug==True):
      print("Health before turn:", healthB4, "Health after turn:", health, "Gold before turn:", pointsB4, "Gold after turn:", points, "Invulnerability: %s" %(invulnMsg))
   else:
      print("Health:", health, "Gold:", points, "Invulnerability: %s" %(invulnMsg))
   if (end==True):
      print("You have escaped Smaug! You collected %d gold." %(points))
   if (debug==False) and (health==0):
      print("You have been slain and lost. You collected %d gold." %(points))
   elif (debug==True) and (health==0):
      print("You have been slain, lost, and are no longer eligible for the highscore. You collected %d gold." %(points))

#once player moves past a certain point, this function will enable the next stage once the player returns to the tunnel
def nextStage(place):
   global mode2
   global mode3
   if (place[14][14]==PLAYER):
      mode2=True
   if (place[12][14]==PLAYER) and (mode2==True):
      mode3=True

#once the game is completed once, this function asks the user if they would like to play again.
def playAgain():
   global play
   global invuln
   global debug
   global finGame
   global complete
   global healthB4
   global health
   global points
   global healthB4
   global pointsB4
   global mode2
   global mode3
   global tunEnRow
   global tunEnCol
   global farTunEnRow
   global endProgram
#Yes, I know; deserve nothing less than hell for all these globals.
   again=input("Would you like to (p)lay again?:")
   if (again=="p") or (again=="P"):
      play=True
      invuln=False
      debug=False
      finGame=False
      complete=False
      health=20
      points=0
      healthB4=20
      pointsB4=0
      mode2=False
      mode3=False
      tunEnRow=13
      tunEnCol=14
      farTunEnRow=0
   else:
      play=False

#this function calls all other functions and continues the game until the player dies
def main ():
   while (play==True):
      intro()
      erebor = initialize()
      display(erebor)
      row=0
      column=14
      end=False
      while(health!=0) and (endProgram==False) and (end==False):
         shift=menu()
         row,column=move(row,column,shift,erebor)
         end=finishGame(erebor)
         if (row>=14):
            if (debug==True):
               print("Smaug is now breathing fire into the main hall")
            dragonfireM1(erebor)
         nextStage(erebor)
         if(mode3==True):
            if (debug==True):
               print("Smaug is now moving towards the tunnel")
            dragonfireM2(erebor)
         messages(end)
         display(erebor)
      oneScore, scoresList=readHighscore()
      writeHighscore(oneScore, scoresList)
      oneScore, scoresList=readHighscore()
      pPoints(scoresList)
      playAgain()

main()

