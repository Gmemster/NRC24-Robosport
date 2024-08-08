from Robosport_FuncMain import*

'Gyro respawn test'
# while True:
    # GyroMove(0,0)
# while True:
#     GyroMoveTilt(0,100)

while True:
    GyroReset()
    GyroMoveDegrees(0,100,1000,0)
    GyroMoveTime(0,100,1) #straight
    GyroMoveColor(0,80) #ramp_colour
    MotorE.dc(-100)
    wait(1500)
    MotorE.stop()
    GyroMoveTime(0,-45,0.3)
    GyroMoveTime(-80,0,0.1) #left wall
    GyroMoveTime(-80,100,0.5)
    GyroReset()
    GyroMoveTime(0,-30,0.2)
    GyroMoveTime(-80,0,0.1) #middle wall
    GyroMoveTime(-80,100,1)
    GyroMoveTime(-90,100,0.3) #align on intersection
    GyroReset()
    GyroMoveTime(0,-30,0.23)
    GyroMoveTime(-80,0,0.1) #right wall
    GyroMoveTime(-80,100,0.8)
    GyroMoveTime(-90,100,0.3)
    GyroReset()
    GyroMoveTime(0,-30,0.5)
    GyroMoveTime(-86,100,0.5) #ramp_colour_reset
    GyroMoveColor(-86,80)
    MotorE.dc(-100)
    wait(2000)
    MotorE.stop()
    GyroMoveTime(-80,-30,0.5)
    GyroMoveTime(-50,0,0.1) #pos_reset
    GyroMoveTime(-50,-80,0.23)
    GyroMoveTime(-80,-100,1.8)