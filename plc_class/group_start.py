#plc_class/group_start.py
#
# Handling group start
# When group is started, the upstart counter starts
# It counts up every self.upstart_time
# This is to ensure start current of motors don't exceed max current (for simulation purposes)

class Group_Start():
    def __init__(self):
        self.ready = False
        self.running = False
        self.stopped = True
        self.upstart_number = 0
        self.max_upstart = 10
        self.upstart_time = 1000 #mS
        self.current_time = 0 #mS

    def update(self, factoryio_status, start_button, stop_button, cycle_time):
        if factoryio_status:
            self.ready = True
            if start_button:
                self.running = True
                self.stopped = False
            if stop_button:
                self.running = False
                self.stopped = True
                self.upstart_number = 0
            
            if self.running: # This is made for simulation purpose, to ensure conveyors dont all start at once.    
                if self.upstart_number < self.max_upstart:
                    self.current_time += cycle_time
                    if self.current_time > self.upstart_time:
                        self.upstart_number += 1
                        self.current_time -= self.upstart_time
        else:
            self.ready = False
            self.running = False
            self.stopped = True
            self.upstart_number = 0

        group_starting = self.running and self.upstart_number < self.max_upstart
        group_running = self.running and self.upstart_number >= self.max_upstart
        return self.ready, group_running, group_starting, self.stopped