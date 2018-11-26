#This module contains the combat functions that are passed during events where damage may occur to the player.

def attack(x,y):
    attack1 = x*((100+y)/100)
    print(attack1)
#Gross Damage Output = Base * ((100 + strength)/100)) || At 100 points of str, player should deal 2x their base damage every hit.
#Attack1 will feed into Attack2 calculations and so forth, factoring dodge, etc.