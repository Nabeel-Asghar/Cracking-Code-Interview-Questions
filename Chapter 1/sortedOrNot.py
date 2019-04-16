def sortedOrNot(x):

    for i in range(len(x)):

        if i==(len(x)-1):
            return "Sorted"
        elif x[i]<=x[i+1]:
            continue
        else:
            return "Not sorted"


x = [2,4,5,5,30,235,600]
print(sortedOrNot(x))
