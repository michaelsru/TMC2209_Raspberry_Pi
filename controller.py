#!/usr/bin/env python3

from src.TMC_2209.TMC_2209_StepperDriver import *
tmc = TMC_2209(21, 16, 20)

tmc.set_direction_reg(False)
tmc.set_current(300)
tmc.set_interpolation(True)
tmc.set_spreadcycle(False)
tmc.set_microstepping_resolution(2)
tmc.set_internal_rsense(False)

tmc.set_acceleration(2000)
tmc.set_max_speed(500)

tmc.set_motor_enabled(True)

tmc.run_to_position_steps(-1000, movement_abs_rel=MovementAbsRel.ABSOLUTE)
tmc.run_to_position_steps(0, movement_abs_rel=MovementAbsRel.RELATIVE)

tmc.set_motor_enabled(False)
