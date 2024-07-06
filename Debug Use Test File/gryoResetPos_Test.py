from Robosport_FuncMain import*


# Print gryo Heading
if hub.buttons.pressed() = (Button.BLUETOOTH):
    print(hub.imu.heading())
    
while True:
    GryoMove(0,0)