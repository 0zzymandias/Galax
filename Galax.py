import math
import time
import sys
import cmd
import textwrap
import random
import combat

#World-time; actions have consequences. Game daysself.
#If you destroy a manufacturing machine for AI brain chips, you fight less and less enemies over time.
#However, prices for those chips will also skyrocket in the economy over time as the world becomes barren.

#Economics
credits = 0
#Time. Every action and movement represents 1 hour of game time. Things like sleeping could advance things forward.
elapsedhours=0
name=""
#Permanent Stats
#Replenishables
#Perks
#Things like dodge and damange resistance, damage bypass, keycard level, etc.

#Dodge. Applied every time a hit is attempted.
dodge=0.05
#Damage resistance. Applied every time an attempted hit connects.
resistance=0.00
#Damage penetration. Applied every time your strike connects with the enemy; .95 piercingdamage implies that 95% of damage you deal ignores armor. 0% implies that no damage ignores armor.
piercingdamage=0.00
#Authentication level. Higher integers will bypass locks entirely.
#Base lockpick skill. Influenced by Dexterity. A high enough lockpick skill will allow you to bypass locks without a keycard.

#Malice
malice = 0
#When this gets higher, bad things happen to the player.

#This will be called in times of combat. This will also be called in times where stat calculation is involved (i.e. picking a lock)

#WORLD LOCATIONS

#|--------------#
#|##############|
#|##############|
#|##,,,,,,,,,,##|
#|######,#######|
#|######,#######|
#|######,#######|
#-------M-------#

#M = main gate
#, = streetway

#Development question to self: procedural generation, or actual world map?

Rooms = {
    '`City Gate Cordon`': {
        'DESC':'The entryway to the city, and by association, exit to the wastes. The guarded gate you entered from looms behind you.',
        'North': 'Residential District',
        'East': 'Commercial District',
        'West': 'Industrial District',
        'South': 'Sealed Gate'
    },  
    'Residential District': {
        'DESC':'The entryway to the city, and by association, exit to the wastes. The guarded gate you entered from looms behind you.',
        'North': 'Inner Residential District',
        'East': 'Solid Wall',
        'West': 'Solid Wall',
        'South': 'City Gate Cordon'
    },
        'Residential District 2': {
        'DESC':'The entryway to the city, and by association, exit to the wastes. The guarded gate you entered from looms behind you.',
        'North': '',
        'East': 'Solid Wall',
        'West': 'Solid Wall',
        'South': 'City Gate Cordon'
    }
}

DESC = 'desc'
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
UP = 'up'
DOWN = 'down'
GROUND = 'ground'
SHOP = 'shop'
GROUNDDESC = 'grounddesc'
SHORTDESC = 'shortdesc'
LONGDESC = 'longdesc'
TAKEABLE = 'takeable'
EDIBLE = 'edible'
DESCWORDS = 'descwords'
SCREEN_WIDTH=80

inventory = ['README Note', ''] # start with blank inventory


#ITEMS



#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#
#FUNCTIONS TO BOOST STATS == CALL IN EVENTS ==========================
#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#

class player(object):
    """docstring for player."""
    def __init__(self, health, stamina, strength, dexterity, intelligence, charisma, agility, luck, dodge, resistance, base_damage, damage_bypass, location):
        super(player, self).__init__()
        self.health = health
        self.stamina = stamina
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.charisma = charisma
        self.agility = agility
        self.luck = luck
        self.dodge = dodge
        self.resistance = resistance
        self.base_damage = base_damage
        self.damage_bypass = damage_bypass
        self.location = location


player.health=100
player.stamina=100
player.strength=15
player.dexterity=15
player.intelligence=15
player.charisma=15
player.agility=15
player.luck=15
player.dodge=0.05
player.resistance=0.00
player.base_damage=5
player.damage_bypass=0.00


print(combat.attack(player.base_damage,player.strength))
#Gross Damage Output = Base * ((100 + strength)/100)) || At 100 points of str, player should deal 2x their base damage every hit.

#
#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#
#Decision by me -- instead of having the player set stats at the beginning (a la Fallout), I'll have them grow per their own decisions.

#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#
#INTRODUCTION===========================================================
#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#

print("Hello!")


print(random.choice(list(Rooms)))
list(Rooms)
print(list(Rooms))
time.sleep(1)

def adder(x,y,z):
    result=x*(y*z)-100
    print(result)

adder(100,2,3)

print("Welcome to Galax Umbria - the world's longest-lasting fully-automated utopia.")

time.sleep(3)

print("Please state your name.")

time.sleep(1)

#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#
#Enter player name.
#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#
print("")
print("--[Enter your name.]--")

name = input()

print("")
print("Welcome, "+name+".")
time.sleep(1.5)

print("Please hold on for a moment.")
#NAME-BASED CHEATS ARE APPLIED HERE
if name=="Ozymandias":
    time.sleep(1)
    print("")
    print("Welcome, sir. Please enjoy your stay.")
    print("Luck: 777")
    player.luck=777

time.sleep(3)

