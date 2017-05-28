demoFile = "demo.txt"
writeMode = "w"
appendMode = "a"

myFile = open(demoFile, writeMode)
myFile.write("This is the first line.\n")
myFile.write("This is the second line.\n")
myFile.close()

print("\nFile written successfully.")
