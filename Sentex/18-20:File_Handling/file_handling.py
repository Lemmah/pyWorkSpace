# Initialize the requriments
# file_name, accessmodes
MYFILE = "example_file.txt"
WRITE = "w"
READ = "r"
APPEND = "a"

# write mode
write_file = open(MYFILE, WRITE)
write_file.write("This is the first text.")
write_file.close()

# read mode
read_file = open(MYFILE, READ)
print(read_file.readlines())
read_file.close()

# append mode
append_file = open(MYFILE, APPEND)
append_file.write("\nThis is a second bit of info.")
append_file.close()

# reading just to confirm changes
read_file = open(MYFILE, READ)
print(read_file.readlines())
read_file.close()
