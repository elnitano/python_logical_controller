# plc_class/modbus.py
# 
# This package allows us to make connection from our Python program, to Factory IO
# The settings on Factory IO is set for following:
# IP: 10.13.37.200 (This is my IP on my PC)
# Port: 502 (Default Modbus Port)
# ID: 1 (Default ID number)
#
# I/O Points:
# Digital Inputs:
# -- Offset: 0
# -- Count: 32
#
# Digital Outputs:
# -- Offset: 0
# -- Count: 32
#
# Register Inputs
# -- Offset: 0
# -- Count: 8
#
# Register Outputs
# -- Offset: 0
# -- Count: 8

from pyModbusTCP.client import ModbusClient
from .dict_setup import digital_input_dict, digital_output_dict

class mb_client():
    def __init__(self):
        self.client = ModbusClient(host="10.13.37.200", port=502, unit_id=1, auto_open=True)

    # When calling read_digital_input() it will return a list of input from 0 to 31
    # read_discrete_inputs(start address, numbers of inputs to read)
    def read_digital_input(self):
        try:
            input_list = self.client.read_discrete_inputs(0, 32)
        except:
            raise Exception("Error while reading digital input!")
        
        input_dict = digital_input_dict
        index = 0
        for k, v in input_dict.items():
            input_dict[k] = input_list[index]
            index += 1
        return input_dict
    
    # When calling write_digital_output() it will be take the outputs list and write it to output addr. 0
    def write_digital_output(self, output_dict):
        output_list = []
        for v in output_dict.values():
            output_list.append(v)
        try:
            self.client.write_multiple_coils(0, output_list)
        except:
            raise Exception("Error while writing digital output!")

    # Return empty output Dictionary
    def get_outpust_dict(self):
        return digital_output_dict

    # When calling read_scale() it will return a list of inputs, in our case we only use 1 for the scale.
    # Value is received as 1000 = 10kg
    # We scale the output, by dividing with 100 to get the correct kg
    def read_scale(self):
        try:
            analog_list = self.client.read_input_registers(0, 1)
        except:
            raise Exception("Error while reading analog input!")
        scale = analog_list[0] / 100
        return scale