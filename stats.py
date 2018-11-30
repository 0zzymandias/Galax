#This is the module that influences stats.

def statadd_small(stat):
    return stat + 1
def statadd_medium(stat):
    return stat + 5
def statadd_big(stat):
    return stat + 10
def statadd_debug(stat):
    return stat + 100

#These functions do not appear functional for the time -- they work when directly inserted into Galax.py, but not when called with stats.statadd..etc.