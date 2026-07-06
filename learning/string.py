word = "hello"
number = 10
combined = f"{word}, {number}"
print(combined)
parts = combined.split(", ")

print(parts)

recovered_word = parts[0]
recovered_number = int(parts[1]) + 5

print(recovered_word, recovered_number)

