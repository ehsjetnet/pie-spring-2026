from typing import Final

"""
Constants file containing information such as motor controller IDs,
wheel radius, and more for editing convenience.
"""

class DriveConstants:
    # None as placeholder
    DRIVE_CONTROLLER_ID: Final[str] = None # Need to check in Dawn
    DRIVE_WHEEL_RADIUS: Final[float] = None # Need to measure, convert from inches to meters.
    DRIVE_MOTOR_TICKS_PER_ROTATION: Final[int] = 16 # Assuming same motor probably the same
    DRIVE_MOTOR_RATIO: Final[int] = 70 # Need to verify
    DRIVE_WHEEL_SPAN: Final[float] = 0.258 # May need to remeasure
    HUB_TO_WHEEL_GEAR_RATIO = 84 / 36 # gear further from motor / gear closer to motor (Remeasure)