#!/usr/bin/env python3

# motor_control.py
import socket
from src.TMC_2209.TMC_2209_StepperDriver import *

# Motor driver setup
tmc = TMC_2209(21, 16, 20)

tmc.set_direction_reg(False)
tmc.set_current(300)
tmc.set_interpolation(True)
tmc.set_spreadcycle(False)
tmc.set_microstepping_resolution(2)
tmc.set_internal_rsense(False)

tmc.set_acceleration(2000)
tmc.set_max_speed(500)

def my_callback(channel):
    print("StallGuard!")
    tmc.stop()

tmc.set_stallguard_callback(26, 5, my_callback)

# Socket setup
HOST = '127.0.0.1'
PORT = 5002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:
        conn, addr = s.accept()
        with conn:
            print(f'Connected by {addr}')
            data = conn.recv(1024)
            if data:
                position = int(data.decode())
                print(f'Setting motor position to {position} steps')

                tmc.set_motor_enabled(True)
                tmc.run_to_position_steps(position, MovementAbsRel.RELATIVE)
                tmc.set_motor_enabled(False)

