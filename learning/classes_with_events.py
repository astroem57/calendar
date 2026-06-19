# This is the file in which the method of storing event data is described
# Learn CLASSES, figure out how to use them here
# when you want to define something but haven't used it yet use pass
class Event:
    def __init__(self, title, day, start_time, duration):
        self.title = title
        self.day = day
        self.start_time = start_time
        self.duration = duration
    
    def end_time(self):
        return self.start_time + self.duration
    

event = Event("Meeting", "January 1st", 8, 4)
print(event.start_time, "to", event.end_time())
print(event.day)
