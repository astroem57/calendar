
# make a class for events that includes key details
# make it so that if the user only knows end time or duration, the calendar can calculate both
#make it so that the user has to input an end time or duration
class Event:
    def __init__(self, title, date, description, start_time, end_time = None, duration = None,):
        self.title = title
        self.date = date
        self.start_time = start_time
        self.description = description
#if the duration does not equal none then find end time but adding duration and start time
        if duration is not None:
            self.duration = duration
            self.end_time = duration + start_time
#if end_time is not none find the duration by taking start time from end time
        elif end_time is not None:
            self.end_time = end_time
            self.duration = duration
            self.duration = end_time - start_time
#test
event = Event("meeting", 1, "blah", 12, 13)

print(event.duration)

        
            
    
