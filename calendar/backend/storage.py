from events import Event
def save(filename, event):
    with open(filename, "a") as file:
        file.write(event.title + "\n")
        file.write(event.date + "\n")
        file.write(event.start_time + "\n")
        file.write(event.duration + "\n")
        file.write(event.description + "\n")
    
def load(filename):
    with open(filename, "r") as file:
        lines = [line.strip() for line in file.readlines()]
    return lines