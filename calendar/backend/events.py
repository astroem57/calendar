
class Event:
    def __init__(self, title, date, description, start_time, end_time = None, duration = None,):
        self.title = title
        self.date = date
        self.start_time = start_time
        self.description = description

        if duration is not None:
            self.duration = duration
            self.end_time = duration + start_time
        
        elif end_time is not None:
            self.end_time = end_time
            self.duration = duration
            self.duration = end_time - start_time
event = Event("meeting", 1, "blah", 12, 13)

print(event.duration)

        
            
    
