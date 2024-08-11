from Robosport_FuncMain import *

while True:
    GyroReset()
    GyroMoveStuck(0,100)
    GyroReset()
    MotorE.dc(-100)
    wait(2000)
    MotorE.stop()
    GyroMoveTime(0,-30,0.2)
    GyroMoveTime(85,100,0.5)
    GyroReset()
    GyroMoveTime(0,-50,0.2)
    GyroMoveTime(85,100,0.5)
    GyroMoveStuck(90,100)
    GyroReset()
    GyroMoveTime(0,-50,0.2)
    