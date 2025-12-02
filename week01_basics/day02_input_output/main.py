from datetime import datetime

time = datetime.now().strftime("%H:%M%p")

print("Enter your name")
name = input("> ")

with open('name.txt', 'w') as file:
	file.write(f"Hello {name}, the time is {time}")

with open('name.txt', 'r') as file:
	print(file.read())
