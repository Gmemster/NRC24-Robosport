from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.iodevices import I2CDevice

'Identify Hub and Ports'
hub = EV3Brick()
ColorA=ColorSensor(Port.S1)
MotorC=Motor(Port.C)
MotorD=Motor(Port.D)
MotorE=Motor(Port.A)
Gyro=GyroSensor(Port.S2,direction=Direction.CLOCKWISE)

'Create Timer Function'
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
    Gyro.reset_angle(0)

def GyroMove(Angle,Speed):
    error=Angle-Gyro.angle()
    correction=error*3
    MotorC.dc(-Speed-correction)
    MotorD.dc(Speed-correction)

def GyroMoveTime(Angle,Speed,Time):
    timer.reset()
    while timer.time()<Time*1000:
        GyroMove(Angle,Speed)

def GyroMoveColor(Angle,Speed):
    while ColorA.color()!=Color.BLUE:
        GyroMove(Angle,Speed)
    RobotStop()

def GyroMoveDegrees(Angle,Speed,Degrees,Time,Stop):
    MotorC.reset_angle(0)
    MotorD.reset_angle(0)
    totalDegrees=0
    timer.reset()
    while totalDegrees<Degrees and timer.time()<Time*1000:
        totalDegrees=(abs(MotorC.angle())+abs(MotorD.angle()))
        GyroMove(Angle,Speed)
    if Stop==1:
        RobotStop()

def GyroMoveStuck(Angle,Speed):
    timer.reset()
    GyroMove(Angle,Speed)
    wait(300)
    while abs(MotorC.speed())>300 or abs(MotorD.speed())>300 and timer.time()<2000:
        GyroMove(Angle,Speed)
    RobotStop()

