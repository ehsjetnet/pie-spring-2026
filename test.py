# Substitute device IDs when using real robot
KOALA_BEAR = "6_17986660329004823992"

def autonomous_setup():
    pass

def autonomous_main():
    pass

def teleop_setup():
    print("Teleop mode has started!")
    
def teleop():
        # Arcade Drive
        forward_speed = 0
        turning_speed = 0
        if Keyboard.get_value("w"):
            forward_speed = 1
        elif Keyboard.get_value("s"):
            forward_speed = -1
        if Keyboard.get_value("d"):
            turning_speed = 1
        elif Keyboard.get_value("a"):
            turning_speed = -1
        Robot.set_value(KOALA_BEAR, "velocity_b", max(min((forward_speed + turning_speed), 1.0), -1.0))
        Robot.set_value(KOALA_BEAR, "velocity_a", max(min(forward_speed - turning_speed, 1.0), -1.0))

def autonomous_actions():
    pass
