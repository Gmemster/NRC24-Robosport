from Robosport_FuncMain import *

while True:

    GyroReset()
    GyroMoveDegrees(0,100,1200,2,1)
    GyroMoveTime(-35,0,0.5)
    MotorE.dc(-100)
    wait(1800)
    MotorE.stop()
    GyroMoveTime(-90,0,0.5)
    GyroMoveStuck(-90,60)

    GyroReset()
    GyroMoveDegrees(0,-50,100,0.5,1)
    GyroMoveTime(-70,80,0.3)
    GyroMoveTime(-80,100,0.5)
    GyroMoveStuck(-83,100)

    GyroReset()
    GyroMoveTime(0,-80,0.1)
    GyroMoveTime(-60,80,0.2)
    GyroMoveTime(-70,100,0.3)
    GyroMoveStuck(-75,100)

    GyroReset()
    GyroMoveTime(0,-80,0.1)
    GyroMoveTime(-80,100,1.5)
    GyroMoveTime(-100,0,0.2)
    MotorE.dc(-100)
    wait(1800)
    MotorE.stop()

