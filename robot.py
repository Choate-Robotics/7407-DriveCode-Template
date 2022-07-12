import commands2
import wpilib

import autonomous
import command
import oi
import sensors
import subsystem
import utils
import config
import constants
import robot_systems


class Robot(wpilib.TimedRobot):
    def __init__(self):
        super().__init__()

    def robotInit(self):
        # Initialize Operator Interface
        oi.OI.OI.init()
        oi.OI.OI.map_controls()

    # Initialize subsystems

    # Pneumatics

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass


if __name__ == "__main__":
    wpilib.run(Robot)
