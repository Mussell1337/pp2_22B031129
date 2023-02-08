def solve(numheads, numlegs):
    if numlegs % 2 != 0 or numheads > numlegs or numheads  == 0:
        print("Incorrect value")
    else:
        rabbit = int((numlegs + (-2*numheads))/2)
        chicken = int(numheads - rabbit)
        print("Number of chickens: {} and number of rabbits: {}".format(chicken, rabbit))
numheads = int(input("heads: "))
numlegs = int(input("legs: "))
solve(numheads, numlegs)