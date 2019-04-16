#String compression, ex. aabbcc -> a2b2c2

def compression(x):

    listx = list(x)
    ourList = []

    i=0
    count = 0
    a = len(x)
    while i<a:
        if listx[i]:
            count = 1
            print(count)
            i=i+1
        elif listx[i]==listx[i-1]:
            count = count + 1
            print(count)
            i=i+1

        elif listx[i]!=listx[i-1]:
            print(count)
            ourList.append(count)
            ourList.append(listx[i])
            count = 0
            i=i+1

    print(ourList)


x = "aabbcc"
compression(x)
