# This program uses the argument variables module from the sys package.
from sys import argv

# The arguments to be used in argv are script and filename.  Thse must be passed in the cli.
script, filename = argv

# Create a file object from the file in the location given to argv and assign it the name 'txt'.  Optionally, you can open the file in certain modes.
txt = open(filename)

# prints filename from argv
print(f"Here's your file {filename}:")
# prints contents of txt (open(filename))
print(txt.read())

txt.close()

# Below is the alternate, where you enter in prompt, rather than argv.

print("Type the filename again:")
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()