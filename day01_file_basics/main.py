from datetime import datetime

time = datetime.now().strftime('%H:%M%p')
name = "Jordan"

with open('name_time.txt', 'w') as textFile:
	textFile.write(f"Hello {name}, the time is {time}")

print(f"Hello {name}, the time is {time}")