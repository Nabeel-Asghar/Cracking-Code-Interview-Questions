#Find if a word is a palindrome
#O(N)

def palindrome(x):

    i=0
    n=len(x)-1

    while i<=n:
        if x[i] == x[n-i]:
            i = i+1
            b = 1
        else:
            return("Not palindrome")

    if b==1:
        return("Palindrome")


x = "racecar"
print(palindrome(x))
