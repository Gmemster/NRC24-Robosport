from Robosport_FuncMain import*

totalDegrees = 0
totalDegrees=(abs(MotorC.angle())+abs(MotorD.angle()))/2

MotorC.reset_angle(0)
MotorD.reset_angle(0)

while True:
    print(totalDegrees)

    if hub.buttons.pressed() = (Button.LEFT or Button.RIGHT):
        MotorC.reset_angle(0)
        MotorD.reset_angle(0)