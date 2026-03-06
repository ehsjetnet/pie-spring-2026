import devices
import constants
import util

"""
How each of these functions work:
1. When autonomous mode starts, your entire file will be loaded.
2. The code in autonomous_setup will then be run once
3. After that, the code in autonomous_main will be run at a rate of 20 times a second
4. Once the autonomous period ends, your code will be shut down. (There may be a pause as referees tally the score.)
5. When tele-operated mode starts, your entire file will be loaded once again.
6. The code in teleop_setup will then be run once
7. After that, the code in teleop_main will be run at a rate of 20 times a second
8. All code will stop running when the match eds.
"""

debug_logger = util.DebugLogger(default_interval=2000)

drive_wheel_left = devices.Wheel(
    debug_logger,
    devices.Motor(Robot, debug_logger, constants.DriveConstants.DRIVE_CONTROLLER_ID, "a")
    .set_invert(False)
    .set_pid(None,None,None),
    constants.DriveConstants.DRIVE_WHEEL_RADIUS,
    constants.DriveConstants.DRIVE_MOTOR_TICKS_PER_ROTATION * 
    constants.DriveConstants.DRIVE_MOTOR_RATIO * 
    constants.DriveConstants.HUB_TO_WHEEL_GEAR_RATIO
)

drive_wheel_right = devices.Wheel(
    debug_logger,
    devices.Motor(Robot, debug_logger, constants.DriveConstants.DRIVE_CONTROLLER_ID, "b")
    .set_invert(True)
    .set_pid(None,None,None),
    constants.DriveConstants.DRIVE_WHEEL_RADIUS,
    constants.DriveConstants.DRIVE_MOTOR_TICKS_PER_ROTATION * 
    constants.DriveConstants.DRIVE_MOTOR_RATIO * 
    constants.DriveConstants.HUB_TO_WHEEL_GEAR_RATIO
)

# Structural Function
def autonomous_setup():
    pass

# Structural Function
def autonomous_main():
    pass

# Structural Function
def teleop_setup():
    pass

# Structural Function
def teleop_main():
    """ 
    Note: need to implement loop via while true. 
    Unlike FTC, the teleop function doesn't loop on its own.

    Pretty important: 
    If you want to add a pause between a set of actions in the code.
    You need to create a coroutine and use
    the await keyword to delay the action for a set time while allowing
    the rest of the code to run.

    If you instead use something like sleep right in the teleop_main function, 
    the entire robot will remain unresponsive for the duration of that pause 
    rather than just pausing a specific robot action.
    """
    two_wheel_drive()

def two_wheel_drive_keyboard():
    drive_fwd = Keyboard.get_value("w")
    drive_back = Keyboard.get_value("s")
    turn_left = Keyboard.get_value("a")
    turn_right = Keyboard.get_value("d")
    drive = 0
    turn = 0

    # Below is theoretical, values may be reversed while testing
    if drive_fwd:
        drive = constants.DriveConstants.KEYBOARD_DRIVE_SPEED
    elif drive_back:
        drive = -constants.DriveConstants.KEYBOARD_DRIVE_SPEED
    elif drive_fwd and drive_back:
        print("Can't drive both forward and backwards")

    # Below is theoretical, values may be reversed while testing
    if turn_left:
        drive = constants.DriveConstants.KEYBOARD_TURN_SPEED
    elif turn_right:
        drive = -constants.DriveConstants.KEYBOARD_TURN_SPEED
    elif turn_left and turn_right:
        print("Can't turn left and right at the same time")

    left_drive_velocity = drive + turn
    right_drive_velocity = drive - turn
    velocity_limit = max(1.0, abs(left_drive_velocity), abs(right_drive_velocity))

    drive_wheel_left.set_velocity(left_drive_velocity/velocity_limit)
    drive_wheel_right.set_velocity(right_drive_velocity/velocity_limit)

# Teleop drive
def two_wheel_drive():
    drive = -Gamepad.get_value("joystick_left_y")
    turn = Gamepad.get_value("joystick_right_x")
    left_drive_velocity = drive + turn
    right_drive_velocity = drive - turn
    velocity_limit = max(1.0, abs(left_drive_velocity), abs(right_drive_velocity))
    
    # We divide the drive velocity by the max velocity to normalize it. This ensures that the value is between
    # 1 and -1.
    drive_wheel_left.set_velocity(left_drive_velocity/velocity_limit)
    drive_wheel_right.set_velocity(right_drive_velocity/velocity_limit)

#For testing purposes
if __name__ == "__main__":
    teleop_main()