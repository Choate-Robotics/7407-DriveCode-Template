import commands2
from robotpy_toolkit_7407.subsystem import Subsystem
import ctre
import ntcore
import wpilib
import command
import config
import constants
from robot_systems import Robot, Pneumatics, Sensors, LEDs, PowerDistribution, Field
import sensors
import subsystem
import utils
from oi.OI import OI


class Robot(wpilib.TimedRobot):
    def __init__(self):
        super().__init__()
        
        self.log = utils.LocalLogger("Robot")
        self.nt = ntcore.NetworkTableInstance.getDefault()

    def robotInit(self):
        self.log._robot_log_setup()
        # Initialize Operator Interface
        if config.DEBUG_MODE == True:
            self.log.setup("WARNING: DEBUG MODE IS ENABLED")
        OI.init()
        OI.map_controls()
        period = .03
        commands2.CommandScheduler.getInstance().setPeriod(period)
        self.log.info(f"Scheduler period set to {period} seconds")
        
        # Initialize subsystems
        def init_subsystems():
            subsystems: list[Subsystem] = list(
                {k: v for k, v in Robot.__dict__.items() if isinstance(v, Subsystem)}.values()
            )

            for subsystem in subsystems:
                subsystem.init()
                
        if config.DEBUG_MODE == False:
            try:
                init_subsystems()
            except Exception as e:
                self.log.error(e)
                self.nt.getTable('errors').putString('subsystem init', str(e))
        else:
            try:
                init_subsystems()
            except Exception as e:
                self.log.error(e)
                self.nt.getTable('errors').putString('subsystem init', str(e))
                raise e
        
        
        self.log.complete("Robot initialized")
    def robotPeriodic(self):
        if self.isSimulation():
            wpilib.DriverStation.silenceJoystickConnectionWarning(True)
        
        if config.DEBUG_MODE == False:
            try:
                commands2.CommandScheduler.getInstance().run()
            except Exception as e:
                self.log.error(e)
                self.nt.getTable('errors').putString('command scheduler', str(e))
        else:
            try:
                commands2.CommandScheduler.getInstance().run()
            except Exception as e:
                self.log.error(e)
                self.nt.getTable('errors').putString('command scheduler', str(e))
                raise e

    # Initialize subsystems

    # Pneumatics

    def teleopInit(self):
        self.log.info("Teleop initialized")

    def teleopPeriodic(self):
        pass
    def autonomousInit(self):
        self.log.info("Autonomous initialized")

    def autonomousPeriodic(self):
        pass

    def disabledInit(self) -> None:
        self.log.info("Robot disabled")

    def disabledPeriodic(self) -> None:
        pass


if __name__ == "__main__":
    wpilib.run(Robot)
