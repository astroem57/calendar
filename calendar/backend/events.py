# make a class for events that includes key details
# make it so that if the user only knows end time or duration, the calendar can calculate both
#make it so that the user has to input an end time or duration

class Event:
    def __init__(self, title, year, month, day, hour = None, minute = None, duration = None, description = None):
        self.title = title
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.duration = duration
        self.description = description
          
    def print(self):
        print(self.title, self.year, self.month, self.day, self.hour, self.minute, self.duration, self.description)
    #fix after work
    def combine(self):
        combined = f"{.title}<|> {.year}<|> {.month}<|> {.day}<|> {event.hour}<|> {event.minute}<|> {event.duration}<|> {event.description}"
        return combined
    

    


def unstringify_event(combined):
    parts = combined.split("<|> ")
    title = parts[0]
    year = int(parts[1])
    month = int(parts[2])
    day = int(parts[3])
    hour = int(parts[4])
    minute = int(parts[5])
    duration = parts[6]
    description = parts[7]
    event = Event(title, year, month, day, hour, minute, duration, description)
    return event