class Conveyor():
    def __init__(self, Group_Start, start_number):
        self.ready = Group_Start.ready
        self.running = Group_Start.running
        self.stopped = Group_Start.stopped
        self.current_number = Group_Start.upstart_number
        self.upstart_number = start_number

    def update(self, Group_Start, block=False):
        self.ready = Group_Start.ready
        self.running = Group_Start.running
        self.stopped = Group_Start.stopped
        self.current_number = Group_Start.upstart_number
        if self.running and self.current_number >= self.upstart_number and not block:
            return True
        return False