def partition(arr,low,high):
    print(arr)
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low , high):

        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

#Brute force
def brute(x,y):

    C = []

    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                C.append(x[i])
    return C

# Driver code to test above
x = [1,2,3,4,5,6,7]
y = [2,3,7,6,8]

n = len(x)
print(x[0])
