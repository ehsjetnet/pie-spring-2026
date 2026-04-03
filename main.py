import devices
import constants
import math
import util
import time

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
robot = None
keyboard = None
actions = None

def initialize():
    global robot, drive_wheel_left, drive_wheel_right, arm_base, keyboard, base_arm_motor
    # actions = Actions
    robot = Robot
    keyboard = Keyboard
    drive_wheel_right = devices.Wheel(   
        devices.Motor(robot, constants.DriveConstants.DRIVE_CONTROLLER_ID, "a")
        .set_invert(True)
        .set_pid(None,None,None),
        constants.DriveConstants.DRIVE_WHEEL_RADIUS,
        constants.DriveConstants.DRIVE_MOTOR_TICKS_PER_ROTATION * 
        constants.DriveConstants.DRIVE_MOTOR_RATIO * 
        constants.DriveConstants.HUB_TO_WHEEL_GEAR_RATIO
    )

    drive_wheel_left = devices.Wheel(
        devices.Motor(robot, constants.DriveConstants.DRIVE_CONTROLLER_ID, "b")
        .set_invert(True)
        .set_pid(None,None,None),
        constants.DriveConstants.DRIVE_WHEEL_RADIUS,
        constants.DriveConstants.DRIVE_MOTOR_TICKS_PER_ROTATION * 
        constants.DriveConstants.DRIVE_MOTOR_RATIO * 
        constants.DriveConstants.HUB_TO_WHEEL_GEAR_RATIO
    )

    base_arm_motor = devices.Motor(robot, constants.ArmConstants.ARM_CONTROLLER_ID, "b").set_invert(True)

    arm_base = devices.Arm(
        devices.PidMotor(robot, constants.ArmConstants.ARM_CONTROLLER_ID, "b")
        .set_invert(False)
        .set_pid(0.08, 0, 0),
        constants.ArmConstants.ARM_LENGTH,
        constants.ArmConstants.ARM_MOTOR_TPR * constants.ArmConstants.ARM_MOTOR_RATIO * constants.ArmConstants.HUB_TO_ARM_GEAR_RATIO,
        0
    )

# Structural Function
def autonomous():
    initialize()
    print("Autonomous set up")
    while(True):
        base_arm_motor.set_velocity(0.65)
        # drive_wheel_left.set_velocity(0.2)
        # drive_wheel_right.set_velocity(0.2)


def two_wheel_drive_keyboard(drive_fwd, drive_back, turn_left, turn_right):
    drive = 0
    turn = 0

    # Below is theoretical, values may be reversed while testing
    if drive_fwd:
        drive = constants.DriveConstants.KEYBOARD_DRIVE_SPEED
        print("drive_fwd")
    elif drive_back:
        drive = -constants.DriveConstants.KEYBOARD_DRIVE_SPEED
        print("drive_back")
    elif drive_fwd and drive_back:
        print("Can't drive both forward and backwards")

    # Below is theoretical, values may be reversed while testing
    if turn_left:
        turn = constants.DriveConstants.KEYBOARD_TURN_SPEED
        print("turn_left")
    elif turn_right:
        turn = -constants.DriveConstants.KEYBOARD_TURN_SPEED
        print("turn_right")
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
    left_drive_velocity = turn + drive
    right_drive_velocity = turn - drive
    # turn = -Gamepad.get_value("joystick_left_y")
    # drive = Gamepad.get_value("joystick_right_x")
    # left_drive_velocity = drive + turn
    # right_drive_velocity = drive - turn
    velocity_limit = max(1.0, abs(left_drive_velocity), abs(right_drive_velocity))
    
    # We divide the drive velocity by the max velocity to normalize it. This ensures that the value is between
    # 1 and -1.
    drive_wheel_left.set_velocity(left_drive_velocity/velocity_limit)
    drive_wheel_right.set_velocity(right_drive_velocity/velocity_limit)

def arm_testing():
    move_up = Gamepad.get_value("button_y")
    move_down = Gamepad.get_value("button_a")
    if move_up:
        base_arm_motor.set_velocity(0.60)
        # slowprint("Arm encoder reading: " + base_arm_motor.get_encoder())
    elif move_down:
        base_arm_motor.set_velocity(-0.25)
        # slowprint("Arm encoder reading: " + base_arm_motor.get_encoder())
    else:
        base_arm_motor.set_velocity(0)
        base_arm_motor.reset_encoder()
        # slowprint("Arm encoder reading " + base_arm_motor.get_encoder())

def arm_pid_testing():
    move_up = Gamepad.get_value("button_y")
    move_down = Gamepad.get_value("button_a")
    if move_up:
        arm_base.set_velocity(0.40)
        # slowprint("Arm encoder reading: " + base_arm_motor.get_encoder())
    elif move_down:
        arm_base.set_velocity(-0.25)
        # slowprint("Arm encoder reading: " + base_arm_motor.get_encoder())
        # slowprint("Arm encoder reading " + base_arm_motor.get_encoder())

# Structural Function
def teleop():
    # Teleop setup
    print("Teleop setup is running")
    initialize()
    # Teleop loop
    while True:
        # drive_fwd = Keyboard.get_value("up_arrow")
        # drive_back = Keyboard.get_value("down_arrow")
        # turn_left = Keyboard.get_value("left_arrow")
        # turn_right = Keyboard.get_value("right_arrow")
        # two_wheel_drive_keyboard(drive_fwd, drive_back, turn_left, turn_right)
        two_wheel_drive()
        arm_pid_testing()
        

# #For testing purposes
# if __name__ == "__main__":
#     teleop_main()

async def slowprint(value):
    print(value)
    # actions.sleep(2.0)
