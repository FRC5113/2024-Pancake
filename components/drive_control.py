import wpimath.controller
import magicbot
from magicbot.state_machine import state
from magicbot import tunable
import navx

from components.Drivetrain import Drivetrain


class DriveControl(magicbot.StateMachine):

    drivetrain: Drivetrain


    navx: navx.AHRS


    turn_to_angle_kP = tunable(0.03)
    turn_to_angle_kI = tunable(0)
    turn_to_angle_kD = tunable(0)

    def setup(self):
        self.turn_to_angle_controller = wpimath.controller.PIDController(
            self.turn_to_angle_kP, self.turn_to_angle_kI, self.turn_to_angle_kD
        )
        self.turn_to_angle_controller.enableContinuousInput(0, 360)

    def set_angle(self, angle: float):
        self.turn_to_angle_controller.setSetpoint(angle)

    def turn_to_angle(self, angle: float) -> None:

        self.set_angle(angle)
        self.engage(self.turning_to_angle)


    @state(first=True)
    def turning_to_angle(self):

        self.turn_to_angle_controller.setPID(
            self.turn_to_angle_kP, self.turn_to_angle_kI, self.turn_to_angle_kD
        )

        measurement = self.navx.getAngle()
        output = self.turn_to_angle_controller.calculate(measurement)
        self.drivetrain.arcadeDrive(0, (output, -0.3, 0.3))
