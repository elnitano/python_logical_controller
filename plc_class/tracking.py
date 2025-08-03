#plc_class/tracking.py
#
# Handling Tracking
# Takes input as type - 1 = Small, 2 = Medium, 3 = Large
# Each type, has a position based on the Encoder counter which determines when the Sweeper should open
# As long as sensor is active on output conveyor, it should fill 1 - 3 in the tracking array, else 0 is filled in.
# Each Encoder Counter should move the position in the array 1 step forward.

class Tracking():
    def __init__(self):
        self.list = [0 for i in range(1000)]
        self.check_ctrl = False
        self.check_time = 200 #mS
        self.current_time = 0 #mS

    def update(self, encoder, input=0):
        if encoder:
            self.list = [input] + self.list[:-1]

    def check(self, number, position):
        if number == self.list[position]:
            return True
        return False