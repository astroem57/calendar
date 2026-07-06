from events import Event
def save(filename, event):
    with open(filename, "a") as file:
        #make the file write out each attribute line by line
        file.write(event.title + "\n")
        file.write(event.date + "\n")
        file.write(event.start_time + "\n")
        file.write(event.duration + "\n")
        file.write(event.description + "\n")
#seperate the events by five lines
def load(filename):
    with open(filename, "r") as file:
        # use line.strip to take away white space
        lines = [line.strip() for line in file.readlines()]
    return lines