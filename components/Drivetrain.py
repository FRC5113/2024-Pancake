import wpilib
import wpilib.drive
import phoenix5
from magicbot import will_reset_to



class Drivetrain:
    # Motor controllers for the drivetrain
    frontleftmotor: phoenix5.WPI_TalonSRX
    frontrightmotor: phoenix5.WPI_TalonSRX
    backleftmotor: phoenix5.WPI_TalonSRX
    backrightmotor: phoenix5.WPI_TalonSRX

    # Variables to reset to during each control loop iteration
    forward = will_reset_to(0)
    turn = will_reset_to(0)

    # Initialization setup function
    def setup(self):
        # Create motor controller groups for the right and left side
        self.rightmotor = wpilib.MotorControllerGroup(
            self.frontrightmotor, self.backrightmotor
        )
        self.leftmotor = wpilib.MotorControllerGroup(
            self.frontleftmotor, self.backleftmotor
        )

        # Create differential drive object for controlling the robot
        self.robotDrive = wpilib.drive.DifferentialDrive(
            self.leftmotor, self.rightmotor
        )

    # Method to set forward and turn values for arcade drive
    def arcadeDrive(self, forward, turn):
        self.forward = forward
        self.turn = turn

    # Method to execute arcade drive during each control loop iteration
    def execute(self):
        self.robotDrive.arcadeDrive(self.forward, self.turn)
