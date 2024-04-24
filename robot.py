import magicbot
import wpilib
import wpilib.drive
import phoenix5
from components.Drivetrain import Drivetrain
from wpilib import SmartDashboard
import navx
from components.drive_control import DriveControl


class MyRobot(magicbot.MagicRobot):
    # Define robot components
    drivetrain: Drivetrain
    drive_control: DriveControl

    # Creates objects as the definition implies
    def createObjects(self):
        # Motor controllers for the drivetrain
        """only 2 motors cause pancake has 2 at the time of writing"""
        self.rightmotor = phoenix5.WPI_TalonSRX(17)
        self.leftmotor = phoenix5.WPI_TalonSRX(22)

        # Joystick for user input
        self.joy = wpilib.XboxController(0)

        # Gyroscope sensor for orientation tracking
        self.navx = navx.AHRS.create_spi()


    @property
    def get_angle(self):
        return self.navx.getAngle()

    # Teleop periodic function, called periodically during teleoperated mode
    def teleopPeriodic(self):

        # Drive the robot using arcade drive with adjusted speed
        with self.consumeExceptions():
            self.drivetrain.arcade_drive(
                self.joy.getLeftY(),
                -self.joy.getLeftX(),
            )
        # Update SmartDashboard with joystick values and current gyroscope angle
        SmartDashboard.putNumber("Joystick X value", self.joy.getLeftY())
        SmartDashboard.putNumber("Joystick Y value", self.joy.getLeftX())
        SmartDashboard.putNumber("navx", self.navx.getAngle())
