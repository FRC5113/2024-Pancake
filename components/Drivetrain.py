import wpilib
import wpilib.drive
import phoenix5
from magicbot import will_reset_to



class Drivetrain:
    # Motor controllers for the drivetrain
    leftmotor: phoenix5.WPI_TalonSRX
    rightmotor: phoenix5.WPI_TalonSRX

    # Variables to reset to during each control loop iteration
    forward = will_reset_to(0)
    turn = will_reset_to(0)

    # Initialization setup function
    def setup(self):

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
