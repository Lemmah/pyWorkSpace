# One advantage of the while loop is the while True loop
# Creating infinite loops

while True:
    stop = str(input("Say stop:"))
    if stop.lower() == "stop":
        print("Bye bye.")
        break
