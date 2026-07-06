#learning
with open("file.txt", "r") as file:
    fire = file.read()
    parts = fire.split(", ")
    recovered_word = parts[0]
    recovered_number = int(parts[1])
    recovered_number_2 = int(parts[2])
print(recovered_word, recovered_number, recovered_number_2)

#doing with a class
with open("player.txt", "r") as file_:
    read = file_.read()
    parts = read.split("<|> ")
    recovered_name = parts[0]
    recovered_user = parts[1]
    recovered_age = int(parts[2])
    recovered_level = int(parts[3])
print(recovered_name, recovered_user, recovered_age, recovered_level)