#Compute polynomial

def polynomial(coef,x):

    p = len(coef)

    i = 0
    y = 0
    for i in range(p):
        p = p-1
        y = y + coef[i] * x**p

    print(y)


coef = [5,4,3,2,1]
x = 5
polynomial(coef, x)