#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#
#STATS EXPLANATION TIME ------------------------
#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#
print("")
print("--[The world of Galax Umbria uses certain stats to measure your capabilities.]--")

time.sleep(2.5)

print("--[The following stats have a natural limit of 100, though certain augmentations can override this limit.]--")
time.sleep(0.5)
print("")
time.sleep(4)

print("")
print("--[Strength represents your physical strength, and your ability to exert brute force.]--")
print("--[At high-enough levels, you will be able to lift, break, and endure more than normal humans.]--")
print("--[Level 100 Special Perk: Enforcer]--")
print("")

time.sleep(7)

print("")
print("--[Dexterity represents your physical finesse, and your ability to interact with intricate mechanisms.]--")
print("--[At high-enough levels, you will be able to better manipulate complex devices, and score critical hits more often.]--")
print("--[Level 100 Special Perk: Critical Eye]--")
print("")

time.sleep(7)

print("")
print("--[Intelligence represents your intellectual prowess, and your ability to calculate outcomes and strategies.]--")
print("--[At high-enough levels, you will be able to quicker derive context from the world, and formulate more effective approaches to situations.]--")
print("--[Level 100 Special Perk: Ubergestalt]--")
print("")

time.sleep(7)

print("")
print("--[Charisma represents your persuasive capability, and your ability to leverage social interactions to your liking.]--")
print("--[At high-enough levels, you will be able to interrogate more effectively, and persuade those who are otherwise unpersuadable.]--")
print("--[Level 100 Special Perk: Messianic Voice]--")
print("")

time.sleep(7)

print("")
print("--[Agility represents your physical reaction time, and your ability to respond to external hostilities.]--")
print("--[At high-enough levels, you will have a higher chance to dodge incoming damage.]--")
print("--[Level 100 Special Perk: Shadow Walk]--")
print("")

time.sleep(7)
print("")
print("--[Luck represents your additional propensity to succeed at something, just because it's you.]--")
print("--[At high enough levels, negative outcomes have potential to be mitigated whilst positive outcomes have potential to be boosted.]--")
print("--[Level 100 Special Perk: Entropic Anomaly]--")
print("")

time.sleep(6)

print("--[Your actions will determine your stat growth.]--")
time.sleep(2)
print("")

agibig()
agibig()
agibig()

luckbig()
strengthbig()
time.sleep(1)
print(str(name))
time.sleep(1)
print("Current Stats:")
print(str(player.strength)+" Strength")
print(str(player.dexterity)+" Dexterity")
print(str(player.intelligence)+" Intelligence")
print(str(player.charisma)+" Charisma")
print(str(player.agility)+" Agility")
print(str(player.luck)+" Luck")

print("")
print("--[Press ENTER to continue to the next section.]--")
input()

#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#
#WORKING FUNCTIONS
#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#
#These were in an earlier build of Galax -- where you set your stats. See comment below. 
#UNUSED
def definestrength():
    player.strength=15+int(input())
def definedexterity():
    player.dexterity=15+int(input())
def defineintelligence():
    player.intelligence=15+int(input())
def definecharisma():
    player.charisma=15+int(input())
def defineagility():
    player.agility=15+int(input())
def defineluck():
    player.luck=15+int(input())
#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#
def strengthsmall():
    player.strength+=1
def strengthbig():
    player.strength+=5

def dexsmall():
    player.dexterity+=1
def dexbig():
    player.dexterity+=5

def intsmall():
    player.intelligence+=1
def intbig():
    player.intelligence+=5

def chrsmall():
    player.charisma+=1
def chrbig():
    player.charisma+=5

def agismall():
    player.agility+=1
def agibig():
    player.agility+=5

def lucksmall():
    player.luck+=1
def luckbig():
    player.luck+=5


#strengthallocate = input()
#print("Please state your aptitudes.")
#/////////////////////////////////////////////////////////////////////////////////////////////
#BEGIN NAV TUTORIAL=========================================================
print("Your visor contains local navigation information; to summarize where you are, say 'Nav'.")
time.sleep(2)
print("--[Tutorial: Say 'Nav'. Case does not matter.]--")
choice = input()
choice = choice.lower()
#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#
#This nav tutorial will loop until you get it right, damn it.
#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#
while (choice != "nav"):
    print("--[Tutorial: Say 'Nav'. Case does not matter.]--")
    choice = input()
    choice = choice.lower()
if choice == "nav":
    print("--[Completed Mission: Nav Tutorial]--")
time.sleep(2)
print("Our state-of-the-art navigation suite will help you navigate society easier.")
time.sleep(3)
print("Call it up at any time by saying 'Nav'.")
time.sleep(3)
#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#
#First credit sequence; being released into the world.
#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#=+=#

print("Your documents check out. All new citizens are given credits in our society.")
time.sleep(3)
print("These may be spent at your leisure for additional services beyond that which is provided to every citizen.")
time.sleep(4)
print("------")
print("[+500 Credits]")
print("------")
credits +=500
print("You may earn additional credits by assisting the projects of others.")
time.sleep(3)
print("--[The gate opens to you. You step inside.]--")
input()
