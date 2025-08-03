from plc_class.modbus import mb_client
from plc_class.group_start import Group_Start
from plc_class.conveyor import Conveyor
from plc_class.sweeper import Sweeper
from plc_class.tracking import Tracking
from plc_class.scale import Scale
from plc_function.scan_time import Scan_Time


def main():
    
    # Creates instance of Modbus Client
    modbus = mb_client()

    # Create instance for GroupStart
    group = Group_Start()

    # Create instances for Conveyors
    input_conveyor_1 = Conveyor(group, 1)
    scale_conveyor_1 = Conveyor(group, 2)
    output_conveyor_1 = Conveyor(group, 3)
    output_conveyor_2 = Conveyor(group, 4)
    small_box_conveyor_1 = Conveyor(group, 5)
    medium_box_conveyor_1 = Conveyor(group, 6)
    large_box_conveyor_1 = Conveyor(group, 7)

    # Create instances for Sweepers
    sweeper_1 = Sweeper(2500)
    sweeper_2 = Sweeper(2500)
    sweeper_3 = Sweeper(2500)

    # Create instance for Tracking
    tracking = Tracking()

    # Create instance for Scale
    scale = Scale()

    # Create Block for Input Conveyor & Scale Conveyor
    block_input_conveyor_1 = False
    block_scale_conveyor_1 = False

    last_time = 0
    while True:
        #Handle scan time of our Python Logical Controller
        cycle_time, last_time = Scan_Time(last_time)

        #Read Input Dict and Set Output Dict
        digital_input = modbus.read_digital_input()
        digital_output = modbus.get_outpust_dict()

        #Convert Start and Stop button to useful variables
        start_button = digital_input["Group Start"]
        stop_button = not digital_input["Group Stop"]

        #Get Weight and Update Instance
        current_weight = modbus.read_scale()
        current_package, block_scale_conveyor_1 = scale.update(current_weight, digital_input["Scale Conveyor 1 B1"], cycle_time)

        tracking_input = 0
        if digital_input["Input Conveyor 1 B1"]:
            tracking_input = current_package

        #Handling conveyor stop of Input and Scale Conveyor
        block_input_conveyor_1 = digital_input["Input Conveyor 1 B1"] and digital_input["Scale Conveyor 1 B1"]

        #Update Group Start
        group_ready, group_running, group_starting, group_stopped = group.update(digital_input["FACTORY I/O (Running)"], start_button, stop_button, cycle_time)

        #Update Tracking
        tracking.update(digital_input["Output Conveyor Encoder A"], tracking_input)

        #Update Conveyors
        digital_output["Input Conveyor 1 (F)"] = input_conveyor_1.update(group, block_input_conveyor_1)
        digital_output["Scale Conveyor 1 (F)"] = scale_conveyor_1.update(group, block_scale_conveyor_1)
        digital_output["Output Conveyor 1 (F)"] = output_conveyor_1.update(group)
        digital_output["Output Conveyor 2 (F)"] = output_conveyor_2.update(group)
        digital_output["Small Box Conveyor 1 (F)"] = small_box_conveyor_1.update(group)
        digital_output["Medium Box Conveyor 1 (F)"] = medium_box_conveyor_1.update(group)
        digital_output["Large Box Conveyor 1 (F)"] = large_box_conveyor_1.update(group)

        #Update Sweeper
        digital_output["Sweeper 1 Arm"], digital_output["Sweeper 1 Motor (F)"] = sweeper_1.update(group_running, tracking.check(1, 180), cycle_time)
        digital_output["Sweeper 2 Arm"], digital_output["Sweeper 2 Motor (F)"] = sweeper_2.update(group_running, tracking.check(2, 480), cycle_time)
        digital_output["Sweeper 3 Arm"], digital_output["Sweeper 3 Motor (F)"] = sweeper_3.update(group_running, tracking.check(3, 880), cycle_time)

        #Update Lamps
        digital_output["Group Stopped"] = group_stopped
        digital_output["Group Starting"] = group_starting
        digital_output["Group Running"] = group_running
        digital_output["Stop Lamp"] = group_stopped
        digital_output["Start Lamp"] = group_starting or group_running

        #Product Spawn
        digital_output["Product Spawn"] = group_running

        #Write PLC Outputs to Factory IO
        modbus.write_digital_output(digital_output)

        #Console log
        print(f'Factory IO Running: {group_ready} {current_package} {current_weight}  | Cycle Time: {cycle_time}ms            \r', flush=True, end="")
if __name__ == "__main__":
    main()
