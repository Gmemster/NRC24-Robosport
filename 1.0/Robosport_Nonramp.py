from Robosport_FuncMain import*

'Gyro respawn test'
# while True:
#     GyroMove(0,0)

while True:
    GyroReset()
    GyroMoveTime(0,100,1.5)
    MotorE.dc(-100)
    wait(1200)
    MotorE.stop()
    GyroMoveTime(0,-30,0.2)
    GyroMoveTime(85,0,0.1)
    GyroMoveTime(85,100,0.7)#turn to the right wall
    GyroReset()
    GyroMoveTime(0,-30,0.2)
    GyroMoveTime(85,0,0.1)
    GyroMoveTime(85,100,1.8)#straights to the middle wall
    GyroReset()
    GyroMoveTime(0,-30,-0.2)
    GyroMoveTime(85,0,0.1)
    GyroMoveTime(85,100,1)#facing left wall
    GyroReset()
    GyroMoveTime(0,-30,0.2)
    GyroMoveTime(85,0,0.1)
    GyroMoveTime(85,100,1.5)
    GyroReset()
    GyroMoveTime(0,-30,0.2)
    GyroMoveTime(-30,-50,1.2)#middle field
    GyroMoveTime(0,-50,2)