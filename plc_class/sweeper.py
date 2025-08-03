#plc_class/sweeper.py
#
# Handling the Sweeper on Conveyor
# It opens Sweeper, and turn on Sweeper Conveyor when signaled
# It will stay so until open_time has finished

class Sweeper():
    def __init__(self, open_time):
        self.opened = False
        self.open_time = open_time #mS
        self.current_open = 0 #mS

    def update(self, running, open, cycle_time):
        if open and running and not self.opened:
            self.opened = True

        if not running:
            self.opened = False
        
        if self.opened:
            self.current_open += cycle_time
            if self.current_open > self.open_time:
                self.opened = False
                self.current_open = 0

        return self.opened, self.opened