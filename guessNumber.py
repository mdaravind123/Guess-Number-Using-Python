#guess the number
import random as r   #random module
import time as t     #time module
import startendcal as stc #strantrange,endrange Calculator
import game as g     #game module

def guessthegame():
  stc.timer()
  startrange=stc.startrange()
  endrange=stc.endrange(startrange)
  game=g.game(startrange,endrange)

guessthegame()
