from Robosport_FuncMain import*

'gryo respawn test'
# while True:
    # GryoMove(0,0)
#yz is gay

while True:
    GryoReset()
    GyroMoveDegrees(0,100,950,3,0)
    GyroMoveDegrees(0,50,100,2,1)
    MotorE.dc(-100)
    wait(2000)
    MotorE.stop()
    GryoMoveTime(-80,0,1) #left wall
    GryoMoveTime(-85,50,0.5)
    GyroMoveStuck(-85,50)

    GryoReset()
    GryoMoveTime(0,-30,0.1)
    GryoMoveTime(-70,100,0.8)
    GryoMoveTime(-85,100,1)
    GyroMoveStuck(-90,50)

    GryoReset()
    GryoMoveTime(0,-30,0.2)
    GryoMoveTime(-75,100,0.8)
    GyroMoveStuck(-85,50)

    GryoReset()
    GryoMoveTime(0,-30,0.2)
    GyroMoveDegrees(-80,100,900,3,0)
    GyroMoveDegrees(-85,50,100,2,1)
    MotorE.dc(-100)
    wait(2000)
    MotorE.stop()

    GryoMoveTime(-75,-100,1)
    GyroMoveStuck(-90,-60)