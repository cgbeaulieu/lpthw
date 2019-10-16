# this one is like your scripts with argv
# define a function named print_two with args as arguments. Do the below when this function is called. 
def print_two(*args):
    # unpacks arguments.  args has two arguments, arg1 and arg 2
    arg1, arg2 = args
    # print the arguments and strings.
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()