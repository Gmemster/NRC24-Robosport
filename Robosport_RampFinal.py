from Robosport_FuncMain import *


GyroReset()
GyroMoveTime(0,100,1)
MotorE.dc(-100)
wait(2000)
MotorE.stop()
GyroMoveTime(-150,20,0.6)
GyroMoveTime(-165,100,0.4)
GyroMoveStuck(-175,100)
GyroReset()
GyroMoveTime(0,-100,0.3)
GyroMoveTurn(-90,100,1,1.2)
GyroReset()
GyroMoveTime(0,-100,0.25)
GyroMoveTurn(-90,100,1,1.4)
MotorE.dc(-100)
wait(2000)
MotorE.stop()
# GyroMoveTurn(-179,0)
# GyroMoveTime(-90,100,0.3)