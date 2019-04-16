#Program to determine if input is a power of 4

def getInput():
    #File input, split into list, line by line
    fileinput = open("input.txt","r")
    info = fileinput.read().split("\n")
    fileinput.close()
    return info

def powerOfFour(x):
    #Convert binary to integer
    x = int(x,2)

    while (x % 4 == 0):
         x /= 4

    return x


def main():
    intInput = getInput()
    for i in intInput:
        if powerOfFour(i) == 1:
            print(i,"-", int(i,2), "is a power of 4")
        else:
            print(i,"-", int(i,2), "is not a power of 4")

if __name__ == "__main__":
    main()
