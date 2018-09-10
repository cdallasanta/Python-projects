for n in reversed(range(100)):
    if n>1:
        next = n-1
        print(str(n) +" bottles of beer on the wall, "+str(n)+" bottles of beer")
        print("Take one down, pass it around, "+ str(next) + "bottles of beer on the wall")
        print(" ")
    else:
        print(str(n)+" bottle of beer on the wall, "+str(n)+" bottle of beer")
        print("Take one down, pass it around, no more bottles of beer on the wall")
        print(" ")
