from Robosport_FuncMain import*

'gryo respawn test'
# while True:
    # GryoMove(0,0)
#yz is gay

while True:
    GyroReset()
    GyroMoveDegrees(0,100, 950,3,0) #move like 60% of the way there
    GyroMoveDegrees(0,50,150,2,1) #move slower
    GyroMoveTime(-30,50,0.7)
    RobotStop()
    MotorE.dc(-100)
    wait(2000)
    MotorE.stop()
    GyroMoveDegrees(-30,-100,300,0.7,0)
    #GyroMoveTime(-30,-100,0.5)
    GyroMoveTime(-80,0,1) #left wall
    GyroMoveTime(-85,75,0.5)
    GyroMoveStuck(-85,50)

    GyroReset()
    GyroMoveTime(0,-30,0.1)
    GyroMoveTime(-70,100,0.8)
    GyroMoveTime(-85,100,1)
    GyroMoveStuck(-90,50)

    GyroReset()
    GyroMoveTime(0,-30,0.2)
    GyroMoveTime(-75,100,0.8)
    GyroMoveStuck(-85,50)

    GyroReset()
    GyroMoveTime(0,-30,0.2)
    GyroMoveDegrees(-80,100,900,3,0)
    GyroMoveDegrees(-85,50,100,2,1)
    MotorE.dc(-100)
    wait(2000)
    MotorE.stop()

    GyroMoveTime(-75,-100,1)
    GyroMoveStuck(-90,-60)