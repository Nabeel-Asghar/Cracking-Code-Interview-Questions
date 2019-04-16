#Program to determine if string is unique (no repeating letters)
#Sets use hashtable so the runtime is mostly O(1) and worst case is O(n)

def uniqueString(x):

    y = set(x)

    if len(x)==len(y):
        print("Unique")
    else:
        print("Not unique")


s = "anything"
uniqueString(s)
