from plc_class.modbus import mb_client
from plc_class.group_start import Group_Start
from plc_function.scan_time import Scan_Time

def main():
    
    # Creates instance of Modbus Client
    modbus = mb_client()

    # Create instance for GroupStart
    group = Group_Start(False)
    last_time = 0
    while True:
        #Read Input Dict and Set Output Dict
        digital_input = modbus.read_digital_input()
        digital_output = modbus.get_outpust_dict()

        start_button = digital_input["Group Start"]
        stop_button = not digital_input["Group Stop"]

        group_ready, group_started, group_stopped = group.update(digital_input["FACTORY I/O (Running)"], start_button, stop_button)
        if group_ready:
            #Handle scan time of our Python Logical Controller
            cycle_time, last_time = Scan_Time(last_time)

            #Update Lamps
            digital_output["Group Stopped"] = group_stopped
            digital_output["Stop Lamp"] = group_stopped
            digital_output["Group Running"] = group_started
            digital_output["Start Lamp"] = group_started

            #Write PLC Outputs to Factory IO
            modbus.write_digital_output(digital_output)

            #Console log
            print(f'Factory IO Running: {group_ready} {start_button} {stop_button} | Cycle Time: {cycle_time}ms            \r', flush=True, end="")
if __name__ == "__main__":
    main()
