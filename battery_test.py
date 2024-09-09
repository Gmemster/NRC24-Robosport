from Robosport_FuncMain import *

voltage=hub.battery.voltage()/1000
current=hub.battery.current()/100
watthour=voltage*current
batterylevel=watthour/15.4*100


print(batterylevel)