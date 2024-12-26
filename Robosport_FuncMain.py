from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

'Identify Hub and Ports'
hub = PrimeHub()
ColorA=ColorSensor(Port.A)
MotorC=Motor(Port.C)
MotorD=Motor(Port.D)
# MotorE=Motor(Port.E)
Ultrasonic=UltrasonicSensor(Port.B)


'Create timer function'
timer=StopWatch()


'Movement functions'
def RobotStart (Cpower,Dpower):
    MotorC.dc(-Cpower)
    MotorD.dc(Dpower)

def RobotStop():
    MotorC.brake()
    MotorD.brake()
    wait(200)

def GyroReset():
    hub.imu.reset_heading(0)

def GyroMove (Angle,Speed):
    error=Angle-hub.imu.heading()
    correction=error*3
    MotorC.dc(-Speed-correction)
    MotorD.dc(Speed-correction)

def GyroMoveTime (Angle,Speed,Time):
    timer.reset()
    while timer.time()<Time*1000:
        GyroMove(Angle,Speed)

def GyroMoveColor (Angle,Speed):
    while ColorA.color()!=Color.BLUE:
        print(ColorA.color())
        GyroMove(Angle,Speed)
    RobotStop()

def GyroMoveDegrees(Angle,Speed,Degrees,Time,Stop):
    MotorC.reset_angle(0)
    MotorD.reset_angle(0)
    totalDegrees=0
    timer.reset()
    while totalDegrees<Degrees and timer.time()<Time*1000:
        totalDegrees=(abs(MotorC.angle())+abs(MotorD.angle()))/2
        GyroMove(Angle,Speed)
    if Stop==1:
        RobotStop()

def GyroMoveStuck(Angle,Speed):
    timer.reset()
    GyroMove(Angle,Speed)
    wait(300)
    print(abs(MotorC.speed()),abs(MotorD.speed()))
    while abs(MotorC.speed())>600 or abs(MotorD.speed())>600 and timer.time()<2000:
        GyroMove(Angle,Speed)
    RobotStop()

#'---- Variable Turn-rate System ----'#
def GyroMoveVar(Angle,Speed,Turn):
    error=Angle-hub.imu.heading()
    correction=error*Turn
    MotorC.dc(-Speed-correction)
    MotorD.dc(Speed-correction)

def GyroMoveTurn(Angle,Speed,Time,Turn):
    timer.reset()
    while timer.time()<Time*1000:
        GyroMoveVar(Angle,Speed,Turn)
    RobotStop()


#Unusable
# def GyroMoveTilt(Angle,Speed,tAngle):
#     y=hub.imu.tilt()
#     while True:
#         y=hub.imu.tilt()
#         # GryoMove(Angle,Speed)
#         print (y[1])
#     RobotStop()
