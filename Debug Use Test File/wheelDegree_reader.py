from Robosport_FuncMain import*

MotorC.reset_angle(0)
MotorD.reset_angle(0)

while True:
    print(MotorC.angle,MotorD.angle)

    if hub.buttons.pressed() = (Button.LEFT or Button.RIGHT):
        MotorC.reset_angle(0)
        MotorD.reset_angle(0)