formatter = "{} {} {} {}"

# Takes the formatter string defined in line 1,
# Calls format function,
# Passes four arguments to format, 
# Replaces {} with the four vars.
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))