#if the duration does not equal none then find end time by adding duration and start time
        if duration is not None:
            self.duration = duration
            self.end_time = duration + start_time
#if end_time is not none find the duration by taking start time from end time
        elif end_time is not None:
            self.end_time = end_time
            self.duration = duration
            self.duration = end_time - start_time