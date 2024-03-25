#First attempt at a rpg python game
#With help from youtube videos, and internet for snippets of code/to get stuff running
#Skyler Coombs

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

##Player setup##
class player:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.mana = 0
        self.statusEffects = []
        self.location = "start"
        self.inv = []
myPlayer = player()

##TITLE##
def titleScreenSelect():
    op = input("> ")
    if op.lower() == ("play"):
        startGame() #not done yet
    elif op.lower() == (""):
        helpMenu() #not done yet
    elif op.lower() == ("quit"):
        sys.exit()
    while op.lower() not in ['play','help','quit']:
        print("Please enter a valid command.")
        op = input("> ")
        if op.lower() == ("play"):
            startGame()  # not done yet
        elif op.lower() == (""):
            helpMenu()  # not done yet
        elif op.lower() == ("quit"):
            sys.exit()
def titleScreen():
    os.system('clear')
    print("##############################")
    print("#Welcome to Skyler's text RPG#")
    print("##############################")
    print("#          ~~~Play~~~        #")
    print("#          ~~~Help~~~        #")
    print("#          ~~~Quit~~~        #")
    print("##COPYRIGHT2023SKYLER_COOMBS##")
    titleScreenSelect()

    ###HELPMENU###
def helpMenu():
    print("#########################################")
    print("######Welcome to Skyler's text RPG#######")
    print("#########################################")
    print("# ~~Use up, down, left, right to move~~ #")
    print("#   ~~Type your commands to do them~~   #")
    print("#  ~~Use 'look' to inspect something~~  #")
    print("#      ~~Best of luck, traveler!~~      #")

    #Game Funciton#
def startGame():
ZONENAME = ""
DESCRIPTION = 'description'
EXAMINE = 'examine'
SOLVED = "False"
UP = "up" , "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"

solvedPlaces = {'a1':False,'a2':False,'a3':False,'a4':False,
                'b1': False, 'b2': False, 'b3': False, 'b4': False,
                'c1': False, 'c2': False, 'c3': False, 'c4': False,
                'd1': False, 'd2': False, 'd3': False, 'd4': False,
                'e1': False, 'e2': False, 'e3': False, 'e4': False,
                'f1': False, 'f2': False, 'f3': False, 'f4': False,
                'g1': False, 'g2': False, 'g3': False, 'g4': False,
                }
zoneMap = {
    'a1':{                              #FILL THIS OUT AND REPEAT FOR ALL ZONES
        ZONENAME :"",
        DESCRIPTION : 'This is the church',
        EXAMINE : 'You stand on the cobblestone street, facing the front enterance of the grand church. The church, if you could call it that, is a large',
        SOLVED : False,
        UP : "nothing go back",
        DOWN : "a2",
        LEFT : "left", "west",
        RIGHT: "b1",
        },
    'a2':{
        ZONENAME: "",
        DESCRIPTION : "description",
        EXAMINE : "examine",
        SOLVED : False,
        UP : "a1,
        DOWN : "a3",
        LEFT : "left", "west",
        RIGHT : "b2",
        },
    'a3':{
        ZONENAME: "",
        DESCRIPTION : "description",
        EXAMINE : "examine",
        SOLVED : False,
        UP : "a2,
        DOWN : "a4",
        LEFT : "left", "west",
        RIGHT : "b3",
        }
    'a4':{
        ZONENAME: "",
        DESCRIPTION : "description",
        EXAMINE : "examine",
        SOLVED : False,
        UP : "a3",
        DOWN : "NOTHING GO BACK",
        LEFT : "left", "west",
        RIGHT : "b4",
        }
    'b1':{
        ZONENAME: "",
        DESCRIPTION : "description",
        EXAMINE : "examine",
        SOLVED : False,
        UP : "nothing go back",
        DOWN : "b2",
        LEFT : "a1",
        RIGHT : "c1",
        }
    'b2': {
        ZONENAME: "",
        DESCRIPTION : "description",
        EXAMINE : "examine",
        SOLVED : False,
        UP : "b1",
        DOWN : "b3",
        LEFT : "a2",
        RIGHT : "c2",
        },
    'b3': {
        ZONENAME: "",
        DESCRIPTION : "description",
        EXAMINE : "examine",
        SOLVED : False,
        UP : "b2",
        DOWN : "b4",
        LEFT : "a3",
        RIGHT : "c3",
        },
    'b4': {
        ZONENAME: "",
        DESCRIPTION : "description",
        EXAMINE : "examine",
        SOLVED : False,
        UP : "b3",
        DOWN : "NOTHING GO BACK",
        LEFT : "a4",
        RIGHT : "c4",
        },
}
