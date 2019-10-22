def counter(i, x, y, n):
    while i < x:
        print(f"At the top i is {i}")
        n.append(i)

        i += y
        print("Numbers now: ", n)

start = input("Where to start? \n    > ")
max = input(f"OK, we'll start at {start}. Where should we stop? \n   > ")
inc = input(f"SICK!!! We'll stop at {max}.  How much should we increment by? \n    > ")

counter(int(start), int(max), int(inc), [])
