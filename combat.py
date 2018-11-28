#This module contains the combat functions that are passed during events where damage may occur to the player.
import random
#(basedamage, player.strength,player.dexterity, player.luck)
#assume base damage of 5, and str/dex/luck of 15 each (starter)


def playerattack(basedamage,playerstr,playerdex,playerluck):
    #crude damage
    attack1 = basedamage*((100+playerstr)/100)
    #output should be 6
    attack2 = round(attack1, 0)
    #critical hit below
    #==================
    #crude damage * (1+dex)
    attack3 = attack1*((25+playerdex)/25)
    #attack2 should be 10
    attack4 = round(attack3,0)
   
    #determine whether to use attack2 (rounded base damage) or attack4 (rounded crit damage)
    #this is done via random number generator influenced by luck
    
    #>=93.18 threshold vs >=.54.54
    #6.82% chance to crit at base vs 45.46% chance to crit at max luck

    #This code creates 2 things:
        #A critical threshold
        #A random number
    #If the random number exceeds the critical threshold, a critical hit lands.
    #This threshold is influenced by luck; higher luck lowers the threshold for a critical strike.
    #The luck factor is always between 0 and 100.

    crit_threshold = (100 - (playerluck/2.2))
   
    luckfactor = int(random.randrange(0,100,1))
    if luckfactor >= crit_threshold:
        output = int(attack4)
    else:
        output = int(attack2)
    return(output)
#Gross Damage Output = Base * ((100 + strength)/100)) || At 100 points of str, player should deal 2x their base damage every hit.
#Attack1 will feed into Attack2 calculations and so forth, factoring dodge, etc.