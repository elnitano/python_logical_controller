#plc_class/scale.py
#
# Handling the Scale
# Weight input will determine the package on the scale.
# When Sensor on weight is triggered, the weight should take a snapshot.
# This Snapshot will be evalulated which package its handling.

class Scale():
    def __init__(self):
        self.last_category = 0
        self.stop_scale = False
        self.stop_time = 500 #mS
        self.current_time = 0 #mS

    def update(self, weight, sensor, cycle_time):
        if sensor:
            if self.current_time <= self.stop_time:
                self.stop_scale = True
                self.current_time += cycle_time
            elif self.stop_scale and self.current_time > self.stop_time:
                if weight < 4.7:
                    self.last_category = 1
                elif 4.7 < weight < 6.5:
                    self.last_category = 2
                else:
                    self.last_category = 3
                self.stop_scale = False
        elif not sensor:
            self.stop_scale = False
            self.current_time = 0
        return self.last_category, self.stop_scale