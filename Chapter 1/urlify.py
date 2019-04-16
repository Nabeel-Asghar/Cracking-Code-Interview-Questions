#Method to replace all empty spaces in a string with "%20"
#O(N)

def urlify(x):

    x = list(x)

    i=0
    while i < len(x):
        if x[i] == " ":
            x[i] = "%20"
        i = i+1

    x = ''.join(x)

    print(x)

x = "Hello World It's Nabeel"
urlify(x)
