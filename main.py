import devices.py

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
    pass