
def power(x,y):

    if y % 2 == 0:
        return(power(x,y/2)*power(x,y/2))

    elif y % 2 == 1:
        return(x*power(x,y/2)*power(x,y/2))

    else:
        return(1)



def sorting(x):
    j = len(x)-1
    i = 0

    while i < len(x):

        if i >= j:
            break

        elif x[i] > 0 and x[j] < 0:
            temp = x[i]
            x[i] = x[j]
            x[j] = temp
            i = i + 1
            j = j-1


        elif x[i] > 0 and x[j] > 0:
            j=j-1

        else:
            i = i+1



    print(x)


x = [4, -5, -7, -3, 5, -8, 2, -200]

sorting(x)
