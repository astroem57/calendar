from events import Event
#ignore 
combined = f"{event.title}<|> {event.date}<|> {event.description}<|> {event.start_time}<|> {event.end_time}<|> {event.duration}"
with open("event.txt", "a") as file:
    file.write(combined)

with open("event.txt", "r") as file2:
    read = file2.read()
    parts = read.split("<|> ")
    recovered_title = parts[0]
    recovered_date = parts[1]
    recovered_description = parts[2]
    recovered_start_time = parts[3]
    recovered_end_time = parts[4]
    recovered_duration = parts[5]
print(recovered_title, recovered_date, recovered_description, recovered_start_time, recovered_end_time, recovered_duration)

events = []
