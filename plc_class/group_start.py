class Group_Start():
    def __init__(self, factoryio_running):
        self.ready = factoryio_running,
        self.running = False
        self.stopped = True

    def update(self, factoryio_status, start_button, stop_button):
        if factoryio_status:
            self.ready = True
            if start_button:
                self.running = True
                self.stopped = False
            if stop_button:
                self.running = False
                self.stopped = True
        else:
            self.ready = False
            self.running = False
            self.stopped = True
        return self.ready, self.running, self.stopped