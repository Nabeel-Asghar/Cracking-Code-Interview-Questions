#Given two strings, check if one is a permutation of the other
#Python uses Timsort, which was named after Tim Peters, the Python developer who invented it. The Wikipedia page has complexity information:

#Worst case performance  O(nlogn)
#Best case performance   O(n)
#Average case performance    O(nlogn)

#Worst case space complexity O(n)

def permutation(x,y):

    if len(x)<len(y):
        print("Not permutation")

    else:

        a = sorted(x)
        b = sorted(y)

        x = ''.join(a)
        y = ''.join(b)

        if y in x:
            print("Permutation")
        else:
            print("Not permutation")

x = "water"
y = "atre"

permutation(x,y)
