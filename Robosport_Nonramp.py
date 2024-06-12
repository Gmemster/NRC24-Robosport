from Robosport_FuncMain import*

'gryo respawn test'
# while True:
#     GryoMove(0,0)

while True:
    GryoReset()
    GryoMoveTime(0,100,1.5)
    MotorE.dc(-100)
    wait(1200)
    MotorE.stop()
    GryoMoveTime(0,-30,0.2)
    GryoMoveTime(85,0,0.1)
    GryoMoveTime(85,100,0.7)#turn to the right wall
    GryoReset()
    GryoMoveTime(0,-30,0.2)
    GryoMoveTime(85,0,0.1)
    GryoMoveTime(85,100,1.8)#straights to the middle wall
    GryoReset()
    GryoMoveTime(0,-30,-0.2)
    GryoMoveTime(85,0,0.1)
    GryoMoveTime(85,100,1)#facing left wall
    GryoReset()
    GryoMoveTime(0,-30,0.2)
    GryoMoveTime(85,0,0.1)
    GryoMoveTime(85,100,1.5)
    GryoReset()
    GryoMoveTime(0,-30,0.2)
    GryoMoveTime(-30,-50,1.2)#middle field
    GryoMoveTime(0,-50,2)