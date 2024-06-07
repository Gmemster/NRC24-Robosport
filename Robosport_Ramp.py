from Robosport_FuncMain import*

'gryo respawn test'
# while True:
    # GryoMove(0,0)
# while True:
#     GyroMoveTilt(0,100)

while True:
    GryoReset()
    GyroMoveDegrees(0,100,1000,0)
    GryoMoveTime(0,100,1) #straight
    GryoMoveColor(0,80) #ramp_colour
    MotorE.dc(-100)
    wait(1500)
    MotorE.stop()
    GryoMoveTime(0,-45,0.3)
    GryoMoveTime(-80,0,0.1) #left wall
    GryoMoveTime(-80,100,0.5)
    GryoReset()
    GryoMoveTime(0,-30,0.2)
    GryoMoveTime(-80,0,0.1) #middle wall
    GryoMoveTime(-80,100,1)
    GryoMoveTime(-90,100,0.3) #align on intersection
    GryoReset()
    GryoMoveTime(0,-30,0.23)
    GryoMoveTime(-80,0,0.1) #right wall
    GryoMoveTime(-80,100,0.8)
    GryoMoveTime(-90,100,0.3)
    GryoReset()
    GryoMoveTime(0,-30,0.5)
    GryoMoveTime(-86,100,0.5) #ramp_colour_reset
    GryoMoveColor(-86,80)
    MotorE.dc(-100)
    wait(2000)
    MotorE.stop()
    GryoMoveTime(-80,-30,0.5)
    GryoMoveTime(-50,0,0.1) #pos_reset
    GryoMoveTime(-50,-80,0.23)
    GryoMoveTime(-80,-100,1.8)