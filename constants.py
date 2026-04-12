from typing import Final
import util

"""
Constants file containing information such as motor controller IDs,
wheel radius, and more for editing convenience.
"""

class DriveConstants:
    # None as placeholder
    DRIVE_CONTROLLER_ID: Final[str] = "6_17986660329004823992" # Need to check in Dawn
    DRIVE_WHEEL_RADIUS: Final[float] = 0.101 # Need to measure, convert from inches to meters.
    DRIVE_MOTOR_TICKS_PER_ROTATION: Final[int] = 16 # Assuming same motor probably the same
    DRIVE_MOTOR_RATIO: Final[int] = 50 # Need to verify
    DRIVE_WHEEL_SPAN: Final[float] = 0.152 # May need to remeasure
    # original for above: 0.258 meters
    HUB_TO_WHEEL_GEAR_RATIO: Final[float] = 36 / 36 # gear further from motor / gear closer to motor (Remeasure)
    KEYBOARD_DRIVE_SPEED: Final[float] = 0.8 # placeholder, may change after testing
    KEYBOARD_TURN_SPEED: Final[float] = 0.8 # placeholder, may change after testing

class ArmConstants:
    ARM_CONTROLLER_ID: Final[str] = "6_10978819230753236066"
    ARM_LENGTH: int = util.inches_to_meters(14)
    FOREARM_LENGTH: int = util.inches_to_meters(13.7)
    ARM_MOTOR_TPR: int = 16
    ARM_MOTOR_RATIO: int = 50
    HUB_TO_ARM_GEAR_RATIO: int = 84/36

class CardReader:
    CARD_CONTROLLER_ID: Final[str] = "6_446663227023814261"



