import time

class TimeKeeper:

    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.api_count = 0

    def _get_current_time_ms(self):
        return time.time_ns() // 1_000_000

    def start(self):
        self.start_time = self._get_current_time_ms()

    def end(self):
        self.end_time = self._get_current_time_ms()

    def get_current_runtime(self):
        return (self._get_current_time_ms() - self.start_time) / 1000

    def is_past_threshold(self, threshold_in_sec):
        if threshold_in_sec is None:
            return False
        else:
            return self.get_current_runtime() > threshold_in_sec

    def get_elapsed_time_in_sec(self):
        return (self.end_time - self.start_time) / 1000