#Determines if string is one letter away from the other strings

def oneaway(x,y):

    a = len(x)
    b = len(y)

    if a-b>=1 or b-a>=1:
        if a-b==1:
            if y in x:
                print("One insert away")
            else:
                print("False")
        if b-a==1:
            if x in y:
                print("One deletion away")
            else:
                print("False")
    else:
        print("False")






x = "pales"
y = "bake"
oneaway(x,y)
