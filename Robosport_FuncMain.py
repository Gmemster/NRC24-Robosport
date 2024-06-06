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
MotorE=Motor(Port.E)


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

def GryoReset():
    hub.imu.reset_heading(0)

def GryoMove (Angle,Speed):
    error=Angle-hub.imu.heading()
    correction=error*5
    MotorC.dc(-Speed-correction)
    MotorD.dc(Speed-correction)

def GryoMoveTime (Angle,Speed,Time):
    timer.reset()
    while timer.time()<Time*1000:
        GryoMove(Angle,Speed)

def GryoMoveColor (Angle,Speed):
    while ColorA.color()!=Color.GREEN:
        print(ColorA.color())
        GryoMove(Angle,Speed)
    RobotStop()

def GyroMoveDegrees(Angle,Speed,Degrees,Time,Stop):
    MotorC.reset_angle(0)
    MotorD.reset_angle(0)
    totalDegrees=0
    timer.reset()
    while totalDegrees<Degrees and timer.time()<Time*1000:
        totalDegrees=(abs(MotorC.angle())+abs(MotorD.angle()))/2
        GryoMove(Angle,Speed)
    if Stop==1:
        RobotStop()

def GyroMoveStuck(Angle,Speed):
    timer.reset()
    while abs(MotorC.speed())>300 or abs(MotorD.speed())>300 and timer.time()<2000:
        print(MotorC.speed(),MotorD.speed(),ColorA.color())
        GryoMove(Angle,Speed)
    RobotStop()
