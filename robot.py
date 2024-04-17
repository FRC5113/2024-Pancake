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
        """remeber to change the ids
            only 2 motors cause pancake has 2 at the time of writing"""
        #self.frontleftmotor = phoenix5.WPI_TalonSRX(15)
        self.frontrightmotor = phoenix5.WPI_TalonSRX(18)
        self.backleftmotor = phoenix5.WPI_TalonSRX(55)
        #self.backrightmotor = phoenix5.WPI_TalonSRX(12)

        # Joystick for user input
        self.joy = wpilib.Joystick(0)

        # Gyroscope sensor for orientation tracking
        self.navx = navx.AHRS.create_spi()

        # Throttle value from joystick for controlling speed
        self.speed = self.joy.getThrottle()

    @property
    def get_angle(self):
        return self.navx.getAngle()

    # Teleop periodic function, called periodically during teleoperated mode
    def teleopPeriodic(self):

        # Drive the robot using arcade drive with adjusted speed
        self.drivetrain.arcadeDrive(
            -self.joy.getX() * 0.5,
            self.joy.getY() * 0.5
        )

        # If trigger on joystick is pressed, command the robot to turn to a specific angle
        if self.joy.getTrigger():
            self.drive_control.turn_to_angle(180)

        # Update SmartDashboard with joystick values and current gyroscope angle
        SmartDashboard.putNumber("Joystick X value", self.joy.getY())
        SmartDashboard.putNumber("Joystick Y value", self.joy.getX())
        SmartDashboard.putNumber("navx", self.navx.getAngle())
